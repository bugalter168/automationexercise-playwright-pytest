# AutomationExercise UI Test Suite

Playwright + pytest automation for all 26 test cases listed on
[automationexercise.com/test_cases](https://www.automationexercise.com/test_cases),
built as a Page Object Model with Allure reporting, parallel/cross-browser
execution, and a CI pipeline that publishes the Allure report to GitHub Pages
and notifies Slack.

## Tech stack

Python 3.11+, `playwright`, `pytest`, `pytest-playwright`, `pytest-xdist`,
`allure-pytest`, `python-dotenv`, `faker`.

## Project structure

```
pages/            Page Object Model — one class per page, all built on BasePage
  base_page.py    Wraps Playwright actions with Allure steps + screenshots
  components.py   Shared widgets: NavBar, CategorySidebar, SubscriptionWidget
  ...
tests/            test_tc01_register_user.py ... test_tc26_scroll_up_without_arrow_button.py
utils/            Faker data generator, constants, API cleanup client
data/             Static fixtures (sample_upload.txt for TC6)
conftest.py       Fixtures: page objects, base_url, ad-blocking, user/account cleanup
.github/workflows/ci.yml   CI: matrix browsers -> Allure report -> GitHub Pages -> Slack
```

## Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
playwright install --with-deps

cp .env.example .env   # adjust BASE_URL if needed
```

`.env` variables:

| Variable   | Default                              | Purpose                          |
|------------|---------------------------------------|-----------------------------------|
| `BASE_URL` | `https://www.automationexercise.com` | Target site under test           |
| `HEADLESS` | `true`                                | Informational; use `--headed` to run with a visible browser |

## Running locally

```bash
# Full suite, headless, chromium (default)
pytest

# A specific browser
pytest --browser firefox
pytest --browser webkit

# Headed, for local debugging
pytest --browser chromium --headed

# Parallel execution across CPU cores
pytest -n auto

# Parallel + specific browser
pytest -n auto --browser firefox

# A single test case
pytest tests/test_tc01_register_user.py

# With Allure results written to a custom directory
pytest --alluredir=allure-results
```

Browser selection uses `pytest-playwright`'s built-in `--browser` flag, so all
three engines (chromium, firefox, webkit) work without any custom CLI plumbing.

## Allure report

Results are written to `allure-results/` (see `pytest.ini`). To view them
locally you need the [Allure commandline](https://allurereport.org/docs/gettingstarted/):

```bash
allure serve allure-results
# or
allure generate allure-results --clean -o allure-report
allure open allure-report
```

Each `BasePage` action (click, fill, hover, assertion, ...) is wrapped in an
`allure.step(...)` with a screenshot attached; a full-page screenshot is also
attached automatically on test failure (see `pytest_runtest_makereport` in
`conftest.py`).

## How CI works

`.github/workflows/ci.yml` runs on push/PR to `main` and on manual dispatch:

1. **`test` job** — matrix over `chromium` / `firefox` / `webkit`. Each leg
   installs dependencies, installs only the browser it needs, and runs
   `pytest -n auto --browser <browser>`, uploading its own `allure-results/<browser>`
   as an artifact regardless of pass/fail.
2. **`report` job** — downloads all three result sets, merges them, computes
   pass/fail/total counts, restores the previous report's history from the
   `gh-pages` branch (so trend charts keep working), regenerates the Allure
   report, and publishes it to `gh-pages` via `peaceiris/actions-gh-pages`.
   The resulting Pages URL is exposed as a job output.
3. **`notify-slack` job** — posts a message via `slackapi/slack-github-action`
   (Bot token) with overall status, pass/fail/total counts, branch/commit, and
   a link to the deployed Allure report. Runs on both success and failure.

Enable GitHub Pages once, for the `gh-pages` branch, root folder, in the
repo's Settings → Pages. The report will then be live at:

```
https://<owner>.github.io/<repo>/
```

### Required GitHub Secrets

| Secret               | Purpose                                    |
|-----------------------|---------------------------------------------|
| `SLACK_BOT_TOKEN`    | Bot token (`xoxb-...`) with `chat:write` scope |
| `SLACK_CHANNEL_ID`   | Channel ID the bot has been invited to      |

`GITHUB_TOKEN` (automatically supplied by Actions) is used to publish the
`gh-pages` branch — no extra secret needed for that part.

## Test data & cleanup

- User registration data is generated per-test with `Faker` (`utils/data_generator.py`),
  so tests never collide on email addresses.
- Any account created during a test is deleted again as part of that test's
  own documented steps (matching the official test-case scripts). As a
  safety net, the `registered_user` / `existing_user` fixtures also call the
  site's `DELETE /api/deleteAccount` REST endpoint in teardown, so a test that
  fails mid-flow never leaves a stray account behind for the next run.
- Ad-network requests (`googlesyndication`, `doubleclick`, etc.) are aborted
  for every test (`conftest.py::block_ad_requests`) so ad iframes never render
  and intercept clicks.
- The Contact Us form's native `window.confirm()` dialog is auto-accepted in
  `ContactPage.submit()`.

## Notes on flakiness

No fixed `sleep()` calls are used anywhere; all waits rely on Playwright's
auto-waiting and explicit `expect(...)` assertions (see `BasePage`), which
retry until the element/state is ready or the assertion times out.

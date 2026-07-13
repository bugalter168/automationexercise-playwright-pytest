# 5-Minute Demo Video Script — English (B2 level)

> Screen sharing ON. **[SHOW]** = what to display. **[SAY]** = read this out loud.
> Simple, clear English. Total ~5 minutes. Practice once before recording.

---

## 0:00 — Intro (30s)

**[SHOW]** The GitHub repo page with the README open.

**[SAY]**
"Hi, my name is Oleksandr. In this video I will show you my test automation
framework. It covers all 26 test cases from automationexercise.com. I built it
with Python, Playwright and pytest. It uses the Page Object Model pattern. It
also has Allure reports, parallel and cross-browser runs, and a CI pipeline that
publishes the report to GitHub Pages and sends a message to Slack. Let me show
you the structure."

---

## 0:30 — Project structure (45s)

**[SHOW]** The file tree: `pages/`, `tests/`, `utils/`, `conftest.py`, `.github/workflows/ci.yml`.

**[SAY]**
"The project is split by responsibility. The `pages` folder has the Page Objects.
There is one class for each page of the website. The `tests` folder has one file
for each test case, from `test_tc01` to `test_tc26`. The `utils` folder has the
Faker data generator and an API client for cleanup. `conftest.py` holds all the
pytest fixtures. And this file, `ci.yml`, is the CI pipeline. The main idea is the
Page Object Model. The test logic is separated from the page locators. So if the
UI changes, I only update one place."

---

## 1:15 — BasePage: the core pattern (1m)

**[SHOW]** Open `pages/base_page.py`. Scroll slowly through `click`, `fill`, `expect_visible`.

**[SAY]**
"This is the most important class — `BasePage`. Every Page Object inherits from
it. I do not call Playwright directly. Instead, I wrap each action — `click`,
`fill`, `check`, `expect_visible` — in a helper method. Each wrapper does three
things. First, it opens an Allure step with a clear description. Second, it does
the Playwright action. Third, it attaches a screenshot. So every step in every
test gets a description and a screenshot in the report automatically. I do not
repeat this code in each test. The descriptions are parametrized — I pass the
text as an argument. For checks I use Playwright's `expect`. It waits
automatically, so the tests are stable and not flaky."

**[SHOW]** Open `pages/login_page.py` for a moment.

**[SAY]**
"Here is a real Page Object — the Login page. In the constructor I define all the
locators. I use stable `data-qa` attributes. Then I expose actions like `login`
and `signup`, and check methods like `expect_login_error_visible`. The tests
never see a raw selector. They only call these methods with clear names."

---

## 2:15 — A test walkthrough (40s)

**[SHOW]** Open `tests/test_tc02_login_valid.py`.

**[SAY]**
"This is Test Case 2 — login with a valid email and password. At the top you can
see the Allure decorators: feature, story, severity and a readable title. The
test reads like simple English. Load the home page. Check it is visible. Go to
login. Log in. Check 'logged in as username'. Then delete the account. The
`existing_user` argument is a fixture. It creates a new account before the test
and removes it after. So every test is independent and repeatable."

---

## 2:55 — conftest.py: fixtures, data, cleanup (45s)

**[SHOW]** Open `conftest.py`. Point to `block_ad_requests`, `registered_user`, `existing_user`, `pytest_runtest_makereport`.

**[SAY]**
"All the shared setup is in `conftest.py`. I have a fixture for each Page Object,
so a test just asks for what it needs. The `generate_user` function uses Faker to
create unique test data. So registration tests never clash. The `registered_user`
and `existing_user` fixtures make sure we clean up. They delete the account
through the API in teardown, even if the test fails early. There is also an
autouse fixture, `block_ad_requests`. It blocks ad requests, so the ad iframes
never load and never steal our clicks. And this hook, `pytest_runtest_makereport`,
attaches a full-page screenshot to Allure when a test fails."

---

## 3:40 — Running: parallel and cross-browser (30s)

**[SHOW]** A terminal with these commands ready:
```
pytest                         # default chromium
pytest -n auto                 # parallel across CPU cores
pytest --browser firefox       # cross-browser
pytest --browser webkit
```

**[SAY]**
"To run the suite I just type `pytest`. With `-n auto` the tests run in parallel
across all CPU cores, using pytest-xdist. I choose the browser with a CLI
argument — `--browser firefox` or `--browser webkit`. This comes from the
pytest-playwright plugin. So the same tests run on Chromium, Firefox and WebKit
with no code changes."

---

## 4:10 — Allure report (25s)

**[SHOW]** Run `allure serve allure-results`. Open one test and expand the steps to show the screenshots.

**[SAY]**
"After a run I open the Allure report. Every test shows its steps with the
descriptions from BasePage. Each step has a screenshot. The tests are grouped by
feature and severity. And the graphs show pass and fail trends over time."

---

## 4:35 — CI pipeline, GitHub Pages, Slack (35s)

**[SHOW]** Open `.github/workflows/ci.yml`, then the Actions tab, then the live GitHub Pages report, then the Slack channel with a message.

**[SAY]**
"The last part is the pipeline. On every push it runs a matrix of three jobs, one
for each browser, in parallel. It installs the dependencies, runs the tests and
uploads the Allure results. The report job merges the results, builds the Allure
report with history, and deploys it to GitHub Pages. Here is the live report. The
last job sends a Slack message with the official Slack GitHub Action. It posts the
passed and failed counts, the branch, and a direct link to the report. So the
full loop is: push code, run tests on three browsers, publish the report, and
notify the team."

---

## 5:00 — Close (10s)

**[SAY]**
"So this is the framework: Page Object Model, a reusable BasePage with Allure
steps and screenshots, Faker data with automatic cleanup, parallel cross-browser
runs, and a full CI pipeline with reporting and Slack. Thank you for watching."

---

## Recording tips
- Generate the Allure report and the Slack message **before** recording. Then just switch tabs.
- Speak slowly. Five minutes is enough for this outline.
- It is fine to paraphrase. Examiners grade understanding, not accent.

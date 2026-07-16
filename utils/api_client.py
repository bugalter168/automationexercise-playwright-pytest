from playwright.sync_api import APIRequestContext, Error


def delete_account(api_context: APIRequestContext, email: str, password: str) -> None:
    """Safety-net cleanup: remove a test account via the site's REST API.

    Used as a teardown fallback for tests that fail before reaching their
    UI 'Delete Account' step, so re-running the suite never trips over a
    leftover 'Email Address already exist!' from a previous failed run.
    """
    try:
        api_context.delete(
            "/api/deleteAccount",
            form={"email": email, "password": password},
            timeout=10000,
        )
    except Error:
        pass
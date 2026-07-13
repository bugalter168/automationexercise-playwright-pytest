import requests


def delete_account(base_url: str, email: str, password: str) -> None:
    """Safety-net cleanup: remove a test account via the site's REST API.

    Used as a teardown fallback for tests that fail before reaching their
    UI 'Delete Account' step, so re-running the suite never trips over a
    leftover 'Email Address already exist!' from a previous failed run.
    """
    try:
        requests.delete(
            f"{base_url}/api/deleteAccount",
            data={"email": email, "password": password},
            timeout=10,
        )
    except requests.RequestException:
        pass

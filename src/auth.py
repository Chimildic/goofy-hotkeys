from google_auth_oauthlib.flow import InstalledAppFlow as Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from os import getenv, path


CREDENTIALS_FILE = getenv("CREDENTIALS_FILE")


def get_credentials():
    if path.isfile(CREDENTIALS_FILE):
        credentials = Credentials(
            None).from_authorized_user_file(CREDENTIALS_FILE)
    else:
        credentials = _run_flow()
        _write_file(credentials)
    if credentials.refresh_token and credentials.expired:
        credentials.refresh(Request())
        _write_file(credentials)
    return credentials


def _run_flow():
    filepath = getenv("SECRETS_FILE")
    scopes = getenv("SCOPES").split(",")
    flow = Flow.from_client_secrets_file(filepath, scopes)
    flow.run_local_server()
    return flow.credentials


def _write_file(credentials: Credentials):
    with open(CREDENTIALS_FILE, "w") as f:
        f.write(credentials.to_json())

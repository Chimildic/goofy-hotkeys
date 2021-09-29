from googleapiclient.discovery import build
from os import getenv
from auth import get_credentials


class AppsScript():

    def __init__(self, id: str):
        self._name = getenv("API_SERVICE_NAME")
        self._version = getenv("API_VERSION")
        self._id = id

    def run(self, function: str):
        body = {"function": function}
        with build(self._name, self._version, credentials=get_credentials()) as service:
            return service.scripts().run(scriptId=self._id, body=body).execute()

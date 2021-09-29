from os import path, getenv
import json


SETTINGS_FILE = getenv("SETTINGS_FILE")


def get_settings():
    if path.isfile(SETTINGS_FILE):
        with open(SETTINGS_FILE) as f:
            return json.load(f)

import keyboard
from os import getenv
from apps_script import AppsScript
from settings import get_settings
from loguru import logger

#TODO: class vs module
class ScriptService():

    def __init__(self):
        format = "{time:DD-MM-YYYY HH:mm:ss} | {level} | {message}"
        logger.add("logs.txt", format=format, retention="3 days")
        values = get_settings()
        id = values["scriptId"] if values["scriptId"] else getenv("SCRIPT_ID")
        self._script = AppsScript(id)
        self._hotkeys = values["hotkeys"]

    def start_listening(self):
        self._register_hotkeys()
        keyboard.wait(self._hotkeys["exit"])
        logger.info("Exit (pressed \"{}\")", self._hotkeys["exit"])

    def _register_hotkeys(self):
        self._add_hotkey(self._hotkeys["reload"], self._on_reload)
        for item in self._hotkeys["goofy"]:
            k, f = item["keys"], item["function"]
            self._add_hotkey(k, self._on_callback, args=(f, k))

    def _unregister_hotkeys(self):
        for item in self._hotkeys["goofy"]:
            keyboard.clear_hotkey(item["keys"])

    def _add_hotkey(self, keys, callback, args=()):
        # lambda bug: https://github.com/boppreh/keyboard/issues/493
        keyboard.add_hotkey(keys, lambda: keyboard.call_later(callback, args))

    def _on_reload(self):
        logger.info("Reload (pressed \"{}\")", self._hotkeys["reload"])
        self._unregister_hotkeys()
        self._hotkeys = get_settings()["hotkeys"]
        self._register_hotkeys()

    def _on_callback(self, function, keys):
        logger.info("Run function \"{}\" (pressed \"{}\")", function, keys)
        response = self._script.run(function)
        logger.info("Result of \"{}\": {}", function, response)

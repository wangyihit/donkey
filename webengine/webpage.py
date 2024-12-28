#!/usr/bin/env python
# encoding=utf-8
import logging


from PySide6.QtCore import Signal
from PySide6.QtWebEngineCore import QWebEnginePage
from webengine.cookiejar import CookieJar
from common.settings import Settings

class WebPage(QWebEnginePage):
    signalFinished = Signal(str)

    def __init__(self, settings:Settings):
        super(WebPage, self).__init__(parent=None)
        self._settings = settings
        self.loadFinished.connect(self._on_load_finished)
        # set cookie_jar in network_access_manager
        self._cookie_store = self.profile().cookieStore()
        self._cookie_jar = CookieJar(self._cookie_store)
        self._cookie_store.cookieAdded.connect(self._cookie_jar.handle_add_cookie)

    def _on_load_finished(self, ok):
        logging.info(f"WebPage loaded, status: {ok}")
        qt_cookies = self._cookie_jar.to_qt_cookies()
        curl_cookies = self._cookie_jar.to_curl_cookies()
        curl_cookie_path = self._settings["curl_cookies"]
        qt_cookie_path = self._settings["qt_cookies"]

        with open(curl_cookie_path, "w") as f:
            f.write(curl_cookies)

        with open(qt_cookie_path, "w") as f:
            f.write(qt_cookies)
        self.signalFinished.emit(self.url().toString())
        self.runJavaScript('console.log("js run");')

    def load_cookies(self):
        cookie_path = self._settings["qt_cookies"]
        data = open(cookie_path).read()
        self.set_cookies(data)

    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        logging.info(f"WebPage console message:{level}, {lineNumber}, {sourceID} {message}"),


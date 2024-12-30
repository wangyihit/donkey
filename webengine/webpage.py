#!/usr/bin/env python
# encoding=utf-8
import logging
import os

from PySide6.QtCore import Signal, QUrl
from PySide6.QtWebEngineCore import QWebEnginePage, QWebEngineNavigationRequest
from webengine.cookiejar import CookieJar
from common.settings import Settings

class WebPage(QWebEnginePage):
    signalFinished = Signal(str)

    def __init__(self, settings:Settings, parent=None):
        super(WebPage, self).__init__(parent=parent)
        self._settings = settings
        self.loadFinished.connect(self._on_load_finished)
        # set cookie_jar in network_access_manager
        self._cookie_store = self.profile().cookieStore()
        self._cookie_jar = CookieJar(self._cookie_store)
        self._cookie_store.cookieAdded.connect(self._cookie_jar.handle_add_cookie)

    def _on_load_finished(self, ok):
        logging.info(f"WebPage loaded, status: {ok}")

    def load_cookies(self):
        cookie_path = self._settings["qt_cookies"]
        if not os.path.exists(cookie_path):
            logging.info(f"Cookies file {cookie_path} does not exist")
            return
        logging.info(f"Loading cookies from {cookie_path}")
        data = open(cookie_path).read()
        self._cookie_jar.set_cookies(data)

    # virtual method
    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        logging.info(f"WebPage console message:{level}, {lineNumber}, {sourceID} {message}"),

    def acceptNavigationRequest(self, url:QUrl, navigation_type:QWebEnginePage.NavigationType, main_frame:bool):
        # const QUrl &url, QWebEnginePage::NavigationType type, bool isMainFrame
        logging.info(f"WebPage accepting navigation request: url={url.toString()}, type={navigation_type}, main_frame={main_frame}")
        return super(WebPage, self).acceptNavigationRequest(url, navigation_type, main_frame)

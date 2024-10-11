#!/usr/bin/env python
# encoding=utf-8

from PySide6.QtWebEngineCore import QWebEnginePage
from webengine.cookiejar import CookieJar


class QQMailLoginStatus(object):
    LOGIN_WITH_USER_INFO = 0
    INPUT_VERIFY_CODE = 1


class WebPage(QWebEnginePage):

    def __init__(self, settings):
        super(WebPage, self).__init__()
        self._settings = settings
        self.loadFinished.connect(self._on_load_finished)
        # set cookie_jar in network_access_manager
        self._cookie_jar = CookieJar()

    def set_cookies(self, cookies):
        self._cookie_jar.load_qt_cookie(cookies)


    def _on_load_finished(self, ok):
        qt_cookies = self._cookie_jar.to_qt_cookies()
        curl_cookies = self._cookie_jar.to_curl_cookies()
        with open("curl_cookies.txt", "w") as f:
            f.write(curl_cookies)

        with open("qt_cookies.txt", "w") as f:
            f.write(qt_cookies)

    def load_cookies(self, cookies):
        self._cookie_jar.load_qt_cookie(cookies)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from PySide6.QtCore import QTimer

from webengine.webpage import WebPage
from overrides import override

class DonkeyWebPage(WebPage):

    def __init__(self, settings, parent=None, ):
        super(DonkeyWebPage, self).__init__(settings, parent)
        self._cookie_timer = QTimer(self)
        self._cookie_timer.timeout.connect(self._handle_save_cookies)


    @override
    def _on_load_finished(self, ok):
        super(DonkeyWebPage, self)._on_load_finished(ok)
        self._handle_save_cookies()
        self._cookie_timer.start(5000)


    def _handle_save_cookies(self):
        logging.info("Saving cookies")
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

    # virtual method
    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        return


if __name__ == '__main__':
    pass

#!/usr/bin/env python
# encoding=utf-8
import sys
import logging
from PySide6.QtWidgets import QApplication
from common.settings import settings, Settings
from webengine.browser import Browser
from webengine.app import g_app


if __name__ == "__main__":
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)
    logging.info("app start")
    app = QApplication(sys.argv)
    settings = Settings()
    proxy_host = settings["proxy_host"]
    proxy_port = settings["proxy_port"]
    if proxy_host and proxy_port:
        pass

    browser = Browser(settings)
    g_app.browser = browser
    g_app.settings = settings
    g_app.app = app
    browser.load_url("https://www.douyin.com/follow")
    app.exec()

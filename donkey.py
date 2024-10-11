#!/usr/bin/env python
# encoding=utf-8
import sys

from PySide6.QtWidgets import QApplication
from common.settings import settings, Settings
from webengine.browser import Browser
from webengine.app import g_app


if __name__ == "__main__":
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
    html_path = settings["in_html"]
    cookies_path = settings["in_cookies"]
    browser.load_url("https://www.baidu.com")
    app.exec()

#!/usr/bin/env python
# encoding=utf-8
import sys
from PyQt5.QtNetwork import QNetworkProxy
from PyQt5.QtWidgets import QApplication
from common.settings import settings, Settings
from webkit.browser import Browser


def set_proxy(host, port):
    proxy = QNetworkProxy()
    proxy.setType(QNetworkProxy.HttpProxy)
    proxy.setHostName(host)
    proxy.setPort(port)
    QNetworkProxy.setApplicationProxy(proxy)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    settings = Settings()
    proxy_host = settings["proxy_host"]
    proxy_port = settings["proxy_port"]
    if proxy_host and proxy_port:
        set_proxy(proxy_host, proxy_port)

    browser = Browser(settings)

    html_path = settings["in_html"]
    cookies_path = settings["in_cookies"]
    if html_path and cookies_path:
        url = "https://mail.qq.com/cgi-bin/loginpage"
        with open(html_path) as f:
            html = f.read()
        with open(cookies_path) as f:
            cookies = f.read()
        browser.load_html(html, url, cookies)
    else:
        browser.load_url("https://mail.qq.com/cgi-bin/loginpage")
    app.exec_()

#!/usr/bin/env python
# encoding=utf-8
import sys
from PyQt5.QtNetwork import QNetworkProxy
from PyQt5.QtWidgets import QApplication
from common.settings import settings, Settings
from webkit.browser import Browser
from webkit.app import g_app


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
    g_app.browser = browser
    g_app.settings = settings
    g_app.app = app
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
        # browser.load_url("https://mail.qq.com/cgi-bin/loginpage")
        url ="https://ui.ptlogin2.qq.com/cgi-bin/login?style=9&appid=522005705&daid=4&s_u…ogin=%E8%AE%B0%E4%BD%8F%E7%99%BB%E5%BD%95%E7%8A%B6%E6%80%81&pt_no_onekey=1"
        browser.load_url("https://mail.qq.com")
    app.exec_()

#!/usr/bin/env python
# encoding=utf-8

from PySide6.QtCore import QUrl, QObject, QDate, QDateTime
from PySide6.QtNetwork import QNetworkCookie
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView

from webengine.cookiejar import CookieJar
from webengine.webpage import WebPage
from webengine.webview import WebView


class Browser(QObject):
    android_default = "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3882.0 Mobile Safari/537.36";
    ios_default = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1";
    pc_default = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36";

    def __init__(self, settings, webpage:QWebEnginePage=None, webview:QWebEngineView=None):
        super(Browser, self).__init__()
        self._settings = settings
        self._webengine_profile = QWebEngineProfile.defaultProfile()
        self._webengine_profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.NoPersistentCookies)
        # QWebEngineProfile.defaultProfile().setHttpUserAgent(self.pc_default)
        self._web_page = webpage if webpage is not None else WebPage(settings)
        self._web_view = webview if webview is not None else WebView(settings)
        self._web_view.setPage(self._web_page)


        # QWebEngineProfile::defaultProfile()->setHttpUserAgent(userAgent)


    def load_url(self, url, show_ui=True):
        self._web_page.load_cookies()
        self._web_view.load(QUrl(url))
        if show_ui is True:
            self._web_view.show()

    def load_html(self, html:str, url:str, cookies="", show_ui=True):
        # if len(cookies) > 0:
        #     self.set_cookies(cookies)
        self._web_view.setHtml(html, QUrl(url))
        if show_ui is True:
            self._web_view.show()

    def get_network_cookies(self, domain:str=None):
        return self._web_page._cookie_jar.network_cookies(domain)

    def add_cookie(self, name:str, value:str, path="/", domain="sugh.szu.edu.cn", secure=True, http_only=False, max_age=None):
        # name=k, value=v, path="/", domain="sugh.szu.edu.cn", secure=True, http_only=False,
        self._web_page._cookie_jar.add_cookie(name, value, path, domain, secure, http_only, max_age)


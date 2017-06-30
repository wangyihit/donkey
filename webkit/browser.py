#!/usr/bin/env python
# encoding=utf-8

from PyQt5.QtCore import QUrl
from networkaccessmanager import NetworkAccessManager
from cookiejar import CookieJar
from webpage import WebPage
from webview import WebView


class Browser(object):

    def __init__(self, settings):
        super(Browser, self).__init__()
        self._settings = settings
        self._cookie_jar = CookieJar()
        self._network_access_manager = NetworkAccessManager(self._cookie_jar)
        self._web_page = WebPage(settings)
        self._web_page.setNetworkAccessManager(self._network_access_manager)
        self._web_view = WebView(settings)
        self._web_view.setPage(self._web_page)

    def load_url(self, url, show_ui=True):
        self._web_view.load(QUrl(url))
        if show_ui is True:
            self._web_view.show()

    def load_html(self, html, url, cookies="", show_ui=True):
        if len(cookies) > 0:
            self._web_page.cookie_jar.load_qt_cookie(cookies)
        self._web_view.setHtml(html, QUrl(url))
        if show_ui is True:
            self._web_view.show()

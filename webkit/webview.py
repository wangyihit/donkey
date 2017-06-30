#!/usr/bin/env python
# encoding=utf-8

from PyQt5.QtWebKitWidgets import QWebView


class WebView(QWebView):

    def __init__(self, settings):
        super(WebView, self).__init__()
        self._settings = settings


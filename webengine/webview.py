#!/usr/bin/env python
# encoding=utf-8

from PySide6.QtWebEngineWidgets import QWebEngineView


class WebView(QWebEngineView):

    def __init__(self, settings):
        super(WebView, self).__init__()
        self._settings = settings


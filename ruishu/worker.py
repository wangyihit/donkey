#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from PySide6.QtCore import QObject
from PySide6.QtCore import Signal
from PySide6.QtWebEngineWidgets import QWebEngineView

from webengine.browser import Browser


class RuiShuiWorker(QObject):
    signal_generate_cookie = Signal(str)

    def __init__(self):
        super().__init__()
        self.browser = None

    def connect_browser(self, browser:Browser):
        self.browser = browser

    def download_url(self, url):
        self.emit(self.signal_generate_cookie("run"))
    # slots
    def handler_download(self, param:dict):
        logging.info(f"handler download: {param}")




if __name__ == '__main__':
    pass

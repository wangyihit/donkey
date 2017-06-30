#!/usr/bin/env python
# encoding=utf-8

import argparse
from PyQt5.QtWebKit import QWebSettings

settings = None


class Settings(object):

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--proxy_host", default="", type=str)
        parser.add_argument("--proxy_port", default=0, type=int)
        parser.add_argument("--in_cookies", default="", type=str)
        parser.add_argument("--out_cookies", default="", type=str)
        parser.add_argument("--cache_path", default="", type=str)
        parser.add_argument("--uname", default="", type=str)
        parser.add_argument("--upass", default="", type=str)
        parser.add_argument("--in_html", default="", type=str)
        parser.add_argument("--out_html", default="", type=str)
        self.parser = parser
        self.args = parser.parse_args()
        self._set_webkit_settings()

    @staticmethod
    def _set_webkit_settings():
        webkit_settings = QWebSettings.globalSettings()
        webkit_settings.setAttribute(QWebSettings.DeveloperExtrasEnabled, True)

    def __getitem__(self, item):
        return getattr(self.args, item)




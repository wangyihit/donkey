#!/usr/bin/env python
# encoding=utf-8

import argparse
# from PySide6.QtWebKit import QWebSettings

settings = None


class Settings(object):

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--proxy_host", default="", type=str)
        parser.add_argument("--proxy_port", default=0, type=int)
        parser.add_argument("--curl_cookies", default="cookies.txt", type=str)
        parser.add_argument("--qt_cookies", default="qt_cookies.txt", type=str)
        parser.add_argument("--cache_path", default="", type=str)
        parser.add_argument("--uname", default="", type=str)
        parser.add_argument("--upass", default="", type=str)
        parser.add_argument("--in_html", default="", type=str)
        parser.add_argument("--out_html", default="", type=str)
        self._parser = parser
        self._args = parser.parse_args()

    def __getitem__(self, item:str):
        return getattr(self._args, item)




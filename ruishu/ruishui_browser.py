#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from PySide6.QtNetwork import QNetworkCookie

from webengine.browser import Browser
from ruishu.util import download

class RuiShuiBrowser(Browser):

    def __init__(self, *args, **kwargs):
        super(RuiShuiBrowser, self).__init__(*args, **kwargs)
        self._web_page.signalFinished.connect(self.on_load_finished)
        self._cookie_dict = dict()
        self.scripts: list[str] = []

    # slots
    def on_load_finished(self, url):
        logging.info("load finished")
        for script in self.scripts:
            self._web_page.runJavaScript(script)
        host_name = "sugh.szu.edu.cn"
        cookies = self.get_network_cookies(host_name)
        logging.info(f"page data: url={url}, cookies= {cookies}")
        self.download_page(url, cookies)

    def download_page(self, url, cookies:list[QNetworkCookie]):
        cookie = {cookie.name().toStdString(): cookie.value().toStdString() for cookie in cookies}
        logging.info(f"download page with cookies: {cookie}")
        cookie.update(self._cookie_dict)
        response = download(url, cookies=cookie)
        open("ruishu.html", "wb").write(response.content)

    def add_cookie(self, name:str, value:str, path="/", domain=None, secure=False, http_only=False, maxage=None):
        self._cookie_dict[name] = value
        super(RuiShuiBrowser, self).add_cookie(name, value, path, domain, secure, http_only, maxage)


if __name__ == '__main__':
    pass

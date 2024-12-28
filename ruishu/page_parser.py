#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from copyreg import constructor

import requests
from bs4 import BeautifulSoup


class PageParser:

    def __init__(self, html:str, url:str):
        self.html = html
        self.url = url
        self.base_content = ""
        self.scripts: list[str] = list()

    def parse(self,):
        soup = BeautifulSoup(self.html, "html.parser")
        metas = soup.select("meta[content]")
        meta_data = ''
        for meta in metas:
            if len(meta['content']) > 1024:
                meta_data = '''var content="%s"; ''' % meta['content']
                break

        self.scripts.append(meta_data)
        script_elements = soup.select("script")
        for script in script_elements:
            if script.has_attr("src"):
                content = self._download_js_data(script.get("src"), script.get("charset"))
            else:
                content = script.text
            self.scripts.append(content)
        return self.scripts

    def _download_js_data(self, url:str, charset:str):
        full_url = self.url + url
        response = requests.get(full_url)
        content = response.content.decode(charset)
        return content


if __name__ == '__main__':
    pass

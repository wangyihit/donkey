#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import sys
import threading
import time

from PySide6.QtWidgets import QApplication
from idna.idnadata import scripts

from ruishu.page_parser import PageParser
from ruishu.ruishui_browser import RuiShuiBrowser
from ruishu.util import download
from common.settings import Settings
from ruishu.worker import RuiShuiWorker
from common.logger import init_log


def _load_page(url:str, html:str):
    pass

def worker_func(worker:RuiShuiWorker):
    while True:
        # logging.info(f"worker thread {threading.get_ident()} running")
        time.sleep(5)

def _main():
    app = QApplication(sys.argv)
    init_log(console_log=True, file_log=False)
    url = "https://sugh.szu.edu.cn/"
    resp = download(url, {})
    cookies = resp.cookies.get_dict("sugh.szu.edu.cn")
    html = resp.content.decode('utf-8')
    page_parser = PageParser(html, url)
    js_scripts = page_parser.parse()

    settings = Settings()

    browser = RuiShuiBrowser(settings)
    browser.scripts = js_scripts
    for k, v in cookies.items():
        browser.add_cookie(name=k, value=v, path="/", domain="sugh.szu.edu.cn", secure=True, http_only=True,)
    current_cookies = browser.get_network_cookies()
    logging.info(f"current cookies: {current_cookies}")
    # browser.load_html(html='''<html></html>''', url=url)
    browser.load_url(url)
    worker = RuiShuiWorker()
    worker.connect_browser(browser)
    t = threading.Thread(target=worker_func, args=(worker,))
    t.start()
    app.exec()


if __name__ == '__main__':
    _main()

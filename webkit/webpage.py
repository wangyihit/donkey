#!/usr/bin/env python
# encoding=utf-8

from PyQt5.QtWebKitWidgets import QWebPage, QWebFrame
from cookiejar import CookieJar
from jslib import js_lib


class QQMailLoginStatus(object):
    LOGIN_WITH_USER_INFO = 0
    INPUT_VERIFY_CODE = 1


class WebPage(QWebPage):

    def __init__(self, settings):
        super(WebPage, self).__init__()
        self._settings = settings
        self.loadFinished.connect(self._on_load_finished)
        # set cookie_jar in network_access_manager
        # self.cookie_jar = CookieJar()
        # self.networkAccessManager().setCookieJar(self.cookie_jar)
        self.qq_login_status = QQMailLoginStatus.LOGIN_WITH_USER_INFO

    def set_cookies(self, cookies):
        cookie = ""

    def get_frame_by_name(self, frame_name):
        frames = self.mainFrame().childFrames()
        for f in frames:
            if f.frameName() == frame_name:
                return f
        return None

    def _login_with_user_info(self, login_frame):
        login_frame.evaluateJavaScript(js_lib)
        js_cmd = "bot.loginQQMail('%s', '%s')" % (
            self._settings["uname"],
            self._settings["upass"],
        )
        login_frame.evaluateJavaScript(js_cmd)

    def _on_load_finished(self, ok):
        if self._settings["in_html"]:
            return
        qq_mail_login_frame_name = "login_frame"
        login_frame = self.get_frame_by_name(qq_mail_login_frame_name)
        if login_frame is None:
            print "Get login frame failed"
            return -1

        if self.qq_login_status == QQMailLoginStatus.LOGIN_WITH_USER_INFO:
            self._login_with_user_info(login_frame)
            self.qq_login_status = QQMailLoginStatus.INPUT_VERIFY_CODE
        out_html_path = self._settings["out_html"]
        if out_html_path:
            with open(out_html_path, "w") as f:
                html = self.mainFrame().toHtml()
                f.write(html)
        out_cookies_path = self._settings["out_cookies"]
        if out_cookies_path:
            cookies_data = self.cookie_jar.to_qt_cookies()
            with open(out_cookies_path, "w") as f:
                f.write(cookies_data)

    def userAgentForUrl(self, url):
        android_ua = "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Mobile Safari/537.36"
        return android_ua

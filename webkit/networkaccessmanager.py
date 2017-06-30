#!/usr/bin/env python
# encoding=utf-8
from app import g_app
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest


class NetworkAccessManager(QNetworkAccessManager):
    QQ_CODE_VERIFY_URL = "https://ssl.captcha.qq.com/cap_union_new_verify"

    def __init__(self, cookie_jar):
        super(NetworkAccessManager, self).__init__()
        self.cookie_jar = cookie_jar
        self.setCookieJar(self.cookie_jar)

    def get_headers(self, req):
        headers = req.rawHeaderList()
        res = ""
        for h in headers:
            res = " %s -H '%s:%s' " % (res, h, req.rawHeader(h))
        return res

    # def createRequest(self, QNetworkAccessManager_Operation, QNetworkRequest, QIODevice_device=None):
    def createRequest(self, op, req, io_device=None):


        url = req.url().toString()
        if url.find("sId") > 0:
            with open("sid", "w") as f:
                f.write(url)
        if not (op == QNetworkAccessManager.PostOperation and url == self.QQ_CODE_VERIFY_URL):
            return super(NetworkAccessManager, self).createRequest(op, req, io_device)
        return super(NetworkAccessManager, self).createRequest(op, req, io_device)
        print "req, url=%s" % url
        cookies = self.cookie_jar.to_curl_cookies()
        with open("verify_code.cookies", "w") as f:
            f.write(cookies)
        data = io_device.readAll()
        with open("post_data", "w") as f:
            f.write(data)

        with open("http_header", "w") as f:
            f.write(self.get_headers(req))
        # g_app.app.exit(0)

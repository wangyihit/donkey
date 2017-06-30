#!/usr/bin/env python
# encoding=utf-8
from PyQt5.QtCore import QByteArray
from PyQt5.QtNetwork import QNetworkCookie, QNetworkCookieJar
'''
cookie file format

# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This file was generated by libcurl! Edit at your own risk.
 
www.example.com        FALSE        /        FALSE        1338534278        cookiename        value
The first few lines are comments and can therefore be ignored. The cookie data consists of the following items (in the order they appear in the file.

domain - The domain that created and that can read the variable.
flag - A TRUE/FALSE value indicating if all machines within a given domain can access the variable. This value is set automatically by the browser, depending on the value you set for domain.
path - The path within the domain that the variable is valid for.
secure - A TRUE/FALSE value indicating if a secure connection with the domain is needed to access the variable.
expiration - The UNIX time that the variable will expire on.
name - The name of the variable.
value - The value of the variable.


'''


class CookieJar(QNetworkCookieJar):

    def __init__(self):
        super(CookieJar, self).__init__()

    def to_curl_cookies(self):
        cookies = self.allCookies()
        # domain flag path secure expiration name value
        cookie_data = []
        for cookie in cookies:
            data = "%s %s %s %s %s %s %s" % (
                    cookie.domain(),
                    True,
                    cookie.path(),
                    cookie.isSecure(),
                    cookie.expirationDate().toTime_t(),
                    cookie.name(),
                    cookie.value(),
                )
            cookie_data.append(data)
        return "\n".join(cookie_data)

    def to_qt_cookies(self):
        cookies = self.allCookies()
        data = []
        for cookie in cookies:
            data.append(str(cookie.toRawForm()))
        return "\n".join(data)

    def load_qt_cookie(self, cookie_data):
        b = QByteArray()
        cookies = QNetworkCookie.parseCookies(b.append(cookie_data))
        self.setAllCookies(cookies)

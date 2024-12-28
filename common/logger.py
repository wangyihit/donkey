#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.handlers
import os
import socket
from datetime import datetime
from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):

    def __init__(self, f='%(timestamp)s %(level)s %(name)s %(message)s'):
        super(CustomJsonFormatter, self).__init__(f)

    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname
        log_record["file"] = record.filename
        log_record["line"] = record.lineno
        log_record["func"] = record.funcName


def _common_info():
    return "pid=%s, server=%s" % (os.getpid(), socket.gethostname())


def init_console_log():
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s, " + _common_info())
    console.setFormatter(formatter)
    log = logging.getLogger("")
    log.addHandler(console)
    log.setLevel(logging.INFO)
    log.info("console log init success")


def init_file_log(file_path):
    handler = logging.handlers.RotatingFileHandler(file_path, maxBytes=1024 * 1024 * 1024, backupCount=7)
    formatter = CustomJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger("")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info("file log init success", extra=dict(info=dict(file_path=file_path)))


def init_es_log(host, port, sender):
    h = logging.handlers.SysLogHandler(address=(host, port))
    h.setLevel(logging.INFO)
    template = "%(asctime)s %(filename)s[line:%(lineno)d], %(levelname)s ,%(message)s, " + _common_info()
    if sender != "":
        template += ", sender=%s" % sender
    formatter = logging.Formatter(template)
    h.setFormatter(formatter)
    log = logging.getLogger("")
    log.addHandler(h)
    log.info("es log init success")


def init_log(console_log=True, file_log=True, log_path="", file_name="", host="", port=0, sender=""):
    if console_log is True:
        init_console_log()
    if file_log is True:
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        init_file_log(os.path.join(log_path, file_name))
    if host and port:
        init_es_log(host, port, sender)



if __name__ == '__main__':
    pass


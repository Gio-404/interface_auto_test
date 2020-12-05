#!usr/bin/env python3
# coding:utf-8
# Create Date:2019/5/16


import logging
import datetime
from logging import handlers
import os


if not os.path.exists("log"):
    os.mkdir("log")


def mylogger():
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        rf_handler = handlers.TimedRotatingFileHandler("log/all.log", when='midnight', interval=1, backupCount=7,
                                                       atTime=datetime.time(0, 0, 0, 0))
        rf_handler.setFormatter(logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"))
        f_handler = logging.FileHandler("log/error.log")
        f_handler.setLevel(logging.ERROR)
        f_handler.setFormatter(logging.Formatter(
            "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
        logger.addHandler(rf_handler)
        logger.addHandler(f_handler)
    return logger

#!usr/bin/env python3
# coding:utf-8
# Create Date:2019/5/21


import requests
import mylogger
from common import register_login


class RequestMethod(object):
    def __init__(self, url, params):
        self.url = url
        self.params = params
        self.mylog = mylogger.mylogger()

    # get方法，不登录
    def get_method(self):
        resp = requests.get(self.url, params=self.params)
        if resp.status_code == 200:
            self.mylog.info("Request Content: %s" % self.params)
            self.mylog.info("Response code:%s Response content:%s" %
                            (resp.status_code, resp.json()))
            return resp.json()
        else:
            self.mylog.info(resp.status_code)

    # post方法，不登录
    def post_method(self):
        resp = requests.post(self.url, params=self.params)
        if resp.status_code == 200:
            self.mylog.info("Request Content: %s" % self.params)
            self.mylog.info("Response code:%s Response content:%s" %
                            (resp.status_code, resp.json()))
            return resp.json()
        else:
            self.mylog.info(resp.status_code)

    # get方法，登录
    def login_get_method(self, username, password):
        login = register_login.Account(username, password)
        resp = requests.get(self.url, params=self.params,
                            cookies=login.get_session())
        if resp.status_code == 200:
            self.mylog.info("Request Content: %s" % self.params)
            self.mylog.info("Response code:%s Response content:%s" %
                            (resp.status_code, resp.json()))
            return resp.json()
        else:
            self.mylog.info(resp.status_code)

    # post方法，不登录
    def login_post_method(self, username, password):
        login = register_login.Account(username, password)
        resp = requests.post(self.url, params=self.params,
                             cookies=login.get_session())
        if resp.status_code == 200:
            self.mylog.info("Request Content: %s" % self.params)
            self.mylog.info("Response code:%s Response content:%s" %
                            (resp.status_code, resp.json()))
            return resp.json()
        else:
            self.mylog.info(resp.status_code)

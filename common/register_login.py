#!usr/bin/env python3
# coding:utf-8
# Create Date:2019/5/16

import requests
from common import create_data
import json
import mylogger
import readconf


class Account(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.config = readconf.ReadConfig()
        self.passport_url = self.config.get_conf("passport_url")
        self.channel = "aostest"
        self.sign = create_data.create_sign(
            self.channel, self.username, self.password)
        self.mylog = mylogger.mylogger()

    # 注册账号
    def reg_account(self):
        params = {'username': self.username, 'password': self.password,
                  'channel': self.channel, 'sign': self.sign}
        resp = requests.post(self.passport_url +
                             "/ws/pp/account/register", data=params)
        resp_content = json.loads(resp.text)
        return resp_content["code"]

    # 登录
    def login_account(self):
        keep_session = requests.session()
        params = {'userid': self.username, 'password': self.password,
                  'channel': self.channel, 'sign': self.sign}
        resp = keep_session.post(
            self.passport_url + "/ws/pp/account/login/", data=params)
        resp_content = json.loads(resp.text)
        if resp_content["code"] == 1:
            return resp.cookies.get_dict()   # 返回登录后的cookie
        else:
            self.mylog.info("登录失败！code：%s" % (resp_content["code"]))

    # 判断账号是否已经注册过
    def get_session(self):
        reg_code = self.reg_account()
        if reg_code == 1 or reg_code == 10023:
            return self.login_account()
        else:
            self.mylog.info("Register Failed, Code:%s" % reg_code)

#!usr/bin/env python3
# coding:utf-8
# Create Date:2019/6/13

import random
import hashlib
import readconf


# 创建tid
def create_tid(num):
    string1 = [chr(i) for i in range(ord("A"), ord("Z")+1)]
    tid = ''.join(random.sample(string1, num))
    return tid


# 创建签名
def create_sign(*args):
    get_salt = readconf.ReadConfig()
    salt = get_salt.get_salt("sign_salt").encode('ascii')
    content = ''.join(args).encode('ascii')
    m = hashlib.md5(content+salt).hexdigest().upper()
    return m.upper()


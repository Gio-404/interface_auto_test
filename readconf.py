#!usr/bin/env python3
# coding:utf-8
# Create Date:2019/6/12

import configparser
import os


base_path = os.path.split(os.path.realpath(__file__))[0]
file_path = os.path.join(base_path, "config.ini")


class ReadConfig(object):
    def __init__(self):
        self.cp = configparser.ConfigParser()
        self.cp.read(file_path)
    
    '''获取环境'''
    def get_conf(self, name):
        value = self.cp.get("ENV", name)
        return value

    '''获取salt'''
    def get_salt(self, name):
        value = self.cp.get("SALT", name)
        return value

#!usr/bin/env python3
# coding:utf-8
# Create Date:2019/5/16


import unittest
import os
import time
from common import HTMLTestRunner

case_path = './testcase/'
report_path = os.path.join(os.getcwd(), 'report')


def get_allcase():
    discover = unittest.defaultTestLoader.discover(
        case_path, pattern="test*.py")
    suite = unittest.TestSuite()
    suite.addTests(discover)
    return suite


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_abspath = os.path.join(report_path, "result_"+now+".html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp, title=u'接口自动化测试报告，测试结果如下：', description=u'用例执行情况')
    runner.run(get_allcase())
    fp.close()

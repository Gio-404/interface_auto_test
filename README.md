# interface_auto_test

#### 介绍
接口自动化测试框架

#### 软件架构
软件架构说明
common  --存放公用模块
|__create_data.py  --创建基础参数
|__HTMLTestRunner.py  --生成测试报告
|__register_login.py  --注册登录方法
|__request_method.py  --请求方法
report  --存放测试报告
testcase  --存放测试用例
config.ini  --环境配置文件
mylogger.py --日志模块
readconf.py  --读取配置文件
runcase.py --运行所有case


#### 使用说明

1. 在testcase文件下编写测试用例
2. 运行runcase执行用例

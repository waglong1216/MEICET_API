#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/10/9 22:03
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
import os
import unittest
from libs.HTMLTestRunnerNew import HTMLTestRunner

from datetime import datetime

from setting.constant import p_path

# 初始化 suite
suite = unittest.TestSuite()
# 初始化 loader 加载器
loader = unittest.TestLoader()

# discover 自动发现测试，
suite = loader.discover(p_path.CASE_PATH)

# REPORT_PATH + 时间戳字符串 + 后缀名 .html
report_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
report_file = os.path.join(p_path.REPORT_PATH, report_name+'.html')

if __name__ == '__main__':
    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner(f)
        runner.run(suite)

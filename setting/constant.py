#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/10/9 21:20
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
import os

class BasePath:
    pass


class ProjectPath(BasePath):
    # 项目路径
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 测试用例数据的路径
    DATA_PATH = os.path.join(ROOT_PATH, 'data')
    # 配置文件路径
    CONFIG_PATH = os.path.join(ROOT_PATH, 'setting')
    # 测试用例方法路径
    CASE_PATH = os.path.join(ROOT_PATH, 'test_case')
    # 测试报告路径
    REPORT_PATH = os.path.join(ROOT_PATH, 'report')
    # 如果没有改文件夹，自动创建
    if not os.path.exists(REPORT_PATH):
        os.mkdir(REPORT_PATH)

class SubPath(ProjectPath):
    pass


p_path = ProjectPath()


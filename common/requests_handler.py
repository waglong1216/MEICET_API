#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/10/16 20:06
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
import logging

import requests


class RequestsHandler:

    def get(self, url, params=None, **kw):
        """发送get请求"""
        # http://:baidu
        try:
            res = requests.get(url, params=params, **kw)
        except Exception as e:
            # 记录日志信息
            logging.error("访问不成功")
        else:
            return res

    def post(self, url, data=None, json=None, **kw):
        """发送 post 请求"""
        try:
            res = requests.post(url, data=data, json=json, **kw)
        except Exception as e:
            # 记录日志信息
            logging.error("访问不成功")
        else:
            return res

    def visit(self, method, url, params=None, data=None, json=None, **kw):
        """访问接口"""
        if method.lower() == 'get':
            res = self.get(url, params=params, **kw)
            return res
        elif method.lower() == 'post':
            return self.post(url, data=data, json=json, params=params, **kw)
        else:
            # requests 通用的访问方式
            return requests.request(method, url, params=params, data=data, json=json, **kw)

    def json(self, method, url, params=None, data=None, json=None, **kw):
        """访问接口，获取 json 数据"""
        res = self.visit(method, url, params=params, data=data, json=json, **kw)
        # 获取json 数据
        try:
            return res.json()
        except:
            # 记录日志信息
            logging.error("不是 json 格式的数据")


class RequestsCookieHandler:

    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, **kw):
        """发送get请求"""
        # http://:baidu
        try:
            res = self.session.get(url, params=params, **kw)
        except Exception as e:
            # 记录日志信息
            logging.error("访问不成功")
        else:
            return res

    def post(self, url, data=None, json=None, **kw):
        """发送 post 请求"""
        try:
            res = self.session.post(url, data=data, json=json, **kw)
        except Exception as e:
            # 记录日志信息
            logging.error("访问不成功")
        else:
            return res

    def visit(self, method, url, params=None, data=None, json=None, **kw):
        """访问接口"""
        if method.lower() == 'get':
            res = self.get(url, params=params, **kw)
            return res
        elif method.lower() == 'post':
            return self.post(url, data=data, json=json, params=params, **kw)
        else:
            # requests 通用的访问方式
            return self.session.request(method, url, **kw)

    def json(self, method, url, params=None, data=None, json=None, **kw):
        """访问接口，获取 json 数据"""
        res = self.visit(method, url, params=params, data=data, json=json, **kw)
        # 获取json 数据
        try:
            return res.json()
        except:
            # 记录日志信息
            logging.error("不是 json 格式的数据")
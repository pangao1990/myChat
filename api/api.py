#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: 潘高
LastEditors: 潘高
Date: 2022-03-21 17:01:39
LastEditTime: 2023-03-31 21:01:05
Description: 本地API，供前端JS调用
usage: 调用window.pywebview.api.<methodname>(<parameters>)从Javascript执行
'''

from api.chat import Chat
from api.storage import Storage
from api.system import System


class API(System, Storage, Chat):
    '''本地API，供前端JS调用'''

    def setWindow(self, window):
        '''获取窗口实例'''
        System.window = window

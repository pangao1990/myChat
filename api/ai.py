#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: 潘高
LastEditors: 潘高
Date: 2023-03-10 14:07:59
LastEditTime: 2023-04-17 14:57:09
Description: 调用OpenAI接口
'''

import os

import openai
import tiktoken

from api.db.orm import ORM
from api.utils.getProxy import GetProxy


class AI:
    '''ai'''

    skOpenAI = ''
    model = ''    # gpt-4(8192)  gpt-4-32k(32768)  gpt-3.5-turbo(4096)  text-davinci-003(4097)
    temperature = ''    # 默认为1，取值在0-2之间。像1.8这样的高值将使输出更加随机，而像0.2这样的低值将使其更加集中和确定性。

    def getChat(self, messages):

        # 如果手动设置了代理IP和端口，则启用手动设置代理信息
        orm = ORM()    # 操作数据库类
        proxyIP = orm.getStorageVar('proxyIP')
        proxyPort = orm.getStorageVar('proxyPort')
        if proxyIP != '' and proxyPort != '':
            # 代理
            os.environ["HTTP_PROXY"] = f'http://{proxyIP}:{proxyPort}'
            os.environ["HTTPS_PROXY"] = f'http://{proxyIP}:{proxyPort}'
        else:
            # 自动获取代理IP和端口
            proxy = GetProxy().run()
            if 'http' in proxy:
                # 代理
                proxyHTTP = proxy['http']
                if proxyHTTP[:7] == 'http://':
                    os.environ["HTTP_PROXY"] = proxyHTTP
                    os.environ["HTTPS_PROXY"] = proxyHTTP
                else:
                    os.environ["HTTP_PROXY"] = f'http://{proxyHTTP}'
                    os.environ["HTTPS_PROXY"] = f'http://{proxyHTTP}'

        '''获取AI返回信息'''
        openai.api_key = AI.skOpenAI
        # 访问OpenAI接口
        response = openai.ChatCompletion.create(model=AI.model, temperature=AI.temperature, messages=messages, request_timeout=(10, 290))
        '''
        {
            "id":"chatcmpl-abc123",
            "object":"chat.completion",
            "created":1677858242,
            "model":"gpt-3.5-turbo-0301",
            "usage":{
                "prompt_tokens":13,
                "completion_tokens":7,
                "total_tokens":20
            },
            "choices":[{
                "message":{
                "role":"assistant",
                "content":"\n\nThis is a test!"
                },
                "finish_reason":"stop",
                "index":0
            }]
        }
        '''
        resText = response.choices[0].message.content
        # print('proxy', proxy, proxy != '', resText)
        return resText

    def getModelList(self):
        '''获取模型列表'''
        openai.api_key = AI.skOpenAI
        modelList = openai.Model.list()
        return modelList

    def getTokenCount(self, msg):
        '''计算消息的令牌个数'''
        try:
            encoding = tiktoken.encoding_for_model(AI.model)
        except KeyError:
            encoding = tiktoken.get_encoding("p50k_base")
        tokenCount = len(encoding.encode(msg))
        return tokenCount

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: 潘高
LastEditors: 潘高
Date: 2023-03-25 19:39:03
LastEditTime: 2023-04-07 08:54:49
Description: 聊天相关
usage: 调用window.pywebview.api.<methodname>(<parameters>)从Javascript执行
'''

from api.ai import AI
from api.db.orm import ORM


class Chat:
    '''聊天相关类'''

    modelList = [{'name': 'gpt-4', 'info': 'GPT-4是一个大型多模态模型，由于其更广泛的基础知识和先进的推理能力，使得它能够执行更复杂的任务，并针对聊天应用进行了优化。最大Tokens值为8192。'},
                {'name': 'gpt-4-32k', 'info': '与GPT-4模型的功能相同，但上下文长度是4倍。最大Tokens值为32768。'},
                {'name': 'gpt-3.5-turbo', 'info': 'GPT-3.5模型可以理解和生成自然语言或代码。而gpt-3.5-turbo是最强大的GPT-3.5型号，以text-davinci-003成本的十分之一优化聊天。最大Tokens值为4096。'},
                {'name': 'text-davinci-003', 'info': '在GPT-3模型中，功能最全面、能力最强的模型。最大Tokens值为2049。'}]

    orm = ORM()    # 操作数据库类

    def chat_addTitle(self, title, theme, model, temperature, news_count):
        '''设置聊天类别'''
        self.orm.setChatTitle(title, theme, model, temperature, news_count)

    def chat_getTitleList(self):
        '''获取聊天类别'''
        res = self.orm.getChatTitleList()
        return res

    def chat_getTitleInfo(self, title):
        '''获取聊天标题信息'''
        res = self.orm.getChatTitleInfo(title)
        return res

    def chat_clearContent(self, title):
        '''清空聊天消息'''
        return self.orm.clearChatTitle(title)

    def chat_deleteTitle(self, title):
        '''删除聊天主题'''
        self.orm.deleteChatTitle(title)

    def chat_updateTitle(self, title, info):
        '''更新聊天主题'''
        self.orm.updateChatTitle(title, info)

    def chat_addContent(self, title, who, content):
        '''新增聊天内容'''
        self.orm.updateChatTitle(title, {'title': title})    # 更新一下title的update_at日期
        return self.orm.addChatContent(title, who, content)

    def chat_getContentList(self, title, page, size):
        '''获取聊天内容'''
        return self.orm.getChatContentList(title, page, size)

    def chat_getSkOpenAI(self):
        '''获取skOpenAI'''
        return self.orm.getStorageVar('skOpenAI')

    def chat_setSkOpenAI(self, skOpenAI):
        '''设置skOpenAI'''
        AI.skOpenAI = skOpenAI
        self.orm.setStorageVar('skOpenAI', skOpenAI)

    def chat_setModel(self, model):
        '''设置模型'''
        AI.model = model

    def chat_setTemperature(self, temperature):
        '''设置temperature'''
        AI.temperature = temperature

    def chat_getModelList(self):
        '''获取模型列表'''
        return self.modelList

    def chat_getAI(self, title, prompt):
        '''获取AI返回信息'''
        # 获取配置信息
        resTitleInfo = self.chat_getTitleInfo(title)
        self.chat_setModel(resTitleInfo['model'])    # 模型
        self.chat_setTemperature(resTitleInfo['temperature'])    # 温度
        theme = resTitleInfo['theme']    # 主题
        news_count = resTitleInfo['news_count']    # 记忆消息个数
        resContentList = self.chat_getContentList(title, 0, news_count)    # 记忆消息内容

        # 组装记忆消息
        messages = list()
        chatDict = dict()
        chatDict['role'] = 'system'
        chatDict['content'] = theme
        messages.append(chatDict)
        for rcl in resContentList['list']:
            chatDict = dict()
            role = rcl['who']
            if role == 'ai':
                role = 'assistant'
            else:
                role = 'user'
            chatDict['role'] = role
            chatDict['content'] = rcl['content']
            messages.append(chatDict)
        # 新的提问
        chatDict = dict()
        chatDict['role'] = 'user'
        chatDict['content'] = prompt
        messages.append(chatDict)

        try:
            resAI = AI().getChat(messages)
            # print('resAI', resAI)
            return resAI
        except Exception as e:
            print('Error => ', e)
            return 'Error => ' + str(e)

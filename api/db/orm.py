#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: 潘高
LastEditors: 潘高
Date: 2023-03-12 20:08:30
LastEditTime: 2023-04-03 10:09:25
Description: 操作数据库类
usage:
    from api.db.orm import ORM

    orm = ORM()    # 操作数据库类
    author = self.orm.getStorageVar('author')    # 获取储存变量
    print('author', author)
'''

from sqlalchemy import delete, insert, select, update, func

from api.db.models import Chat, StorageVar, Title
from pyapp.db.db import DB


class ORM:
    '''操作数据库类'''

    def getStorageVar(self, key):
        '''获取储存变量'''
        resVal = ''
        dbSession = DB.session()
        with dbSession.begin():
            stmt = select(StorageVar.value).where(StorageVar.key == key)
            result = dbSession.execute(stmt)
            result = result.one_or_none()
            if result is None:
                # 新建
                stmt = insert(StorageVar).values(key=key)
                dbSession.execute(stmt)
            else:
                resVal = result[0]
        dbSession.close()
        return resVal

    def setStorageVar(self, key, val):
        '''更新储存变量'''
        dbSession = DB.session()
        with dbSession.begin():
            stmt = update(StorageVar).where(StorageVar.key == key).values(value=val)
            dbSession.execute(stmt)
        dbSession.close()

    def getChatTitleList(self):
        '''获取聊天类别'''
        resList = list()
        dbSession = DB.session()
        with dbSession.begin():
            stmt = select(Title).distinct()
            result = dbSession.execute(stmt)
            result = result.all()
            resList = [res[0].toDict() for res in result]
        dbSession.close()
        return resList

    def getChatTitleInfo(self, title):
        '''获取聊天标题信息'''
        resDict = dict()
        dbSession = DB.session()
        with dbSession.begin():
            stmt = select(Title).where(Title.title == title)
            result = dbSession.execute(stmt)
            result = result.all()
            if len(result) > 0:
                resDict = result[0][0].toDict()
        dbSession.close()
        return resDict

    def setChatTitle(self, title, theme, model, temperature, news_count):
        '''设置聊天类别'''
        dbSession = DB.session()
        with dbSession.begin():
            print(title, theme, model, temperature, news_count)
            stmt = insert(Title).values(title=title, theme=theme, model=model, temperature=temperature, news_count=news_count)
            dbSession.execute(stmt)
        dbSession.close()

    def getChatContentList(self, title, page, size):
        '''获取聊天内容'''
        total = 0
        resList = list()
        dbSession = DB.session()
        with dbSession.begin():
            # 获取总数
            stmt = select(func.count(Chat.id)).where(Chat.title == title)
            result = dbSession.execute(stmt)
            result = result.one_or_none()
            if result is not None:
                total = result[0]
                # 获取列表
                start = total-page*size
                if start < 0:
                    start = 0
                stmt = select(Chat).where(Chat.title == title).order_by(Chat.id).offset(start).limit(size)
                result = dbSession.execute(stmt)
                result = result.all()
                resList = [res[0].toDict() for res in result]
        dbSession.close()
        return {'list': resList, 'total': total}

    def deleteChatTitle(self, title):
        '''删除聊天主题'''
        dbSession = DB.session()
        with dbSession.begin():
            stmt = delete(Title).where(Title.title == title)
            dbSession.execute(stmt)
            stmt = delete(Chat).where(Chat.title == title)
            dbSession.execute(stmt)
        dbSession.close()

    def updateChatTitle(self, title, info):
        '''更新聊天主题'''
        dbSession = DB.session()
        with dbSession.begin():
            stmt = update(Title).where(Title.title == title).values(**info)
            dbSession.execute(stmt)
        dbSession.close()

    def clearChatTitle(self, title):
        '''清空聊天消息'''
        dbSession = DB.session()
        with dbSession.begin():
            stmt = delete(Chat).where(Chat.title == title)
            dbSession.execute(stmt)
        dbSession.close()

    def addChatContent(self, title, who, content):
        '''新增聊天内容'''
        dbSession = DB.session()
        with dbSession.begin():
            stmt = insert(Chat).values(title=title, who=who, content=content)
            dbSession.execute(stmt)
        dbSession.close()

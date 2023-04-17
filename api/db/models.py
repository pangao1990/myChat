#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
FilePath: /myChat/api/db/models.py
Author: 潘高
LastEditors: 潘高
Date: 2023-03-12 20:29:49
LastEditTime: 2023-04-03 10:35:20
Description: 创建数据表
usage: 更新数据表格式后，请按如下操作迁移数据库：
        m=备注更改内容 npm run alembic

        注意：上述命令仅能迁移打包程序自带数据库(Config.staticDir)。在程序运行初始化时，会自动检测并迁移本地电脑中保存的数据库(Config.storageDir)
'''

import json

from sqlalchemy import DateTime, Numeric, Column, Integer, String, Float, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel(Base):
    '''基类'''
    __abstract__ = True

    def _gen_tuple(self):
        # 处理 日期 等无法正常序列化的对象
        def convert_datetime(value):
            if value:
                return value.strftime("%Y-%m-%d %H:%M:%S")
            else:
                return ""
        for col in self.__table__.columns:
            try:
                if isinstance(col.type, DateTime):
                    value = convert_datetime(getattr(self, col.name))
                elif isinstance(col.type, Numeric):
                    value = float(getattr(self, col.name))
                else:
                    value = getattr(self, col.name)
                yield (col.name, value)
            except Exception as e:
                print(e)
                pass

    def toDict(self):
        # 转化为 字典
        return dict(self._gen_tuple())

    def toJson(self):
        # 序列化为 JSON
        return json.dumps(self.toDict())


class StorageVar(BaseModel):
    '''储存变量'''
    __tablename__ = "storage_var"
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(), doc='键', comment='键', server_default='', nullable=False, index=True)
    value = Column(String(), doc='值', comment='值', server_default='', nullable=False)
    remark = Column(String(), doc='备注', comment='备注', server_default='', nullable=False)
    created_at = Column(DateTime(), doc='创建时间', comment='创建时间', server_default=text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"))
    updated_at = Column(DateTime(), doc='更新时间', comment='更新时间', server_default=text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"), onupdate=text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"))

    def __str__(self):
        return self.key + ' => ' + self.value


class Title(BaseModel):
    '''标题列表'''
    __tablename__ = "title"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(), doc='标题', comment='标题', server_default='', nullable=False, index=True)
    theme = Column(String(), doc='主题', comment='主题', server_default='', nullable=False)
    model = Column(String(), doc='模型', comment='模型', server_default='gpt-3.5-turbo', nullable=False)
    temperature = Column(Float(), doc='温度参数', comment='温度参数', server_default='1.0', nullable=False)
    news_count = Column(Integer, doc='记忆消息个数', comment='记忆消息个数', server_default='0', nullable=False)
    created_at = Column(DateTime(), doc='创建时间', comment='创建时间', server_default=text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"))
    updated_at = Column(DateTime(), doc='更新时间', comment='更新时间', server_default=text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"), onupdate=text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"))

    def __str__(self):
        return self.id + ' => ' + self.title


class Chat(BaseModel):
    '''聊天信息'''
    __tablename__ = "chat"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Integer, doc='标题', comment='标题', server_default='', nullable=False, index=True)
    who = Column(String(), doc='所属人', comment='所属人', server_default='', nullable=False)
    content = Column(String(), doc='内容', comment='内容', server_default='', nullable=False)
    created_at = Column(DateTime(), doc='创建时间', comment='创建时间', server_default=text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"))
    updated_at = Column(DateTime(), doc='更新时间', comment='更新时间', server_default=text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"), onupdate=text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"))

    def __str__(self):
        return self.title + ' => ' + self.who + ' => ' + self.content

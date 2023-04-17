#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
FilePath: /myChat/api/utils/getProxy.py
Author: 潘高
LastEditors: 潘高
Date: 2023-03-31 15:32:03
LastEditTime: 2023-04-07 08:37:51
Description: 获取代理信息
usage: 运行前，请确保本机已经搭建Python3开发环境，且已经安装 PyPAC 模块。
'''

import os
import re
import sys

import pypac


class GetProxy:
    '''获取代理信息'''

    def run(self):
        proxies = {}
        if sys.platform == 'darwin':
            proxies = self.getFromEnvironment() or self.getFromPac()
        else:
            proxies = self.getFromEnvironment() or self.getFromRegistry() or self.getFromPac()
        return proxies

    def getFromEnvironment(self):
        '''从环境变量中提取代理希信息'''
        proxies = {}
        for name, value in os.environ.items():
            name = name.lower()
            if value and name[-6:] == '_proxy':
                proxies[name[:-6]] = value
        if 'REQUEST_METHOD' in os.environ:
            proxies.pop('http', None)
        for name, value in os.environ.items():
            if name[-6:] == '_proxy':
                name = name.lower()
                if value:
                    proxies[name[:-6]] = value
                else:
                    proxies.pop(name[:-6], None)
        return proxies

    def getFromPac(self):
        '''从pac文件中获取代理信息'''
        if 'HTTP_PROXY' in os.environ:
            del os.environ["HTTP_PROXY"]
        if 'HTTPS_PROXY' in os.environ:
            del os.environ["HTTPS_PROXY"]
        proxies = {}
        pacFile = pypac.get_pac(from_dns=False)
        if pacFile is not None:
            proxy = pacFile.find_proxy_for_url('https://api.openai.com', 'openai.com')
            proxy = proxy.replace(' ', '')
            proxyList = proxy.split(';')
            for proxyL in proxyList:
                if proxyL.find('PROXY') == 0 or proxyL.find('proxy') == 0:
                    proxies['http'] = proxyL.replace('PROXY', '').replace('proxy', '')
                    break
        return proxies

    def getFromRegistry(self):
        """从注册表获取代理信息"""
        proxies = {}
        try:
            import winreg
        except ImportError:
            return proxies
        try:
            internetSettings = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings')
            proxyEnable = winreg.QueryValueEx(internetSettings, 'ProxyEnable')[0]
            if proxyEnable:
                proxyServer = str(winreg.QueryValueEx(internetSettings, 'ProxyServer')[0])
                if '=' not in proxyServer and ';' not in proxyServer:
                    proxyServer = 'http={0};https={0};ftp={0}'.format(proxyServer)
                for p in proxyServer.split(';'):
                    protocol, address = p.split('=', 1)
                    if not re.match('(?:[^/:]+)://', address):
                        if protocol in ('http', 'https', 'ftp'):
                            address = 'http://' + address
                        elif protocol == 'socks':
                            address = 'socks://' + address
                    proxies[protocol] = address
                if proxies.get('socks'):
                    address = re.sub(r'^socks://', 'socks4://', proxies['socks'])
                    proxies['http'] = proxies.get('http') or address
                    proxies['https'] = proxies.get('https') or address
            internetSettings.Close()
        except (OSError, ValueError, TypeError):
            pass
        return proxies


if __name__ == "__main__":
    getProxy = GetProxy()
    proxy = getProxy.run()
    print('proxy', proxy)

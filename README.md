### 一句话介绍

myChat 是一款第三方 ChatGPT 客户端，基于 OpenAI 接口调用，支持 Windows 和 macOS 系统。

### 运行前提条件

- **魔法上网**。
- **需要 sk 码**。本软件不提供也不保存 sk 码，用户需要自行 [注册账号](https://blog.pangao.vip/超详细注册OpenAI接口账号的教程/) ，获取 sk 码。

### 软件安装

#### 下载软件安装包

在 https://github.com/pangao1990/myChat/releases 中下载对应系统的最新软件安装包。

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-1.png)

#### Windows 安装步骤

- 双击安装包，选择【下一步】

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-2.png)

- 选择【安装】

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-3.png)

- 选择【完成】，即完成软件安装

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-4.png)

#### macOS 安装步骤

- 双击安装包，将 myChat.app 拖入右边的 Applications 文件夹，即完成软件安装

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-5.png)

### 简单使用

- 双击桌面快捷方式，打开 myChat 软件。

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-6.png)

- 首次使用，需要输入 **sk 码**。

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-7.png)

- 【重要】打开魔法上网，设置全局代理。

此时，便可使用 myChat 客户端与 ChatGPT 对话了。

### 高级功能

#### 新增聊天主题

点击左上角的 **+号**，即可添加新的聊天主题。

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-8.png)

- 聊天标题：仅为方便使用者标记分类，不会传递给 ChatGPT
- 聊天主题：该主题信息会在每一次聊天过程中发送给 AI，请尽量详细描述
- GPT 模型：支持 **gpt-4** 、 **gpt-4-32k** 、 **gpt-3.5-turbo** 、 **text-davinci-003** 等模型。当然了，gpt-4 模型需要 sk 码已经申请获批权限。建议一般情况下使用 gpt-3.5-turbo 模型，性价比最高。
- 记忆消息个数：发送给 ChatGPT 的历史消息个数。选择【0】则表示每次都是独立会话，不会发送历史对话记录给 ChatGPT。选择【全部】则表示会将全部历史对话发送给 ChatGPT 作为参考。
- 模型参数：也就是 ChatGPT 的 temperature 参数。数值越小，回复越精准。数值越大，回复越多元化。

#### 主题广场

本软件预设了很多可用的主题，免费给用户使用。例如：论文润色、模拟面试、担任导游、下五子棋、脱口秀演员、作曲家、心理医生、编写代码、虚拟女友等等。

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-9.png)

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-10.png)

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-11.png)

### 注意事项

如若出现魔法上网已开启，但仍然出现连接超时的情况，请手动设置代理 IP 和端口。

报错信息如下：

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-12.png)

左下角【更多设置】选择【设置代理】：

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-13.png)

在魔法上网的软件中找到代理 IP 和端口信息，依次填入，确认保存。

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-14.png)

### 软件部分截图

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-15.png)

![image](https://pangao1990.gitee.io/pic/myChat——第三方ChatGPT客户端又双叒叕更新啦-16.png)

### 历史版本

##### V2.4.1

- 修复自定义 API 地址时，无法使用 http 协议的问题。

##### V2.4.0

- 新增自定义 API 地址。

##### V2.3.1

- 修复 macOS 的 Intel 芯片平台下无法复制内容的问题。

##### V2.3.0

- 修复部分 win10 系统白屏的问题。
- 优化程序安装包。

##### V2.2.2

- 将超时提示由原来的 100 秒改为 300 秒。
- 修复 macOS 的 Intel 芯片版本在自动升级中遇到的一些问题。

##### V2.2.1

- 修复某些情况下连接超时后无法继续提问的 bug。

##### V2.2.0

- 新增主题广场，提供众多 prompt。

##### V2.1.0

- 新增代码高亮。
- 修复 Windows 平台下无法自动获取代理信息的问题。

##### V2.0.1

- 修复由 urllib3 模块引起的 SSLEOFError 错误问题。

##### V2.0.0

- 新增 GPT 模型选择、参数调节。
- 新增自动获取系统代理 IP 及端口。
- 新增自动检测软件升级。
- 修复对话内容无法复制的问题。
- 优化数据库结构。

##### V1.2.0

- 初始版本。

---

更多编程教学请关注公众号：**潘高陪你学编程**

![image](https://pangao1990.gitee.io/pic/潘高陪你学编程.jpg)

---

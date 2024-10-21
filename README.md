# xhs-wb-crawler
# 小红书爬虫

本项目旨在对小红书内容进行爬取,支持爬取搜索页、个人主页、详情页;
支持爬取微博关注的超话列表，并签到（可返回签到数）

## 安装

在开始使用该项目之前，请确保已经安装了所需的依赖库


## 配置

### 1. 配置 Cookies
1.运行命令 python tool/cookie_util.py 获取chrome浏览器下的cookie
2.直接修改 static/cookies.txt 文件

## 运行 🚀

- 运行 `python search.py` 进行关键词搜索：


## 注意事项 ⚠️

- 确保您已配置正确的 Cookies
- 爬取小红书数据时，请遵循相关法律法规和平台规定，避免违反用户隐私或平台政策。
# 小红书爬虫

本项目旨在对小红书内容进行爬取

## 安装

在开始使用该项目之前，请确保已经安装了所需的依赖库


## 配置

### 1. 配置 Cookies
1.运行命令 python tool/cookie_util.py 获取chrome浏览器下的cookie
2.直接修改 static/cookies.txt 文件

## 运行 🚀

- 运行 `python search.py` 进行关键词搜索,并导出结果到excel
- 运行 `python profile.py` 查询个人主页信息
- 运行 `python detail.py` 查询小红书详情页信息
- 运行 `python sign.py` 抓取关注的微博超话，并且签到，返回当前签到数（需要修改 tool/util.py 脚本中get_weibo_headers方法的cookie字段）


## 注意事项 ⚠️

- 确保您已配置正确的 Cookies
- 爬取小红书数据时，请遵循相关法律法规和平台规定，避免违反用户隐私或平台政策。

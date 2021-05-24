## flaskBlog
基于python3和flask的博客

## 用到的技术
- python3
- flask
- flask-wtf
- flask-sqlalchemy
- markdown
- bootstrap4
- mysql等

## 主要功能
- 撰写文章
- 文章列表
- 文章分类
- 标签管理
- 推荐文章
- SEO优化 
- 内置图床
- 网站设置
- 百度推送
- 会员注册
- 邀请码
- 搜索引擎抓取统计

## 配置
配置都是在 `setting.py` 中，也可以在后台配置。


## 运行
默认开发环境为Ubuntu 20.04.2.0 LTS
```
$ git clone https://gitee.com/9233/flaskblog.git
$ cd flaskblog
$ python3 -m venv venv  #创建python虚拟环境
$ source venv/bin/activate
$ 
$ pip install -r requirements.txt # 安装项目依赖，可能不全，根据提示自行安装即可

mysql>create database flaskblog default charset 'utf8' collate 'utf8_general_ci';
$ flask initdb #创建数据库
$ export FLASK_ENV=development
$ flask run # 启动
```

`首次访问后台先创建后台管理账号：http://127.0.0.1:5000/admin 根据提示创建账号，并登录`

## 博客演示地址
http://www.flaskblog.com

## 新功能开发
我会不断持续更新新功能，期待更多的flasker者加入，让flaskBlog更强大！
如果你希望添加某个新功能，请在[这里](https://github.com/9233/flaskblog/issues/2)提交。

---
 ## 致大家🙋‍♀️🙋‍♂️
 如果本项目帮助到了你，请在[这里](https://github.com/9233/flaskblog/issues/1)留下你的网址，让更多的人看到。
您的回复将会是我继续更新维护下去的动力。 

## 问题相关
有任何问题欢迎提Issue，或者将问题描述发送至我邮箱 `superchao0727@gmail.com`.我会尽快解答.推荐提交Issue方式.  

## 感谢jetbrains

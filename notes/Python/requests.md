---
layout: page
title:  Python 之 requests 模块
update: 2017-07-17 21:01 +0800
---

## 概述

requests 模块，注意是最后有 s 的，注意拼写。

## 安装　

```pip install requests```

## 使用

requests 支持GET POST DELETE等多种方法

```python
r = requests.get('https://api.github.com/events')
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

r.status_code #返回状态码
r.text #返回的内容，同 r.content
r.url #返回最终的URL，重定向的返回重定向后的地址（allow_redirects=False设置禁止重定向)
r.json() #如果返回值能整理成 json 格式，这个函数能将文本弄成相关的 Python 对象
r.encoding='utf-8' #编码方式

#自定义headers
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

#设置time-out 单位是秒
requests.get(url,timeout=0.01)

#查看响应头
r.headers
r.headers.get('content-type')
r.headers['content-type']

#访问cookies
r.cookies['example_cookie_name']

#会话对象，能跨请求保留有关数据，或者提供请求的默认参数
with requests.Session() as s:
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})
    s.get(url)
    
#使用代理
proxies = {
  "http": "http://10.10.1.10:3128",
  "http": "http://user:pass@10.10.1.10:3128/",
  "https": "http://10.10.1.10:1080",
}

requests.get("http://example.org", proxies=proxies)
```




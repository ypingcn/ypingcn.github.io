---
layout: page
title:  Let's Encrypt 使用记录
update: 2017-07-15 21:30 +0800
---

不管如何，加上 https 是个明智的选择。

## 安装

在网上找到的大部分是从源代码编译开始用的，找到一个 certbot ，是用 PPA 装的软件，方便不少。

https://certbot.eff.org/

以我自己的配置来说（Ubuntu 16.04 + Nginx），安装的命令是这样的：

```
$ sudo apt-get update
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install python-certbot-nginx 
```

具体命令，在上面的链接中正确选择好就会显示。

## 相关文件生成

运行 ``` sudo letsencrypt certonly ```

提示

```
How would you like to authenticate with the ACME CA?
1: Spin up a temporary webserver (standalone)
2: Place files in webroot directory (webroot)
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 
```

选择1（standalone 和 webroot 的区别可以看看这篇 《[Let's Encrypt SSL证书配置](http://www.jianshu.com/p/eaac0d082ba2)》 )

之后提示

```Please enter in your domain name(s) (comma and/or space separated)  (Enter 'c' to cancel):```

根据提示输入域名


出现类似于以下内容就是正确配置了

```
IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at
   /etc/letsencrypt/live/domain.com/fullchain.pem. Your cert will
   expire on 2017-10-13. To obtain a new or tweaked version of this
   certificate in the future, simply run certbot again. To
   non-interactively renew *all* of your certificates, run "certbot
   renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

```

生成2048位 DH parameters：

```
sudo openssl dhparam -out /etc/ssl/certs/dhparams.pem 2048
```

## 修改 Nginx 配置

在 /etc/nginx/sites-enabled 下新建文件，添加以下内容

```
server {
         listen 443 ssl;
         server_name domain.com;
         ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem;
         ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem;
         ssl_dhparam /etc/ssl/certs/dhparams.pem;
         ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-A    ES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-S    HA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-    AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-S    HA:AES256-SHA:AES:CAMELLIA:DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC    3-SHA';
        ssl_prefer_server_ciphers on;
}
```

重启 Nginx 后即可生效。


---
layout: page
title:  Let's Encrypt 使用记录
date: 2017-07-15 21:30 +0800
update: 2021-11-19 22:56 +0800
---

随着网络技术的发展，原有的网络传输设计也遇到了各种问题。使用 HTTP 传输无法保证中间内容不会被第三方修改，所以便诞生了基于 HTTP 的 HTTPS 协议。多了一层虽然会给服务端增加额外的开销，但这对于用户而言是值得的，加上 HTTPS 是个明智的选择。各方都在鼓励网站向 HTTPS 方向进行改造，搜索引擎也对 HTTPS 的网站给予不同程度的加分。

HTTPS 需要安装相关的证书，付费免费都能找到相应的服务商。而其中最有名的便是 Let's Encrypt 了，免费且能满足 HTTPS 的使用需求，连 Github Page 等服务都使用了 Let's Encrypt 的证书。这家的证书是使用一个叫 Certbot 的程序生成的。Certbot 是 Let's Encrypt 的官方工具。

下面便是 Certbot 相关的安装使用记录——

## 安装

在网上找到的大部分是从源代码编译开始用的，找到一个 Certbot ，是用 PPA 装的软件，方便不少。

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

提示选择验证的方式。

```
How would you like to authenticate with the ACME CA?
1: Spin up a temporary webserver (standalone)
2: Place files in webroot directory (webroot)
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 
```

因为是个人向的网站，没有太多可用性的要求，便选择 1 。（standalone 和 webroot 的区别在于，standalone 是用服务器的 80 / 443 端口验证的，需要暂停所在机器的服务，而 webroot 是在网站根目录下生成一个特殊的文件夹，通过 Certbot 的官方服务器发出请求，判断是否能验证成功 )

之后终端中便会提示要求输入域名。

```Please enter in your domain name(s) (comma and/or space separated)  (Enter 'c' to cancel):```


输入且验证成功后，如出现类似于以下内容就是正确生成证书了。

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

重启 Nginx 后即可生效，完成 HTTPS 证书的部署。


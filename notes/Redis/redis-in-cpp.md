---
layout: page
title:  C++ 使用 redis
update: 2017-09-17 15:43 +0800
---

> 参考　[hiredis/README.md at master · redis/hiredis · GitHub](https://github.com/redis/hiredis/blob/master/README.md)


C++ 中使用 redis 可以用 hiredis 完成，但是 hiredis 是用 C 语言写的，使用起来还是要做一点改变，而不只是加个头文件。

## 下载 hiredis

``` git clone https://github.com/redis/hiredis```

## 编译 hiredis

``` make ```

文件夹将会有``` libhiredis.so ``` 

## 准备 C++ 文件

在 hiredis 的同级目录下新建``` test.cpp ```，内容如下

```c++
extern "C"
{
  #include "hiredis/hiredis.h"
}

#include <iostream>
int main(int argc, char const *argv[]) {
  redisContext* redis = redisConnect("127.0.0.1", 6379);
  // 用来连接redis数据库，参数为数据库的ip地址和端口，一般redis数据库的端口为6379。类似的函数有redisContext* redisConnectWithTimeout(const char *ip, int port, timeval tv) 
  if( redis == NULL || redis->err ) //当 redis->err 为真时，redis->errstr 显示具体的错误原因
  {
    std::cout << redis->errstr << '\n';
  }
  const char * command = "set test yes";
  redisReply * reply = (redisReply*) redisCommand(redis, command); //  返回值为void*，强制转换成为redisReply类型
  if(reply == NULL)
  {
    std::cout << "error" << '\n';
    redisFree(redis);
  }
  if(reply->type == REDIS_REPLY_STATUS)　// REDIS_REPLY_STATUS 返回状态，可以用 strcasecmp(reply->str,"OK") 判断是否正确执行
  {
    std::cout << "redis reply is : " << reply->str << '\n';
  }
  std::cout << "test finish" << '\n';
  freeReplyObject(reply); // 释放 reply 占用的内存
  redisFree(redis); // 断开连接
  return 0;
}
```
留意最上面的

``` extern "C" ``` 部分即可

## 编译 C++ 程序

``` g++ test.cpp hiredis/libhiredis.so ```
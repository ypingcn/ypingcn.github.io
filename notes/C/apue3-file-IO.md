---
layout: page
title:  第三章 文件IO
date: 2017-09-25 20:18 +0800
update: 2021-11-19 23:29 +0800
---

简单记录一下
```cpp
#include <fcntl.h>

int open(const char *__file, int __oflag, ...)
int openat(int __fd, const char *__file, int __oflag, ...)
```

openat 返回最小的未用的文件描述符。openat 的第一个参数可以用 open 返回值，例如

```cpp
cout << openat(open("/home/",O_DIRECTORY),"a.txt",O_RDONLY) << endl;
```

有以下参数可以在 __oflag 上使用

O_RDONLY 只读

O_WRONLY　只写

O_RDWR　可读可写

O_DIRECTORY　非目录返回错误

// P50

```cpp
#include <fcntl.h>

int creat(const char *__file, mode_t __mode)
```

S_IRUSR S_IWUSR S_IXUSR 用户读\写\执行

S_IRGRP S_IWGRP S_IXGRP 组

S_IROTH S_IWOTH S_IXOTH 其他

按位与　作为参数

返回为只写打开的文件描述符


```cpp
#include <unistd.h>

int close(int __fd)
```
成功0错误-1

```cpp
#include <unistd.h>

__off_t lseek(int __fd, __off_t __offset, int __whence)
```
返回新的成功偏移量，错误-1

有以下选项给 - __whence

SEEK_SET SEEK_CUR SEEK_END，分别对应 开始位置　当前位置　结束位置
```lseek(int __fd, 0, SEEK_END)``` 返回值等同文件大小

```cpp
#include <unistd.h>

ssize_t read(int __fd, void *__buf, size_t __nbytes)
```
返回读到的字节数　文件末则为0　错误-1

```cpp
#include <unistd.h>

ssize_t write(int __fd, const void *__buf, size_t __n)
```
返回已写的字节数　错误为 -1

```cpp
#include <unistd.h>

ssize_t pread(int __fd, void *__buf, size_t __nbytes, __off_t __offset)
ssize_t pwrite(int __fd, const void *__buf, size_t __n, __off_t __offset)
```
相当于先lseek 再read/write ，但不更新当前文件偏移量

```cpp
#include <unistd.h>

int dup(int __fd)
int dup2(int __fd, int __fd2)
```
返回新文件描述符，第二个可以指定（若fd2已打开则关闭）

```cpp
#include <unistd.h>

void sync()
int fsync(int __fd)
int fdatasync(int __fildes)
```

sync 将修改过的块排入队列并马上返回。

fsync 特定文件操作，更新数据＋属性，磁盘写完成后才返回。0 正常 -1　错误。

fdatasync 类似 fsync ，但只更新数据。

```cpp
#include <fcntl.h>

int fcntl(int __fd, int __cmd, ...)
```
cmd 有

复制已有描述符 F_DUPFD

获取、设置文件描述符 F_GETFD F_SETFD

获取、设置文件状态标志 F_GETFL F_SETFL(先&F_ACCMODE再与 O_RDONLY 等比较)

//等P65

```cpp
#include <sys/ioctl.h>

ioctl(int __fd, unsigned long __request, ...)
```
//后续

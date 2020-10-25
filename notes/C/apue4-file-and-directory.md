---
layout: page
title:  第四章 文件和目录
date: 2017-09-25 20:18 +0800
update: 2021-11-20 21:19 +0800
---

```cpp
#include <sys/stat.h>

int stat(const char *__restrict __file, struct stat *__restrict __buf)
int fstat(int __fd, struct stat *__buf)
int lstat(const char *__restrict __file, struct stat *__restrict __buf)
int fstatat(int __fd, const char *__restrict __file, struct stat *__restrict __buf, int __flag)
```
lstat 返回的是文件链接信息，fstatat 是相对路径信息。上述接口错误会返回 ERRNO 的错误码

 - ENOENT         参数file_name指定的文件不存在
 - ENOTDIR        路径中的目录存在但却非真正的目录
 - ELOOP          欲打开的文件有过多符号连接问题，上限为16符号连接
 - EFAULT         参数buf为无效指针，指向无法存在的内存空间
 - EACCESS        存取文件时被拒绝
 - ENOMEM         核心内存不足
 - ENAMETOOLONG   参数file_name的路径名称太长


 - S_ISLNK (st_mode)    判断是否为符号连接
 - S_ISREG (st_mode)    是否为一般文件
 - S_ISDIR (st_mode)    是否为目录
 - S_ISCHR (st_mode)    是否为字符装置文件
 - S_ISBLK (st_mode)    是否为先进先出
 - S_ISSOCK (st_mode)   是否为socket

//等 P76
//判断文件类型

```cpp
#include <unistd.h>

int access(const char *__name, int __type)
int faccessat(int __fd, const char *__file, int __type, int __flag)
```

按实际用户id 和实际用户组id 进行权限测试。

```__type``` 有　R_OK W_OK X_OK

```__flag``` 为 AT_EACCESS时用的是调用进程的有效用户id 和有效用户组id

```cpp
#include <sys/stat.h>

__mode_t umask(__mode_t __mask)
```
```__mode_t``` 的取值

 - S_IRUSR S_IWUSR S_IXUSR 用户读\写\执行
 - S_IRGRP S_IWGRP S_IXGRP 组
 - S_IROTH S_IWOTH S_IXOTH 其他

按位与　作为参数，禁止所设置的

```cpp
#include <sys/stat.h>

int chmod(const char *__file, __mode_t __mode);
int fchmod(int __fd, __mode_t __mode);
int fchmodat(int __fd, const char *__file, __mode_t __mode, int __flag)

struct stat {
  mode_t     st_mode;       //文件访问权限
  ino_t      st_ino;       //索引节点号
  dev_t      st_dev;        //文件使用的设备号
  dev_t      st_rdev;       //设备文件的设备号
  nlink_t    st_nlink;      //文件的硬连接数
  uid_t      st_uid;        //所有者用户识别号
  gid_t      st_gid;        //组识别号
  off_t      st_size;       //以字节为单位的文件容量
  time_t     st_atime;      //最后一次访问该文件的时间
  time_t     st_mtime;      //最后一次修改该文件的时间
  time_t     st_ctime;      //最后一次改变该文件状态的时间
  blksize_t st_blksize;    //包含该文件的磁盘块的大小
  blkcnt_t   st_blocks;     //该文件所占的磁盘块
};
```

```__flag``` 设置了　AT_SYMLINK_NOFOLLOW 时不会跟随符号链接

```__mode_t``` 加上之前的９个还有

 - S_IRWXU S_IRWXG S_IRWXO 用户读写执行、组读写执行、其他读写执行
 - S_ISVTX 保存正文
 - S_ISUID 执行设置用户ID
 - S_ISGID 执行设置组ID

```cpp
#include <unistd.h>

int chown(const char *__file, __uid_t __owner, __gid_t __group);
int fchown(int __fd, __uid_t __owner, __gid_t __group);
int fchownat(int __fd, const char *__file, __uid_t __owner, __gid_t __group, int __flag)
int lchown(const char *__file, __uid_t __owner, __gid_t __group)
```

```__flag``` 设置了　AT_SYMLINK_NOFOLLOW 时更改链接本身所有者

```cpp
#include <unistd.h>

int truncate(const char *__file, __off_t __length)
int ftruncate(int __fd, __off_t __length)
```

truncate 文件截断，length 小于实际则剩余部分无法访问，大于则空洞

```cpp
#include <unistd.h>
int link(const char *__from, const char *__to)
int linkat(int __fromfd, const char *__from, int __tofd, const char *__to, int __flags)
int unlink(const char *__name)
int unlinkat(int __fd, const char *__name, int __flag)
```

硬链接
```cpp
#include <stdio.h>
remove(const char *__filename)
```

删除的接口 remove

```cpp
#include <stdio.h>

int rename(const char *__old, const char *__new)
int renameat(int __oldfd, const char *__old, int __newfd, const char *__new)
```

重命名接口

```cpp
#include <unistd.h> 

int symlink(const char *__from, const char *__to)
int symlinkat(const char *__from, int __tofd, const char *__to)
```

创建符号链接，原文件在前。

```cpp
#include <unistd.h>
ssize_t readlink(const char *__restrict __path, char *__restrict __buf, size_t __len)
ssize_t readlinkat(int __fd, const char *__restrict __path, char *__restrict __buf, size_t __len)
```

因为open()会跟随链接，用这些读取链接本身

```cpp
#include <sys/stat.h>

int futimens(int __fd, const struct timespec *__times)

struct timespec {
    time_t tv_sec;        /* seconds */
    long   tv_nsec;       /* nanoseconds 10^-9*/
};

int utimensat(int __fd, const char *__path, const struct timespec *__times, int __flags)
int utimes(const char *__file, const struct timeval *__tvp)
struct timeval {
  time_t tv_sec;  /* seconds */
  long tv_usec; 　　/* microsecond 10^-3 */
}
```

修改访问时间和修改时间的接口，```__times``` 为空指针则修改为当前时间。

utimensat 第二个函数的__path参数是相对于fd 参数计算的，fd要么是打开目录的文件描述符，要么设置为AT_FDCWD ,__path为绝对路径则忽略　fd 参数

```cpp
#include <sys/stat.h>

int mkdir(const char *__path, __mode_t __mode);
int mkdirat(int __fd, const char *__path, __mode_t __mode);

struct __dirstream {
  void * __fd;
  char * __data;
  int __entry_data;
  char * __ptr;
  int __entry_ptr;
  size_t __allocation;
  size_t __size;
  __libc_lock_define(, __lock)
};

typedef struct __dirstream DIR;

struct dirent {
  long d_ino; /* inode number 索引节点号 */
  off_t d_off; /* offset to this dirent 在目录文件中的偏移 */
  unsigned short d_reclen; /* length of this d_name 文件名长 */
  unsigned char d_type; /* the type of d_name 文件类型 */
  char d_name[NAME_MAX + 1]; /* file name (null-terminated) 文件名，最长255字符 */
}

struct stat {
  mode_t st_mode; //文件访问权限   
  ino_t st_ino; //索引节点号   
  dev_t st_dev; //文件使用的设备号   
  dev_t st_rdev; //设备文件的设备号   
  nlink_t st_nlink; //文件的硬连接数   
  uid_t st_uid; //所有者用户识别号   
  gid_t st_gid; //组识别号   
  off_t st_size; //以字节为单位的文件容量   
  time_t st_atime; //最后一次访问该文件的时间   
  time_t st_mtime; //最后一次修改该文件的时间   
  time_t st_ctime; //最后一次改变该文件状态的时间   
  blksize_t st_blksize; //包含该文件的磁盘块的大小   
  blkcnt_t st_blocks; //该文件所占的磁盘块   
};
```

```cpp
#include <unistd.h>

int rmdir(const char *__path);
```

删除指定的目录。

```cpp
#include <unistd.h>

int chdir(const char *__path)
int fchdir(int __fd)
char *getcwd(char *__buf, size_t __size)
```

返回当前工作目录的绝对路径 buf,出错则为NULL。
---
layout: page
title:  第四章 文件和目录
update: 2017-09-25 20:18 +0800
---

```cpp
#include <sys/stat.h>
int stat(const char *__restrict __file, struct stat *__restrict __buf)
int fstat(int __fd, struct stat *__buf)
int lstat(const char *__restrict __file, struct stat *__restrict __buf)
//返回文件链接信息
int fstatat(int __fd, const char *__restrict __file, struct stat *__restrict __buf, int __flag)
//相对路径信息
//[linux stat函数讲解 - Leo Chin - 博客园]
//(http://www.cnblogs.com/hnrainll/archive/2011/05/11/2043361.html)
S_ISREG(__buf.st_mode)
S_ISDIR() S_ISSOCK()
//等 P76
//判断文件类型

#include <unistd.h>
// 按实际用户id 和实际用户组id 进行权限测试
int access(const char *__name, int __type)
int faccessat(int __fd, const char *__file, int __type, int __flag)
//__type 有　R_OK W_OK X_OK
//__flag 为 AT_EACCESS时用的是调用进程的有效用户id 和有效用户组id

#include <sys/stat.h>
__mode_t umask(__mode_t __mask)
__mode_t
//S_IRUSR S_IWUSR S_IXUSR 用户读\写\执行
//S_IRGRP S_IWGRP S_IXGRP 组
//S_IROTH S_IWOTH S_IXOTH 其他
//按位与　作为参数，禁止所设置的

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

//__flag 设置了　AT_SYMLINK_NOFOLLOW 时不会跟随符号链接
//__mode_t 加上之前的９个还有
//S_IRWXU S_IRWXG S_IRWXO 用户读写执行、组读写执行、其他读写执行
//S_ISVTX 保存正文
//S_ISUID 执行设置用户ID
//S_ISGID 执行设置组ID
//[4.4 S_ISUID、S_ISGID位与文件访问权限检查 - zhoulaowu的专栏 - CSDN博客]
//(http://blog.csdn.net/zhoulaowu/article/details/14103599)

#include <unistd.h>
int chown(const char *__file, __uid_t __owner, __gid_t __group);
int fchown(int __fd, __uid_t __owner, __gid_t __group);
int fchownat(int __fd, const char *__file, __uid_t __owner, __gid_t __group, int __flag)
int lchown(const char *__file, __uid_t __owner, __gid_t __group)
//__flag 设置了　AT_SYMLINK_NOFOLLOW 时更改链接本身所有者

#include <unistd.h>
int truncate(const char *__file, __off_t __length)
int ftruncate(int __fd, __off_t __length)
//文件截断，length 小于实际则剩余部分无法访问，大于则空洞

#include <unistd.h> //硬链接
int link(const char *__from, const char *__to)
int linkat(int __fromfd, const char *__from, int __tofd, const char *__to, int __flags)
int unlink(const char *__name)
int unlinkat(int __fd, const char *__name, int __flag)

#include <stdio.h>
remove(const char *__filename)

#include <stdio.h>
int rename(const char *__old, const char *__new)
int renameat(int __oldfd, const char *__old, int __newfd, const char *__new)

#include <unistd.h> 
//符号链接，原文件在前
int symlink(const char *__from, const char *__to)
int symlinkat(const char *__from, int __tofd, const char *__to)

#include <unistd.h>
ssize_t readlink(const char *__restrict __path, char *__restrict __buf, size_t __len)
ssize_t readlinkat(int __fd, const char *__restrict __path, char *__restrict __buf, size_t __len)
// 因为open()会跟随链接，用这些读取链接本身

#include <sys/stat.h>
//修改访问时间和修改时间
int futimens(int __fd, const struct timespec *__times)
//__times 为空指针则修改为当前时间
struct timespec {
    time_t tv_sec;        /* seconds */
    long   tv_nsec;       /* nanoseconds 10^-9*/
};
int utimensat(int __fd, const char *__path, const struct timespec *__times, int __flags)
//第二个函数的__path参数是相对于fd 参数计算的，fd要么是打开目录的文件描述符，要么设置为AT_FDCWD ,__path为绝对路径则忽略　fd 参数
int utimes(const char *__file, const struct timeval *__tvp)
struct timeval {
  time_t tv_sec;  /* seconds */
  long tv_usec; 　　/* microsecond 10^-3 */
}

#include <sys/stat.h>
int mkdir(const char *__path, __mode_t __mode);
int mkdirat(int __fd, const char *__path, __mode_t __mode);

//[Linux下DIR，dirent,stat等结构体详解 - 菜鸟的逆袭 - CSDN博客]
//(http://blog.csdn.net/zhuyi2654715/article/details/7605051)

#include <unistd.h>
int rmdir(const char *__path);

#include <unistd.h>
int chdir(const char *__path)
int fchdir(int __fd)
char *getcwd(char *__buf, size_t __size)
//返回当前工作目录的绝对路径 buf,出错则为NULL
```
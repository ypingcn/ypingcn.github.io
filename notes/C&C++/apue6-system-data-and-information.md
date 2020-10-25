---
layout: page
title:  第六章 系统数据文件和信息
update: 2017-09-25 20:18 +0800
---

```cpp
struct passwd
{
   char * pw_name; /* Username, POSIX.1 */
   char * pw_passwd; /* Password */
   __uid_t pw_uid; /* User ID, POSIX.1 */
   __gid_t pw_gid; /* Group ID, POSIX.1 */
   char * pw_gecos; /* Real Name or Comment field */
   char * pw_dir; /* Home directory, POSIX.1 */
   char * pw_shell; /* Shell Program, POSIX.1 */
};

#include <pwd.h>
srtuct passwd * getpwuid(__uid_t __uid)
struct passwd * getpwnam(const char *__name)

struct passwd * getpwent(void) // 从 /etc/passwd 读取一行

void endpwent(void) // 关闭文件



struct spwd
{
    char *sp_namp; /* Login name */
    char *sp_pwdp; /* Encrypted password */
    long int sp_lstchg; /* Date of last change */
    long int sp_min; /* Minimum number of days between changes */
    long int sp_max; /* Maximum number of days between changes */
    long int sp_warn; /* Number of days to warn user to change the password */
    long int sp_inact; /* Number of days the account may be inactive */
    long int sp_expire; /* Number of days since 1970-01-01 until account expires */
    unsigned long int sp_flag; /* Reserved */
};

#include <shadow.h>
//要用管理员权限运行，否则会出错
struct spwd * getspnam(const char *__name)
struct spwd * getspent(void)


struct group
{
    char *gr_name;  /* Group name */
    char *gr_passwd;  /* password */
    __gid_t gr_gid;  /* Group ID */
    char **gr_mem;  /* Member list */
}

#include <grp.h>
struct group * getgrgid(__gid_t __gid)
struct group * getgrnam(const char *__name)
struct group * getgrent() // 从　/etc/group/ 读取一行
void endgrent(void ) // 关闭文件

#include <unistd.h>
int getgroups(int __size, __gid_t *__list) // 获取程序所属用户的附属组数,size 为 0 时不修改 list 的内容
#include <grp.h>
int setgroups(size_t __n, const __gid_t *__groups)
int initgroups(const char *__user, __gid_t __group)

/*
/etc/passed 口令
/etc/group 组
/etc/shadow 阴影　【??】
/etc/hosts 主机
/etc/networks 网络
/etc/protocols 协议
/etc/services 服务
P149
*/

#include <sys/utsname.h>
int uname(struct utsname *__name)
struct utsname{
 char sysname[_UTSNAME_SYSNAME_LENGTH];//当前操作系统名
 char nodename[_UTSNAME_NODENAME_LENGTH];//网络上的名称
 char release[_UTSNAME_RELEASE_LENGTH];//当前发布级别
 char version[_UTSNAME_VERSION_LENGTH];//当前发布版本
 char machine[_UTSNAME_MACHINE_LENGTH];//当前硬件体系类型
}

#include <unistd.h>
int gethostname(char *__name, size_t __len) // 网络中的主机名

#include <time.h>
time_t time(time_t *__timer) // 结果在返回值和参数里

#include <sys/time.h>
int clock_gettime(clockid_t __clock_id, struct timespec *__tp)
// CLOCK_REALTIME:系统实时时间,随系统实时时间改变而改变,即从UTC1970-1-1 0:0:0开始计时,
// CLOCK_MONOTONIC:从系统启动这一刻起开始计时,不受系统时间被用户改变的影响
// CLOCK_PROCESS_CPUTIME_ID:本进程到当前代码系统CPU花费的时间
// CLOCK_THREAD_CPUTIME_ID:本线程到当前代码系统CPU花费的时间
int clock_getres(clockid_t __clock_id, struct timespec *__res) // 获取时间精度
int clock_settime(clockid_t __clock_id, const struct timespec *__tp)

struct tm {
  int tm_sec;       /* 秒 – 取值区间为[0,59] */
  int tm_min;       /* 分 - 取值区间为[0,59] */
  int tm_hour;      /* 时 - 取值区间为[0,23] */
  int tm_mday;      /* 一个月中的日期 - 取值区间为[1,31] */
  int tm_mon;       /* 月份（从一月开始，0代表一月） - 取值区间为[0,11] */
  int tm_year;      /* 年份，其值等于实际年份减去1900 */
  int tm_wday;      /* 星期 – 取值区间为[0,6]，其中0代表星期天，1代表星期一，以此类推 */
  int tm_yday;      /* 从每年的1月1日开始的天数 – 取值区间为[0,365]，其中0代表1月1日，1代表1月2日，以此类推 */
  int tm_isdst;     /* 夏令时标识符，实行夏令时的时候，tm_isdst为正。不实行夏令时的进候，tm_isdst为0；不了解情况时，tm_isdst()为负。*/
};

#include <time.h>
struct tm * gmtime(const time_t *__timer) //UTC时间
struct tm * localtime(const time_t *__timer) //本地时间
time_t mktime(struct tm *__tp) // tm 与 time_t 的转换
size_t strftime(char *__restrict __s, size_t __maxsize, const char *__restrict __format, const struct tm *__restrict __tp) // 返回存入数组的字符数
char * strptime(const char *__restrict __s, const char *__restrict __fmt, struct tm *__tp) // 返回指向上次解析的字符的下一个字符的指针，错误为　NULL P156


//例子 P154
time_t t = time(nullptr);
struct tm * tmp = localtime(&t);
char buf[16];
if ( strftime(buf,16,"%r ",tmp) == 0 )
  cout<<"error"<<endl;
else
  cout<<buf<<endl;
```
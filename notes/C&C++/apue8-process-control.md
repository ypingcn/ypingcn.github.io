---
layout: page
title:  第八章 进程控制
update: 2017-09-25 20:18 +0800
---

```cpp
#include <unistd.h>
__pid_t getpid() // 调用进程的进程id
__pid_t getppid() // 父进程id
__uid_t getuid() // 调用进程的实际用户id
__uid_t geteuid() // 调用进程的有效用户id
__gid_t getgid()　// 实际组id
__gid_t getegid() // 有效组id

__pid_t fork() // 子进程返回0 父进程返回子进程id 出错为-1
//fork 之后父进程先执行还是子进程先执行是不确定的
//在重定向父进程的标准输出时，子进程的标准输出也被重定向
//父进程和子进程共享一个文件偏移量
//子进程不能修改父进程变量

__pid_t vfork() // 返回值同fork() 但保证子进程先运行　子进程能修改父进程变量

//僵尸进程是指已经终止但其父进程尚未对其进行善后处理的进程　P189

#include <sys/wait.h>
__pid_t wait(void *__stat_loc) // 阻塞调用则，直到子进程终止成为僵尸进程
__pid_t waitpid(__pid_t __pid, int *__stat_loc, int __options) // 返回终止子进程的进程 id

//__stat_loc 为终止状态，用以下宏判断具体情况
//WIFEXITED(status) 正常终止，这种情况下可以用　WEXITSTATUS(status) 获得具体的返回值
//WIFSIGNALED(status)　异常终止，用　WTERMSIG(status) 获得信号编号
//WIFSTOPPED(status) 子进程暂停【？】
//WIFCONTINUED(status)　子进程暂停后继续【？】

//参数__pid 说明：
// == -1 任意子进程
// > 0　pid 相同的子进程
// == 0 组id等于调用进程组id的任意子进程（第九章）
//< -1 等待组id 等于参数绝对值的任意一个子进程

 //__options 参数+例子　P193　按位或运算的结果
 //WCONTINUED 子进程暂停后继续但未报告状态
 //WNOHANG 若子进程不是立即可用的，不阻塞，返回值为 0
 //WUNTRACED　子进程停止后但未报告状态

#include <sys/wait.h>
int waitid(idtype_t __idtype, __id_t __id, siginfo_t *__infop, int __options)

//__idtype
//P_PID 特定进程
//P_PGID　特定进程组的任一子进程
//P_ALL　任意进程 忽略参数 __id

//__options
//WCONTINUED
//WNOHANG
//WUNTRACED
//WEXITED 等待已经退出的进程
//WNOWAIT 不破坏子进程的退出进程
//WSTOPED 进程终止但为报告　【？】

#include <sys/types.h>
#include <sys/wait.h>
#include <sys/time.h>
#include <sys/resource.h>
pid_t wait3(void *__stat_loc, int __options, struct rusage *__usage)
pit_d wait4(__pid_t __pid, void *__stat_loc, int __options, struct rusage *__usage)

// wait3等待所有的子进程；wait4可以像waitpid一样指定要等待的子进程：pid>0表示子进程ID；pid=0表示当前进程组中的子进程；pid=-1表示等待所有子进程；pid<-1表示进程组ID为pid绝对值的子进程。

struct rusage {
struct timeval ru_utime; /* user time used */
struct timeval ru_stime; /* system time used */
long ru_maxrss;
#define ru_first ru_ixrss
long ru_ixrss; /* XXX: 0 */
long ru_idrss; /* XXX: sum of rm_asrss */
long ru_isrss; /* XXX: 0 */
long ru_minflt; /* any page faults not requiring I/O */
long ru_majflt; /* any page faults requiring I/O */
long ru_nswap; /* swaps */
long ru_inblock; /* block input operations */
long ru_oublock; /* block output operations */
long ru_msgsnd; /* messages sent */
long ru_msgrcv; /* messages received */
long ru_nsignals; /* signals received */
long ru_nvcsw; /* voluntary context switches */
long ru_nivcsw; /* involuntary ” */
#define ru_last ru_nivcsw
};

#include <unistd.h> // 错误返回　-1 成功无返回
int execl(const char *__path, const char *__arg, ...);
int execv(const char *__path, char *const *__argv);
int execle(const char *__path, const char *__arg, ...);
int execve(const char *__path, char *const *__argv, char *const *__envp)
int execlp(const char *__file, const char *__arg, ...)
int execvp(const char *__file, char *const *__argv);
int fexecve(int __fd, char *const *__argv, char *const *__envp)
// l == list , v = vector
//例子
execl("/bin/ls","-l","-a","/home",(char*)0);

char * exec_arg[5];
exec_arg[0] = "ls";
exec_arg[1] = "-l";
exec_arg[2] = "-a";
exec_arg[3] = "/home/";
exec_arg[4] = (char *)0;
execv("/bin/ls",exec_arg);

char * exec1[] = {"ls","-l","-a","/home",(char *)0};
printf("%d",execv("/bin/ls",exec1));

char * argv[]={"ls","-al","/etc/passwd",(char *)0};
char * envp[]={"PATH=/bin",0}
execve("/bin/ls",argv,envp);

// 新进程继承调用进程的属性 P201

#include <unistd.h>
int setuid(__uid_t __uid) // 设置实际用户id 和有效用户 id
int setuid(__gid_t __gid)
// 实际用户ID和实际用户组ID：标识我是谁。
// 有效用户ID和有效用户组ID：进程用来决定我们对资源的访问权限。
// 系统通过进程的有效用户ID和有效用户组ID来决定进程对系统资源的访问权限。
// 实际用户 id 要有超级权限

#include <unistd.h>
int setreuid(__uid_t __ruid, __uid_t __euid)
int setregid(__gid_t __rgid, __gid_t __egid)
// 交换实际用户 id 和有效用户 id，参数为-1表示不修改相应部分

int seteuid(__uid_t __uid)
int setegid(__gid_t __gid)
// 修改有效用户　id 和有效组 id

#include <stdlib.h>
int system(const char *__command)

//进程会计
#include <sys/acct.h>

#include <unistd.h>
char * getlogin(void)
// 如果调用此函数的进程没有链接到用户登录所用的终端，函数将会失败
int nice(int __inc) // 进程调度优先值，参数范围在0 - 2*NZERO-1 sysconf(_SC_NZERO) 获得 NZERO 的数值，数值越小优先级越高

#include <sys/resource.h>
int getpriority(__priority_which_t __which, id_t __who)
int setpriority(__priority_which_t __which, id_t __who, int __prio)
// which 有　PRIO_PROCESS PRIO_PGRP PRIO_USER 进程　进程组　用户id
// who 为 0 时，表示调用进程、进程组、用户，(PRIO_USER,0) 返回调用进程的实际用户id

// 进程时间
#include <sys/times.h>
clock_t times(struct tms *__buffer) // 返回流逝的墙上时钟时间（以时钟滴答数为单位）sysconf(_SC_CLK_TCK); 获得具体数值

struct tms{
       clock_t  tms_utime;   /* user cpu time */
       clock_t  tms_stime;   /* system cpu time */
       clock_t  tms_cutime;  /* user cpu time of children */
       clock_t  tms_cstime;  /* system cpu time of children */
 };

// 墙上时钟时间 流逝的时间
// 用户CPU时间  进程花在执行用户模式(非内核模式)代码上的时间总量
// 系统CPU时间  花在执行内核代码上的时间总量
```
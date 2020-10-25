---
layout: page
title:  第十章 信号
date: 2017-09-25 20:18 +0800
update: 2021-11-24 20:18 +0800
---

信号相关

```cpp
#include <signal.h>

__sighandler_t signal(int __sig, __sighandler_t __handler);
```

这里的 ```__sighandler_t```　是指向函数的指针，只有一个整型参数且无返回值

第二个参数可以是SIG_IGN SIG_DFL(忽略 和 采取默认动作)SIGKILL SIGSTOP 不能忽略

SIG_ERR 错误　子进程继承父进程的信号处理方式


一个可重入的函数 简单来说就是可以被中断的函数 P262有具体列表
在信号处理函数里调用非可重入函数　结果是未知的。

执行信号的处理动作称为信号递达（Delivery），信号从产生到递达之间的状态，称为信号未决（Pending）。进程可以选择阻塞（Block）某个信号。被阻塞的信号产生时将保持在未决状态，直到进程解除对此信号的阻塞，才执行递达的动作。

```cpp
#include <signal.h>

int kill(__pid_t __pid, int __sig)
int raise(int __sig)
raise(signo) == kill(getpid(),signo)
```
kill 函数第一个参数的含义

```> 0```　特定进程

```== 0```　同一进程组

```< 0```　发送给进程组id 为绝对值的

```== -1``` 发送给所有有权限发送的进程

```cpp
#include <unistd.h>

unsigned int alarm(unsigned int __seconds)
int pause(void)
```

alarm 定时产生SIGALRM　信号，返回值是0或者之前设置的剩余时间

```cpp
#include <unistd.h>

int sigemptyset(sigset_t *__set)　//清除所有信号
int sigfillset(sigset_t *__set) // 包含所有信号
int sigaddset(sigset_t *__set, int __signo)
int sigdelset(sigset_t *__set, int __signo)
int sigismember(const sigset_t *__set, int __signo)// 真１假０
```

---

```cpp
#include <signal.h>

int sigprocmask(int __how, const sigset_t *__restrict __set, sigset_t *__restrict __oset)
int sigpending(sigset_t *__set)
int sigaction(int __sig, const struct sigaction *__restrict __act, struct sigaction *__restrict __oact)

struct sigaction {
    void (*sa_handler)(int);
    void (*sa_sigaction)(int, siginfo_t *, void *);
    sigset_t sa_mask;
    int sa_flags;
    void (*sa_restorer)(void);
}
// sig 参见P279表
```

信号屏蔽集内的信号的处理方式，单线程用 how，可选项有

SIG_BLOCK //加入信号到进程屏蔽。

SIG_UNBLOCK //从进程屏蔽里将信号删除。

SIG_SETMASK //将set的值设定为新的进程屏蔽。

oset 保存原先的信号集

sigpending 产生但为处理的信号，称为未决

```cpp
// 如果设置了SA_SIGINFO 可以这样自定义信号处理函数
void hander(int signo,siginfo_t * info,void * context)
siginfo_t {
    int      si_signo;  /* Signal number */
    int      si_errno;  /* An errno value */
    int      si_code;   /* Signal code */
    pid_t    si_pid;    /* Sending process ID */
    uid_t    si_uid;    /* Real user ID of sending process */
    int      si_status; /* Exit value or signal */
    clock_t  si_utime;  /* User time consumed */
    clock_t  si_stime;  /* System time consumed */
    sigval_t si_value;  /* Signal value */
    int      si_int;    /* POSIX.1b signal */
    void *   si_ptr;    /* POSIX.1b signal */
    void *   si_addr;   /* Memory location which caused fault */
    int      si_band;   /* Band event */
    int      si_fd;     /* File descriptor */
}

//第三个参数能强制转换称 ucontext_t 类型【疑问】
```

```cpp
#include <setjmp.h>

int sigsetjmp(sigjmp_buf env, int savemask) // 直接调用返回0　从siglongjmp 返回非零
void siglongjmp(sigjmenv, int　val)
```

---

```cpp
#include <signal.h>

int sigsuspend(const sigset_t *__set)

#include <stdlib.h>

void abort(void)
```
恢复信号屏蔽字，再使进程休眠。sigsuspend 返回-1 errno==EINTR
system() 返回值是shell 的状态，而非程序的返回值

```cpp
#include <unistd.h>

unsigned int sleep(unsigned int __seconds)
```

sleep 返回０或未休眠完的秒数，调用者被挂起直到在时间到了或者捕捉到一个信号并处理完返回

```cpp
#include <time.h>

int nanosleep(const struct timespec *__requested_time, struct timespec *__remaining)
int clock_nanosleep(clockid_t __clock_id, int __flags, const struct timespec *__req, struct timespec *__rem)
```

nanosleep 参数为需要休眠的时间、未休眠的时间

clock_nanosleep 正常返回0 错误返回错误码，flags 为0相对时间　TIMER_ABSTIME为绝对



------

附录 P251 信号的类型 附带各种信号定义：
在终端使用```kill -l```命令可以显示所有的信号。

1) SIGHUP 2) SIGINT 3) SIGQUIT 4) SIGILL

5) SIGTRAP 6) SIGABRT 7) SIGBUS 8) SIGFPE

9) SIGKILL 10) SIGUSR1 11) SIGSEGV 12) SIGUSR2

13) SIGPIPE 14) SIGALRM 15) SIGTERM 16) SIGSTKFLT

17) SIGCHLD 18) SIGCONT 19) SIGSTOP 20) SIGTSTP

21) SIGTTIN 22) SIGTTOU 23) SIGURG 24) SIGXCPU

25) SIGXFSZ 26) SIGVTALRM 27) SIGPROF 28) SIGWINCH

29) SIGIO 30) SIGPWR 31) SIGSYS 34) SIGRTMIN

35) SIGRTMIN+1 36) SIGRTMIN+2 37) SIGRTMIN+3 38) SIGRTMIN+4

39) SIGRTMIN+5 40) SIGRTMIN+6 41) SIGRTMIN+7 42) SIGRTMIN+8

43) SIGRTMIN+9 44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12

47) SIGRTMIN+13 48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14

51) SIGRTMAX-13 52) SIGRTMAX-12 53) SIGRTMAX-11 54) SIGRTMAX-10

55) SIGRTMAX-9 56) SIGRTMAX-8 57) SIGRTMAX-7 58) SIGRTMAX-6

59) SIGRTMAX-5 60) SIGRTMAX-4 61) SIGRTMAX-3 62) SIGRTMAX-2

63) SIGRTMAX-1 64) SIGRTMAX

其中前面31个信号为不可靠信号(非实时的，可能会出现信号的丢失)，后面的信号为可靠信号(实时的real_time,对信号排队，不会丢失)。

1) SIGHUP (挂起) 当运行进程的用户注销时通知该进程，使进程终止


2) SIGINT (中断) 当用户按下时,通知前台进程组终止进程

3) SIGQUIT (退出) 用户按下或时通知进程，使进程终止

4) SIGILL (非法指令) 执行了非法指令，如可执行文件本身出现错误、试图执行数据段、堆栈溢出

5) SIGTRAP 由断点指令或其它trap指令产生. 由debugger使用

6) SIGABRT (异常中止) 调用abort函数生成的信号

7) SIGBUS 非法地址, 包括内存地址对齐(alignment)出错. eg: 访问一个四个字长的整数, 但其地址不是4的倍数.

8) SIGFPE (算术异常) 发生致命算术运算错误,包括浮点运算错误、溢出及除数为0.

9) SIGKILL (确认杀死) 当用户通过kill -9命令向进程发送信号时，可靠的终止进程

10) SIGUSR1 用户使用

11) SIGSEGV (段越界) 当进程尝试访问不属于自己的内存空间导致内存错误时，终止进程

12) SIGUSR2 用户使用

13) SIGPIPE 写至无读进程的管道, 或者Socket通信SOCT_STREAM的读进程已经终止，而再写入。

14) SIGALRM (超时) alarm函数使用该信号，时钟定时器超时响应

15) SIGTERM (软中断) 使用不带参数的kill命令时终止进程

17) SIGCHLD (子进程结束) 当子进程终止时通知父进程

18) SIGCONT (暂停进程继续) 让一个停止(stopped)的进程继续执行. 本信号不能被阻塞.

19) SIGSTOP (停止) 作业控制信号,暂停停止(stopped)进程的执行. 本信号不能被阻塞, 处理或忽略.

20) SIGTSTP (暂停/停止) 交互式停止信号, Ctrl-Z 发出这个信号

21) SIGTTIN 当后台作业要从用户终端读数据时, 终端驱动程序产生SIGTTIN信号

22) SIGTTOU 当后台作业要往用户终端写数据时, 终端驱动程序产生SIGTTOU信号

23) SIGURG 有"紧急"数据或网络上带外数据到达socket时产生.

24) SIGXCPU 超过CPU时间资源限制. 这个限制可以由getrlimit/setrlimit来读取/改变。

25) SIGXFSZ 当进程企图扩大文件以至于超过文件大小资源限制。

26) SIGVTALRM 虚拟时钟信号. 类似于SIGALRM, 但是计算的是该进程占用的CPU时间.

27) SIGPROF (梗概时间超时) setitimer(2)函数设置的梗概统计间隔计时器(profiling interval timer)

28) SIGWINCH 窗口大小改变时发出.

29) SIGIO(异步I/O) 文件描述符准备就绪, 可以开始进行输入/输出操作.

30) SIGPWR 电源失效/重启动

31) SIGSYS 非法的系统调用。

在以上列出的信号中，

程序不可捕获、阻塞或忽略的信号有：SIGKILL,SIGSTOP

不能恢复至默认动作的信号有：SIGILL,SIGTRAP

默认会导致进程流产的信号有：SIGABRT,SIGBUS,SIGFPE,SIGILL,SIGIOT,SIGQUIT,SIGSEGV,SIGTRAP,SIGXCPU,SIGXFSZ

默认会导致进程退出的信号有：SIGALRM,SIGHUP,SIGINT,SIGKILL,SIGPIPE,SIGPOLL,SIGPROF,SIGSYS,SIGTERM,SIGUSR1,SIGUSR2,SIGVTALRM

默认会导致进程停止的信号有：SIGSTOP,SIGTSTP,SIGTTIN,SIGTTOU

默认进程忽略的信号有：SIGCHLD,SIGPWR,SIGURG,SIGWINCH
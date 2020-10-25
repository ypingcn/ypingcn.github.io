---
layout: page
title:  第九章 进程关系
update: 2017-09-25 20:18 +0800
---

```cpp
#include <unistd.h>
pid _t getpgrp(void) // 获得进程组 id == getpgid(0)
int setpgid(__pid_t __pid, __pid_t __pgid) // pid 是0 则使用调用者的进程id
pid_t setsid(void) // 建立一个新的会话，返回进程组id
pid_t getsid(pid_t pid) // 返回回话首进程的进程组id
pid_t tcgetpgrp(int __fd) // 获取前台进程组id 出错-1
pid_t tcsetpgrp(int __fd, __pid_t __pgrp_id)

//作业控制
```
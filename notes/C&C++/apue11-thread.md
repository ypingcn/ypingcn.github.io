---
layout: page
title:  第十一章 线程
update: 2017-09-25 20:18 +0800
---

```cpp
#include <pthread.h>
int pthread_equal(pthread_t __thread1, pthread_t __thread2)
pthread_t pthread_self() 
// 返回线程本身
int pthread_create(pthread_t *restrict __newthread, const pthread_attr_t *restrict __attr, void *(*__start_routine)(void *), void *restrict __arg) 
//进程号、进程属性【NULL 后面讲】、开始的函数、函数参数
void pthread_exit(void *__retval)
// 参数返回值
int pthread_join(pthread_t __th, void **__thread_return)
// 获取返回值
int pthread_cancel(pthread_t __th)
// 取消进程的其他线程，成功0 ,反之是错误编号
void pthread_cleanup_push(routine, arg)
//安排退出时需要调用的函数
void pthread_cleanup_pop(int )
//0作为参数可用

// 互斥量
int pthread_mutex_init(pthread_mutex_t *__mutex, const pthread_mutexattr_t *__mutexattr)
// 第二个参数使用NULL的默认参数，也可以直接赋值　PTHREAD_MUTEX_INITIALIZER
int pthread_mutex_init(pthread_mutex_t *__mutex, const pthread_mutexattr_t *__mutexattr)
// 销毁互斥量
int pthread_mutex_lock(pthread_mutex_t *__mutex)
int pthread_mutex_trylock(pthread_mutex_t *__mutex)
int pthread_mutex_unlock(pthread_mutex_t *__mutex)
int pthread_mutex_timedlock(pthread_mutex_t *restrict mutex,const struct timespec *restrict tsptr);
//达到指定时间不加锁互斥量，并返回ETIMEOUT

// 读写锁
int pthread_rwlock_init(pthread_rwlock_t *rwlock, const pthread_rwlockattr_t *attr); //读写锁
int pthread_rwlock_destory(pthread_rwlock_t * rwlock)
int pthread_rdlock(pthread_rwlock_t * rwlock)
int pthread_wrlock(pthread_rwlock_t * rwlock)
int pthread_unlock(pthread_rwlock_t * rwlock)
int pthread_rwlock_timedrdlock(pthread_rwlock_t * restrict rwlock,const struct timespec * restrict tsptr)
// 带超时的读写锁
int pthread_rwlock_timedwlock(pthread_rwlock_t * restrict rwlock,const struct timespec * restrict tsptr)

// 条件变量
int pthread_cond_init(pthread_cond_t *cv,const pthread_condattr_t *cattr);
// 初始化条件变量
int pthread_cond_destory(pthread_cond_t * cond)
int pthread_cond_wait(pthread_cond_t *restrict __cond, pthread_mutex_t *restrict __mutex)
int pthread_cond_timedwait(pthread_cond_t *restrict __cond, pthread_mutex_t *restrict __mutex, const struct timespec *restrict __abstime)
int pthread_cond_signal(pthread_cond_t *__cond)
int pthread_cond_broadcast(pthread_cond_t *__cond)

//自旋锁　线程不希望在重新调度上花费太多的时间
int pthread_spin_init(pthread_spinlock_t * lock,int pshared)
// 第二个参数　PTHREAD_PROCESS_PRIVATE　只能被初始化该锁的进程访问　PTHREAD_PROCESS_SHARED　用于同步该进程和其他进程中的线程
int pthread_spin_destory(pthread_spinlock_t * lock)
int pthread_spin_lock(pthread_spinlock_t * lock)
int pthread_spin_trylock(pthread_spinlock_t * lock)
int pthread_spin_unlock(pthread_spinlock_t * lock)

// 屏障　允许所有线程等待直到所有合作的线程都达到某一点　
//【http://blog.csdn.net/qq405180763/article/details/23919191】
//【在init时指定n+1个等待，其中n是线程数。而在每个线程执行函数的首部调用wait()。这样100个pthread_create()结束后所有线程都停下来等待最后一个wait()函数被调用。这个wait()由主进程在它觉得合适的时候调用就好。最后这个wait()就是鸣响的起跑枪。】
int pthread_barrier_init(pthread_barrier_t *restrict barrier, const pthread_barrierattr_t *restrict attr, unsigned count);
// 等待的线程数
int pthread_barrier_wait(pthread_barrier_t *barrier);
int pthread_barrier_destroy(pthread_barrier_t *barrier);
```
---
layout: page
title:  第五章 标准IO库
update: 2017-09-25 20:18 +0800
---

```cpp
#include <stdio.h>
void setbuf(FILE *__restrict __stream, char *__restrict __buf)
//buf　指向长度为BUFSIZ 的缓冲区
int setvbuf(FILE *__restrict __stream, char *__restrict __buf, int __modes, size_t __n)
// __modes 参数有：_IOFBF _IOLBF _IONBF 全缓冲　行缓冲　不带缓冲
// 带缓冲而buf 为 NULL ，则会自动分配合适长度缓冲区。P118

#include <stdio.h>
int fflush(FILE *__stream)
// 参数为空则刷新所有输出流，正确返回0　错误返回　EOF
FILE * fopen(const char *__restrict __filename, const char *__restrict __modes)
FILE * freopen(const char *__restrict __filename, const char *__restrict __modes, FILE *__restrict __stream)
FILE * fdopen(int __fd, const char *__modes)
//__modes 有 r w a , r+ w+ a+,读、写、追加，w 和 w+ 会截断到0
int fclose(FILE *__stream) 
//正确返回0 错误为EOF

#include <stdio.h> 
// 返回下一个字符，文件尾或出错则EOF
int getc(FILE *__stream)　// 宏
int fgetc(FILE *__stream) // 函数
int getchar(void) == getc(stdin)
int ferror(FILE *__stream)　//判断是出错还是文件尾
int feof(FILE *__stream)
void clearerr(FILE *__stream) 
// 清除出错标志和文件结束标志
int ungetc(int __c, FILE *__stream)
// 将c压回流中，成功返回c错误EOF
int putc(int __c, FILE *__stream) //　宏
int fputc(int __c, FILE *__stream) //　函数
int putchar(int __c) == putc(int __c,stdin)

char fgets(char *__restrict __s, int __n, FILE *__restrict __stream)
// 保留换行
char gets(char *__s) // 不推荐，删除换行
int fputs(const char *__restrict __s, FILE *__restrict __stream)
// 成功非负，错误EOF
int puts(const char *__s)
// 成功非负，错误EOF,添加换行

//使用fgets fputs 都必须自己处理换行符

#include <stdio.h>
// 都返回读或者写的对象数，在不同系统之间可能无法使用
size_t fread(void *__restrict __ptr, size_t __size, size_t __n, FILE *__restrict __stream)
// size 为每个元素的长度(sizeof(类型名)等) n 为要写的元素个数
size_t fwrite(const void *__restrict __ptr, size_t __size, size_t __n, FILE *__restrict __s)

#include <stdio.h>
long ftell(FILE *__stream);
//当前偏移位置，错误返回-1L
off_t ftello(FILE *__stream)
int fseek(FILE *__stream, long __off, int __whence)
int fseeko(FILE *__stream, __off_t __off, int __whence)
//whence - SEEK_SET SEEK_CUR SEEK_END 开始位置　当前位置　结束位置
void rewind(FILE *__stream)
// 返回文件头　== fseek(stream，0L，SEEK_SET)。

#include <stdio.h> // 成功0　错误非0 , fpos_t?
int fgetpos(FILE *__restrict __stream, fpos_t *__restrict __pos)
int fsetpos(FILE *__stream, const fpos_t *__pos)

#include <stdio.h>
int printf(const char *__restrict __format, ...);
int fprintf(FILE *__restrict __stream, const char *__restrict __format, ...)
int dprintf(int __fd, const char *__restrict __fmt, ...)
// 前三个成功返回字符数，错误为负值
int sprintf(char *__restrict __s, const char *__restrict __format, ...)
// 缓冲区大小问题，考虑下一个？
int snprintf(char *__restrict __s, size_t __maxlen, const char *__restrict __format, ...)
// 后面四个的 format 等参数参照　printf

#include <stdio.h>
#include <stdarg.h> //?????????????
int vprintf(const char *__restrict __format, __va_list_tag *__arg);
int vfprintf(FILE *__restrict __s, const char *__restrict __format, __va_list_tag *__arg);
int vdprintf(int __fd, const char *__restrict __fmt, __va_list_tag *__arg);
int vsprintf(char *__restrict __s, const char *__restrict __format, __va_list_tag *__arg)
int vsnprintf(char *__restrict __s, size_t __maxlen, const char *__restrict __format, __va_list_tag *__arg);
//[vprintf 和 vsnpintf 的用法_越来越好_新浪博客]
//(http://blog.sina.com.cn/s/blog_a9303fd90101d6l9.html)

#include <stdio.h>
int　scanf(const char *__restrict __format, ...);
int fscanf(FILE *__restrict __stream, const char *__restrict __format, ...)
int sscanf(const char *__restrict __s, const char *__restrict __format, ...)

#include <stdio.h>
#include <stdarg.h>
int vscanf(const char *__restrict __format, __va_list_tag *__arg)
int vsscanf(const char *__restrict __s, const char *__restrict __format, __va_list_tag *__arg)
int vfscanf(FILE *__restrict __s, const char *__restrict __format, __va_list_tag *__arg)

#include <stdio.h>
int fileno(FILE *__stream)
// 返回文件描述符
char * tmpnam(char *__s)
// 【不推荐使用】临时文件,参数可为nullptr，不为空则指向至少　L_tmpnam 个字符的数组
FILE * tmpfile(void);

#include <stdlib.h>
char * mkdtemp(char *__template)
//返回指向目录的指针，错误为null
int mkstemp(char *__template)
//返回文件描述符，错误为 -1
//参数要提前声明赋值好，最后六位要是大写的X,例如
char name[] = "/tmp/testXXXXXX"
mkdtemp(name);

// 内存流　？？？？？？
#include <stdio.h>
FILE * fmemopen(void *__s, size_t __len, const char *__modes)
FILE * open_memstream(char **__bufloc, size_t *__sizeloc)
// 面向宽字节
#include <wchar.h>
open_wmemstream(wchar_t **__bufloc, size_t *__sizeloc)
//[创建内存流：fmemopen()函数详解 - 夜夜夜夜 - CSDN博客]
//(http://blog.csdn.net/drdairen/article/details/51912828)
```
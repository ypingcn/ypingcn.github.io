---
layout: page
title:  第五章 标准IO库
date: 2017-09-25 20:18 +0800
update: 2021-11-20 21:45 +0800
---

```cpp
#include <stdio.h>

void setbuf(FILE *__restrict __stream, char *__restrict __buf)
int setvbuf(FILE *__restrict __stream, char *__restrict __buf, int __modes, size_t __n)
```
buf 指向长度为BUFSIZ 的缓冲区

```__modes``` 参数有：_IOFBF _IOLBF _IONBF 全缓冲　行缓冲　不带缓冲

带缓冲而buf 为 NULL ，则会自动分配合适长度缓冲区。P118

```cpp
#include <stdio.h>

int fflush(FILE *__stream)
FILE * fopen(const char *__restrict __filename, const char *__restrict __modes)
FILE * freopen(const char *__restrict __filename, const char *__restrict __modes, FILE *__restrict __stream)
FILE * fdopen(int __fd, const char *__modes)
int fclose(FILE *__stream) 
```

fflush 参数为空则刷新所有输出流，正确返回 0 错误返回 EOF

```__modes``` 有 r w a , r+ w+ a+,读、写、追加，w 和 w+ 会截断到0

fclose 正确返回0 错误为EOF

```cpp
#include <stdio.h> 

int getc(FILE *__stream)　// 宏
int fgetc(FILE *__stream) // 函数
int getchar(void) == getc(stdin)
int ferror(FILE *__stream)　
int feof(FILE *__stream)
void clearerr(FILE *__stream) 
int ungetc(int __c, FILE *__stream)
int putc(int __c, FILE *__stream) //　宏
int fputc(int __c, FILE *__stream) //　函数
int putchar(int __c) == putc(int __c,stdin)
char fgets(char *__restrict __s, int __n, FILE *__restrict __stream)
char gets(char *__s) // 不推荐，删除换行
int fputs(const char *__restrict __s, FILE *__restrict __stream)
int puts(const char *__s)
// 成功非负，错误EOF,添加换行
```

getc返回下一个字符，文件尾或出错则EOF

ferror 判断是出错还是文件尾

clearerr 清除出错标志和文件结束标志

ugetc 将c压回流中，成功返回c错误EOF

fgets 保留换行

fputs 成功非负，错误EOF

使用fgets fputs 都必须自己处理换行符

```cpp
#include <stdio.h>

size_t fread(void *__restrict __ptr, size_t __size, size_t __n, FILE *__restrict __stream)
size_t fwrite(const void *__restrict __ptr, size_t __size, size_t __n, FILE *__restrict __s)
```

fread fwirte 都返回读或者写的对象数，在不同系统之间可能无法使用。size 为每个元素的长度(sizeof(类型名)等) n 为要写的元素个数。

```cpp
#include <stdio.h>

long ftell(FILE *__stream);
off_t ftello(FILE *__stream)
int fseek(FILE *__stream, long __off, int __whence)
int fseeko(FILE *__stream, __off_t __off, int __whence)
void rewind(FILE *__stream)
```
ftell 当前偏移位置，错误返回-1L

fseeko 中的 whence 的选项有 SEEK_SET SEEK_CUR SEEK_END，分别代表 开始位置　当前位置　结束位置

rewind 返回文件头　== fseek(stream，0L，SEEK_SET)。

```cpp
#include <stdio.h>

int fgetpos(FILE *__restrict __stream, fpos_t *__restrict __pos)
int fsetpos(FILE *__stream, const fpos_t *__pos)
```

成功0　错误非0 , fpos_t 是文件写入的位置。

```cpp
#include <stdio.h>

int printf(const char *__restrict __format, ...);
int fprintf(FILE *__restrict __stream, const char *__restrict __format, ...)
int dprintf(int __fd, const char *__restrict __fmt, ...)
int sprintf(char *__restrict __s, const char *__restrict __format, ...)
int snprintf(char *__restrict __s, size_t __maxlen, const char *__restrict __format, ...)
```

printf fprintf dprintf 前三个成功返回字符数，错误为负值。
snprintf 后面第四个的 format 等参数参照　printf

```cpp
#include <stdio.h>
#include <stdarg.h> //?????????????

int vprintf(const char *__restrict __format, __va_list_tag *__arg);
int vfprintf(FILE *__restrict __s, const char *__restrict __format, __va_list_tag *__arg);
int vdprintf(int __fd, const char *__restrict __fmt, __va_list_tag *__arg);
int vsprintf(char *__restrict __s, const char *__restrict __format, __va_list_tag *__arg)
int vsnprintf(char *__restrict __s, size_t __maxlen, const char *__restrict __format, __va_list_tag *__arg);
```

格式打印输出打印

```cpp
#include <stdio.h>

int　scanf(const char *__restrict __format, ...);
int fscanf(FILE *__restrict __stream, const char *__restrict __format, ...)
int sscanf(const char *__restrict __s, const char *__restrict __format, ...)
```

格式输入

```cpp
#include <stdio.h>
#include <stdarg.h>

int vscanf(const char *__restrict __format, __va_list_tag *__arg)
int vsscanf(const char *__restrict __s, const char *__restrict __format, __va_list_tag *__arg)
int vfscanf(FILE *__restrict __s, const char *__restrict __format, __va_list_tag *__arg)
```
输入


```cpp
#include <stdio.h>

int fileno(FILE *__stream)
char * tmpnam(char *__s)
// 【不推荐使用】临时文件,参数可为nullptr，不为空则指向至少　L_tmpnam 个字符的数组
FILE * tmpfile(void);
```

fileno 返回文件描述符

```cpp
#include <stdlib.h>

char * mkdtemp(char *__template)
int mkstemp(char *__template)

char name[] = "/tmp/testXXXXXX"
mkdtemp(name);
```

mkdtemp 返回指向目录的指针，错误为null

mkstemp 返回文件描述符，错误为 -1。参数要提前声明赋值好，最后六位要是大写的X,例如

```cpp
// 内存流　？？？？？？
#include <stdio.h>

FILE * fmemopen(void *__s, size_t __len, const char *__modes)
FILE * open_memstream(char **__bufloc, size_t *__sizeloc)
// 面向宽字节

#include <wchar.h>

open_wmemstream(wchar_t **__bufloc, size_t *__sizeloc)
```
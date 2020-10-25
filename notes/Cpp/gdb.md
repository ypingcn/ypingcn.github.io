---
layout: page
title:  GDB 调试
update: 2017-09-25 19:18 +0800
---

要先加``` -g ```生成 可执行文件，再``` gdb a.out ```

| 命令                        | 描述                                |
| :------------------------ | :-------------------------------- |
| start                     | 开始，在main()第一行语句等待                 |
| next (n)                  | 下一语句                              |
| step (s)                  | 下一语句，若是函数则进入函数                    |
| print (p)                 | 打印表达式的值，或者修改（set var）             |
| backtrace(bt)             | 查看各级函数调用                          |
| list (l)                  | 列出源代码                             |
| list [num]                | 从num行开始列出源代码，默认显示10行              |
| list [function-name]      | 从 function-name 开始列出源代码           |
| quit (q)                  | 退出                                |
| info (i) locals           | 查看局部变量的值                          |
| finish                    | 运行到当前函数返回                         |
| display                   | 显示某个变量的值                          |
| undisplay [num]           | 取消显示                              |
| break (b) [num]           | 设置断点                              |
| break [function-name]     | 在函数开头设置断点                         |
| break ... if ...          | 条件断点                              |
| continue (c)              | 连续运行程序                            |
| delete breakpoints [num]  | 删除断点                              |
| disable breakpoints [num] | 禁用断点                              |
| enable [num]              | 启用断点                              |
| info(i) breakpoints       | 显示断点信息                            |
| run (r)                   | 重新开始运行                            |
| watch                     | 设置观察点（显示改变前后的值）                   |
| info (i) watchpoints      | 显示观察点信息                           |
| x                         | 从某个位置打印信息（x/7b b表示每个字节一组，7表示打印7组） |




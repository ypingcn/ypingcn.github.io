---
layout: page
title:  Markdwon + LaTex 表达数学式子
description: Markdown 撰写数学式子（字符、省略号、括号、分隔符、箭头、插入文字、上下标与希腊字母、标准函数、分数、根号、导数、偏导数、积分、极限、求和、向量、排列组合等）的方法
date: 2016-11-10 08:20 +0800
update: 2022-06-03 15:19 +0800
---

<a href="/notes/Markdown/basic/" style="font-weight: bold">基础的 Markdown 语法</a> 中无法满足数学式子的表达需求，此时可以借助 Latex 语法完成。在 Markdown 中由前后两个 ``` $$ ```包围的部分可以写 LaTex 源代码（最新版 Typora 已经支持）如下

```Markdown
$$
LaTex code
$$
```
 ------

## 速查

Markdown 中 Latex 基本符号速查表

|  显示字符  |  输入字符  |  显示字符  |  输入字符  |   显示字符  |  输入字符  |
|   :---:   |   :---:   |   :---:   |   :---:   |   :---:   |   :---:   |
| ``` # ``` | ``` \# ``` |  ``` $ ``` | ``` \$ ``` | ``` % ``` | ``` \% ``` |
| ``` & ``` | ``` \& ``` | ``` ~ ``` | ``` \~ ``` |``` _ ``` | ``` \_ ``` |
| ``` ^ ``` | ``` \^ ``` | ``` \ ``` | ``` \\ ``` | ``` { ``` | ``` \{ ``` |
| ``` } ``` | ``` \} ``` | | | |  |
| ≤ | ``` \le ``` | ≥ | ``` \ge ``` | ≡ | ``` \equiv ``` |
| ≠ | ``` \ne ``` |
| 文本底线对齐的省略号 | ``` \ldots ``` | 文本中对齐的省略号 | ``` \cdots ``` |
| 圆括号 | ``` () ``` | 方括号 | ``` [] ``` | 竖线 | ``` | ``` | 
| 花括号 | ``` \{\} ``` | 双竖线 | ``` \| ``` |
| 长圆括号 | ```\left(  \right)``` | 长方括号 | ```\left[  \right]``` | 长花括号 | ```\left\{  \right\}``` |
| 换行 | ``` \\ ``` | 空格 | ``` \space ``` |
| ← | ``` \leftarrow ``` | → | ``` \rightarrow ``` |  文字 | ``` \mbox{ } ``` | 

 ------

## 字符相关

### **字符**

插入```  # $ % & ~ _ ^ \ { }  ```需多加```  \  ```符号（类似于 C 语言中的转义字符），其他可以直接插入。

``` \\ ``` 对应换行符 ，``` \space ``` 对应空格。

小于等于、大于等于、恒等于、不等于分别为 ``` \le \ge \equiv \ne ``` （ l 意为 less ，e 意为 equal ，g 意为 greater ）

### **省略号**

``` \ldots \cdots ``` 分别表示与文本底线对齐和与文本中对齐的省略号。（l 意为 line ，c 意为 center ）

### **括号**

圆括号、方括号和竖线直接输入，花括号前需添加 ``` \ ```  ，双竖线对应``` \| ``` 。

长圆括号、长方括号、长花括号对应``` \left(  \right) ``` ```\left[  \right] ``` ``` \left\{  \right\}  ``` 

### **箭头**

左右箭头对应 ``` \leftarrow \rightarrow ``` 

### **插入文字**

``` \mbox{ } ``` 用于插入文字（显示效果不是斜体字） 。

 ------

## 数学式子    

### **标准函数**

欲输入 ``` sin ``` 时，应用``` \sin(x) ```。

### **分数**

二分之一对于 ``` \frac{1}{2} ```

### **根号**

根号二对应 ``` \sqrt{2} ``` ，开 n 次方为``` \sqrt[n]{expression} ```

### **导数 偏导数**

对 x 导数对应 ``` \mathrm{d}x ```

对 x 的偏导数对应``` \partial x ```

### **积分**

f(x) 对 x 从 a 到 b 的积分 ``` \int_a^b f(x) \mathrm{d}x ``` ， 多重积分则多次输入 ``` \int ``` ，两个符号之间添加 ``` \!\!\! ``` 调整正确的间隔。

### **极限**

x 到正无穷的极限 ``` \lim_{x\to+\infty} ```

### **求和**

1 到 n 的和对应 ``` \sum_{1}^{n} ```

### **向量**

向量 ab 对应 ``` \vec{ab} ```

### **排列组合**

从 n 中选 m 的组合数和排列数为 ``` \mathrm{C}_n^m  \mathrm{A}_n^m  ``` 

[具体内容参见文末参考资料](#1)。

 ------

## 上下标与希腊字母

``` ^  ```表示上标 ``` _ ```表示下标，同时出现上下标时，先上标后下标与先下标后上标的效果相同。

用 ``` \ ``` 加相应的拼写即可，第一个字母大写则显示大写字母，小写则显示小写字母。

| 输入 |  展示| 输入 |  展示|
|  :---:   |   :---:   |:---:   |:---:   |
| \alpha |	α |\beta 	| β| 
| \gamma 	| γ| \Gamma 	| Γ| 
| \theta 	| θ| \Theta 	| Θ|
| \delta 	| δ | \Delta 	| Δ |
| \triangledown|  	▽ |  \epsilon 	| ϵ| 
| \zeta 	| ζ| \eta 	|  η| 
| \kappa 	| κ| \lambda | 	λ| 
| \mu 	| μ| \nu 	| ν| 
| \xi 	| ξ|  \pi 	| π|
| \sigma 	| σ| \tau | 	τ| 
| \upsilon | 	υ|\phi 	|  ϕ
| \omega | 	ω| 

 ------
## 多行的数学公式

例子

```latex
\begin{eqnarray}
\cos 2\theta & = & \cos^2 \theta - \sin^2 \theta \\
& = & 2 \cos^2 \theta - 1.
\end{eqnarray}
```

& 是对齐点，具体例子中表示多行式子在等号之间对齐。

```latex
f(n) =
\begin{cases} 
n+1,  & \mbox{if }n \mbox{ is even} \\
n-1, & \mbox{if }n \mbox{ is odd}
\end{cases}
```

条件定义式。奇数加一，偶数减一。

 ------

## 矩阵

例子

```
\begin{array}{ccc}
a & b & c \\
d & e & f \\
g & h & i 
\end{array}
```
表示 3 x 3 的矩阵，c 表示居中对齐，l 是左对齐，r 是右对齐。

------

参考资料 ：

\#1 <a href="https://zh.wikipedia.org/wiki/Help:%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F" style="color: #0c82ff;"  target="_blank" rel="noopener nofollow">帮助:数学公式 - 维基百科，自由的百科全书</a>

\#2 <a href="https://zh.wikibooks.org/wiki/LaTeX/%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F" style="color: #0c82ff;"  target="_blank" rel="noopener nofollow">LaTeX/数学公式 - 维基教科书，自由的教学读本</a>

---

**更多阅读**

<div class="row">
    <div class="col-lg-8 col-lg-offset-2
    col-md-10 col-md-offset-1
    post-container">
        <ul class="pager">
            <li class="previous">
                <a href="/notes/Markdown/LaTex-math/" target="_blank" data-toggle="tooltip" data-placement="top"
                    title="《Markdwon + LaTex 表达数学式子》">
                    下一篇<br>
                    <span>《Markdwon + LaTex 表达数学式子》</span>
                </a>
            </li>
            <li class="next">
                <a href="/notes/Markdown/basic/" target="_blank" data-toggle="tooltip" data-placement="top"
                    title="《Markdown 基础语法》">
                    下一篇<br>
                    <span>《Markdown 基础语法》</span>
                </a>
            </li>
        </ul>
    </div>
</div>

---
layout: page
title: std::function && std::bind
update: 2017-10-30 21:32 +0800
---

## function

留意加``` -std=c++11 ```

```c++
#include <functional>
#include <iostream>
using namespace std;

function< void (int) > func;// 括号里类型由未来使用时的类型（占位符的类型）决定
void c(int val)
{
	cout<<val<<endl;
}

class cpp
{
public:
	void operator()(int val)
	{
		cout<<val<<endl;
	}
};

int main(int argc, char const *argv[]) {
	func = c;
	func(100);
	cpp obj;
	func = obj;
	func(200);
	return 0;
}
```

## bind

```c++
#include <functional>
#include <iostream>
#include <cstdio>
using namespace std;

void c(int a,int b)
{
	cout<<a<<" % "<<b<<endl;
}

class cpp
{
public:
	void c(int a,int b)
	{
		cout<<a<<" % "<<b<<endl;
	}
	void cc(int a,char b)
	{
		printf("%d %% %c\n",a,b);
	}
};

int main(int argc, char const *argv[]) {
	auto f1 = bind(c,10,std::placeholders::_1);
	//std::placeholders 占位符，std::placeholders::_1 表示第一个参数
	f1(20);// c(10,20)

	cpp obj;
	auto f2 = bind(&cpp::c,obj,std::placeholders::_1,std::placeholders::_2);
	f2(10,20); // c(10,20)

	function< void(int)> f3 = std::bind(&cpp::c, obj, 200, std::placeholders::_1);
	f3(100);
	function< void(char)> f4 = std::bind(&cpp::cc, obj, 200, std::placeholders::_1);
	f4('a');
	function< void(int,char)> f5 = std::bind(&cpp::cc, obj, std::placeholders::_1, std::placeholders::_2);
	f5(666,'e');
	
	return 0;
}
```


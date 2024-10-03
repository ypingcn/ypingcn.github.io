---
layout: page
title:  「代码片段」 bloomfilter
update: 2024-10-03 19:00 +0800
---

「代码片段」 bloomfilter

BloomFilter 判断不存在的 key ，则是 100% 不存在的

判断存在的，不一定完全存在

可以参考阅读redis的布隆过滤器实现

https://github.com/RedisBloom/RedisBloom/blob/master/deps/bloom/bloom.c

```cpp
#include <vector>

#include <string>

#include <sstream>

#include "bits/stdc++.h"

// 1  SDBMHash
inline unsigned int hashfunc0(const char *str)
{
    unsigned int hash = 0;

    while (*str)
    {
        // equivalent to: hash = 65599*hash + (*str++);
        hash = (*str++) + (hash << 6) + (hash << 16) - hash;
    }

    return hash;
}

// 2  RS Hash Function
inline unsigned int hashfunc1(const char *str)
{
    unsigned int b = 378551;
    unsigned int a = 63689;
    unsigned int hash = 0;

    while (*str)
    {
        hash = hash * a + (*str++);
        a *= b;
    }

    return hash;
}

// 3 JS Hash Function
inline unsigned int hashfunc2(const char *str)
{
    unsigned int hash = 1315423911;

    while (*str)
    {
        hash ^= ((hash << 5) + (*str++) + (hash >> 2));
    }

    return hash;
}

// 4 P. J. Weinberger Hash Function
inline unsigned int hashfunc3(const char *str)
{
    unsigned int BitsInUnignedInt = (unsigned int)(sizeof(unsigned int) * 8);
    unsigned int ThreeQuarters = (unsigned int)((BitsInUnignedInt * 3) / 4);
    unsigned int OneEighth = (unsigned int)(BitsInUnignedInt / 8);
    unsigned int HighBits = (unsigned int)(0xFFFFFFFF) << (BitsInUnignedInt - OneEighth);
    unsigned int hash = 0;
    unsigned int test = 0;

    while (*str)
    {
        hash = (hash << OneEighth) + (*str++);

        if ((test = hash & HighBits) != 0)
        {
            hash = ((hash ^ (test >> ThreeQuarters)) & (~HighBits));
        }
    }

    return hash;
}

// 5 ELF Hash Function
inline unsigned int hashfunc4(const char *str)
{
    unsigned int hash = 0;
    unsigned int x = 0;

    while (*str)
    {
        hash = (hash << 4) + (*str++);

        if ((x = hash & 0xF0000000L) != 0)
        {
            hash ^= (x >> 24);
            hash &= ~x;
        }
    }

    return hash;
}

// 常用2
// 6 BKDR Hash Function
inline unsigned int hashfunc5(const char *str)
{
    unsigned int seed = 131; // 31 131 1313 13131 131313 etc..
    unsigned int hash = 0;

    while (*str)
    {
        hash = hash * seed + (*str++);
    }

    return hash;
}

// 7 DJB Hash Function
inline unsigned int hashfunc6(const char *str)
{
    unsigned int hash = 5381;

    while (*str)
    {
        hash += (hash << 5) + (*str++);
    }

    return hash;
}

// 8 AP Hash Function
inline unsigned int hashfunc7(const char *str)
{
    unsigned int hash = 0;
    int i;

    for (i = 0; *str; i++)
    {
        if ((i & 1) == 0)
        {
            hash ^= ((hash << 7) ^ (*str++) ^ (hash >> 3));
        }
        else
        {
            hash ^= (~((hash << 11) ^ (*str++) ^ (hash >> 5)));
        }
    }

    return hash;
}

class BloomKey
{
public:
    unsigned int value[7];
    BloomKey(const char *str)
    {
        value[0] = hashfunc0(str);
        value[1] = hashfunc1(str);
        value[2] = hashfunc2(str);
        value[3] = hashfunc4(str);
        value[4] = hashfunc5(str);
        value[5] = hashfunc6(str);
        value[6] = hashfunc7(str);
    }
};

class Bloomfilter
{
public:
    Bloomfilter(long size = 10 * 1024 * 1024)
        : filter(size), size(size)
    {
    }

    bool exists(const BloomKey &key)
    {
        for (auto v : key.value)
        {
            if (filter[v % size] == 0)
            {
                return false;
            }
        }

        return true;
    }

    void insert(const BloomKey &key)
    {
        for (auto v : key.value)
        {
            filter[v % size] = 1;
        }
    }

    void reset()
    {
        memset(filter.data(), 0, filter.size() * sizeof(char));
    }

protected:
    std::vector<char> filter;
    long size;
};

int main()
{
    Bloomfilter filter;
    filter.insert(BloomKey("HelloWorld"));
    std::cout << (filter.exists(BloomKey("HelloWorld")) ? "Y" : "N") << std::endl;
}

```
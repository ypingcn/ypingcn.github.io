---
layout: page
title:  「代码片段」 bin2hex
update: 2024-10-03 19:00 +0800
---

「代码片段」 bin2hex

```cpp
std::string bin2hex(const std::string &input)
{
    std::string res;
    const char hex[] = "0123456789ABCDEF";
    for (auto sc : input)
    {
        unsigned char c = static_cast<unsigned char>(sc);
        res += hex[c >> 4];
        res += hex[c & 0xf];
    }

    return res;
}
```
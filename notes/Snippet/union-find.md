---
layout: page
title:  「代码片段」 union-find
update: 2024-10-03 19:00 +0800
---

「代码片段」 union-find

并查集

特别是在需要快速判断两个元素是否属于同一个集合以及进行集合合并的场景中表现尤为出色

例题: leetcode 128 最长的连续子序列

```cpp
#include <bits/stdc++.h>

using namespace std;

class UnionFind
{
private:
    vector<int> parent;

public:
    UnionFind(int n) : parent(n)
    {
        for (int i = 0; i < n; ++i)
        {
            parent[i] = i; // 初始化时，每个元素都是其自己的父节点
        }
    }

    int find(int x)
    {
        while (x != parent[x])
        {
            x = parent[x]; // 路径压缩
        }
        return x;
    }

    void unionFind(int x, int y)
    {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY)
        {
            parent[rootX] = rootY; // 将x的根指向y的根
        }
    }
};

int main()
{
    int n = 10; // 假设我们有10个元素
    UnionFind uf(n);

    // 查找操作示例
    cout << "Find(5): " << uf.find(5) << endl; // =5

    // 合并操作示例
    uf.unionFind(1, 3);
    uf.unionFind(2, 4);
    uf.unionFind(3, 5);
    uf.unionFind(2, 5);
    for (int i = 1; i <= 5; i++)
    {
        cout << "Find(" << i << "): " << uf.find(i) << endl; // 都是5
    }

    return 0;
}
```
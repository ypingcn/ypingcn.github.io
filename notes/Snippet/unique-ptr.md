---
layout: page
title:  「代码片段」 unique_ptr
update: 2024-10-03 19:00 +0800
---

「代码片段」 unique_ptr


```cpp
#include <iostream>

template <typename T>
class unique_ptr {
public:
    unique_ptr(T* ptr = nullptr) : ptr(ptr) {}

    ~unique_ptr() {
        delete ptr;
    }

    unique_ptr(unique_ptr&& other) noexcept : ptr(other.ptr) {
        other.ptr = nullptr;
    }

    unique_ptr& operator=(unique_ptr&& other) noexcept {
        if (this!= &other) {
            delete ptr;
            ptr = other.ptr;
            other.ptr = nullptr;
        }
        return *this;
    }

    T& operator*() const {
        return *ptr;
    }

    T* operator->() const {
        return ptr;
    }

    T* release() {
        T* temp = ptr;
        ptr = nullptr;
        return temp;
    }

private:
    T* ptr;
    unique_ptr(const unique_ptr&) = delete;
    unique_ptr& operator=(const unique_ptr&) = delete;
};
```
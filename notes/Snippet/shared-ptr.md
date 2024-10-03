---
layout: page
title:  「代码片段」 shared_ptr
update: 2024-10-03 19:00 +0800
---

「代码片段」 shared_ptr


```cpp

#include <iostream>

template<typename T>
class shared_ptr {
public:
    shared_ptr(T* ptr = nullptr) : ptr(ptr), ref_count(new size_t(1)) {}

    shared_ptr(const shared_ptr& other) : ptr(other.ptr), ref_count(other.ref_count) {
        if (ref_count) ++(*ref_count);
    }

    shared_ptr& operator=(const shared_ptr& other) {
        if (this!= &other) {
            release();
            ptr = other.ptr;
            ref_count = other.ref_count;
            if (ref_count) ++(*ref_count);
        }
        return *this;
    }

    ~shared_ptr() {
        release();
    }

    T& operator*() const { return *ptr; }
    T* operator->() const { return ptr; }

    size_t use_count() const { return ref_count? *ref_count : 0; }

private:
    T* ptr;
    size_t* ref_count;

    void release() {
        if (ref_count && --(*ref_count) == 0) {
            delete ptr;
            delete ref_count;
        }
    }
};
```
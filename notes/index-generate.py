#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os,re
from datetime import datetime

print("--- --- begin --- ---")

header = [
    "---",
    "layout: page",
    "title: 笔记",
    "update: "+datetime.now().strftime("%y-%m-%d 12:00")+" +0800",
    "not_show_copyright: true",
    "not_show_ad: true",
    "---",
    "",
    "个人整理自用的技术向笔记文章，比较零碎所以不用博文的形式更新",
    ""
]

dir = [x for x in os.listdir(".") if os.path.isdir(x)]
index = open("index.md", "w")

for x in header:
    index.write(x + "\n")

for x in sorted(dir):
    index.write("## " + x + "\n\n")
    os.chdir(x)
    file = os.listdir(".")
    for filename in sorted(file):
        if not filename.endswith(".md"):
            continue
        update = re.compile("update: (.*)")
        title = re.compile("title:  (.*)")
        update_str = ""
        title_str = ""
        for line in open(filename, "r"):
            update_result = update.findall(line)
            title_result = title.findall(line)
            if not title_result and not update_result:
                continue
            if title_result:
                title_str = title_result[0]
            if update_result:
                update_str = update_result[0]

        if update_str != "" and title_str != "":
            print(update_str, " ==> ", title_str)
            index.write(
                '<a href="./'
                + x
                + "/"
                + filename[0 : len(filename) - 3]
                + '/" style="color:#0c82ff;">《'
                + title_str
                + "》</a> （最近更新："
                + update_str
                + "）\n\n"
                )
    os.chdir("..")

print("--- --- done --- ---")

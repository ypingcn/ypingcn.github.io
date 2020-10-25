#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os,re
from datetime import datetime

print("--- --- begin --- ---")

header = ["---","","layout: page","title: 笔记","update: "+datetime.now().strftime("%Y-%m-%d")+" +0800","","---","个人整理自用的技术向笔记文章，比较零碎所以不用博文的形式更新"]

dir = [x for x in os.listdir(".") if os.path.isdir(x)]
index = open("index.md","w")

for x in header:
    index.write(x+"\n")
for x in sorted(dir):
    index.write("## "+x+"\n\n")
    os.chdir(x)
    file = os.listdir(".")
    for y in sorted(file):
        if not y.endswith('.md'):
            continue
        pattern = re.compile(u"title:  (.*)")
        for line in open(y,"r"):
            #print(line)
            result = pattern.findall(line)
            if result:
                print(result[0])
                index.write("<a href=\"./"+x+"/"+y[0:len(y)-3]+"\" style=\"color:#0c82ff;\">《"+result[0]+"》</a>\n\n")
    os.chdir("..")
    index.write("\n")

print("--- --- done --- ---")


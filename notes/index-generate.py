#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os,re
from datetime import datetime

print("--- --- begin --- ---")

header = ["---","","layout: page","title: 笔记目录","update: "+datetime.now().strftime("%Y-%m-%d")+" +0800","","---",""]

dir = [x for x in os.listdir(".") if os.path.isdir(x)]
index = open("index.md","w")

for x in header:
    index.write(x+"\n")
for x in dir:
    index.write("## "+x+"\n")
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
                index.write("["+result[0]+"](./"+x+"/"+y[0:len(y)-3]+")"+"\n\n")
    os.chdir("..")
    index.write("\n")

print("--- --- done --- ---")


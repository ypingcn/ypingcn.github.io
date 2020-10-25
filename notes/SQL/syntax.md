---
layout: page
title:  SQL 基础语法
update: 2016-11-19 10:36 +0800 
---

SQL 的基础语法（select/insert/update/delete ...）

参考资料

w3school [SQL教程](http://www.w3school.com.cn/sql/index.asp)

SQL语句大小写不敏感。


## Basic

```
SELECT column FROM table
```

### select

```
SELECT DISTINCT column FROM table

SELECT column FROM table WHERE column operator value

SELECT column FROM table WHERE 1 AND 2 (WHERE 1 OR 2)

SELECT column FROM table ORDER BY column

SELECT column FROM table LIMIT number(MySQL)

SELECT column FROM table WHERE column LIKE pattern (% _ [charlist] [^charlist])

SELECT column FROM table WHERE column IN (value1,value2,...)

SELECT column FROM table WHERE column BETWEEN value1 AND value2

SELECT column FROM table AS alias_name(表的别名)
SELECT column AS alias_name FROM table（列的别名）

SELECT column INTO new_table [IN external_database] FROM old_table
```

### insert

```
INSERT INTO table VALUES (v1.v2...)
INSERT INTO table (column1,column2,...) VALUES (v1,v2,...)
```

### update

```
UPDATE table SET column = new_value WHERE column = value
```

### delete

```
DELETE FROM table WHERE column = value
```

### union

```
SELECT column1 FROM table1 UNION SELECE column2 FROM table2(元素不重复)
SELECT column2 FROM table1 UNION ALL SELECT column2 FROM table2（元素可以重复）
```

### create

```
CREATE DATABASE name
CREATE TABLE name( c1 type,c2 type,c3 type,...)
```

## Join

```
(INNER) JOIN: 如果表中有至少一个匹配，则返回行
LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行
RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行
FULL JOIN: 只要其中一个表中存在匹配，就返回行

SELECT column FROM table1 INNER JOIN table2 ON table1.column = table2.column
SELECT column FROM table1 LEFT JOIN table2 ON table1.column = table2.column 
SELECT column FROM table1 RIGHT JOIN table2 ON table1.column = table2.column 
SELECT column FROM table1 FULL JOIN table2 ON table1.column = table2.column 
```

## Constraint

### not null

```
CREATE TABLE name( c1 type NOT NULL,c2 type,c3 type,...)
```

### unique

```
CREATE TABLE name( c1 type,c2 type,c3 type,... ,UNIQUE(c1) ) (MySQL)
CREATE TABLE name( c1 type,c2,type,c3 type,... ,CONSTRAINT constraint_name UNIQUE(c1,c2) ) (MySQL)
ALTER TABLE table ADD UNIQUE(column)
ALTER TABLE table ADD CONSTRAINT constraint_name UNIQUE(c1,c2)
ALTER TABLE table DROP INDEX constraint_name (MySQL)
```

### primary key

```
CREATE TABLE name( c1 type,c2 type,c3 type,... ,PRIMARY KEY(c1) ) (MySQL)
CREATE TABLE name( c1 type,c2,type,c3 type,... ,CONSTRAINT constraint_name PRIMARY KEY(c1,c2) )  (MySQL)
ALTER TABLE table ADD PRIMARY KEY(column)
ALTER TABLE table ADD CONSTRAINT constraint_name PRIMARY KEY(c1,c2)
ALTER TABLE table DROP PRIMARY KEY(MySQL)
```

### foreign key

```
CREATE TABLE name( c1 type,c2 type,c3 type,... ,FOREIGN KEY(c1) REFERENCE table2(column) ) (MySQL)
CREATE TABLE name( c1 type,c2 type,c3 type,... ,CONSTRAINT constraint_name FOREIGN KEY(c1) REFERENCE table2(column) ) (MySQL)
ALTER TABLE table ADD FOREIGN KEY (column) REFERENCE table2(column)
ALTER TABLE table ADD CONSTRAINT constraint_name FOREIGN KEY (column) REFERENCE table2(column)
ALTER TABLE table DROP FOREIGN KEY constraint_name (MySQL)
```

### check

```
CREATE TABLE name( c1 type,c2 type,c3 type,... ,CHECK(expression) ) (MySQL)
CREATE TABLE name( c1 type,c2 type,c3 type,... ,CONSTRAINT constraint_name CHECK(expression) ) (MySQL)
ALTER TABLE table ADD CHECK(expression)
ALTER TABLE table ADD CONSTRAINT constraint_name CHECK(expression)
ALTER TABLE table DROP CHECK constraint_name (MySQL)
```

### default

```
CREATE TABLE name( c1 type,c2 type,c3 type,... ,cn type DEFAULT 'value' ) (MySQL)
ALTER TABLE table ALTER column SET DEFAULT 'value' (MySQL)
ALTER TABLE table ALTER column DROP DEFAULT (MySQL)
```

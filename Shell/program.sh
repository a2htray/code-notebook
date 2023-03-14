#!/usr/bin/env bash

# 定义变量
var1=abc

# 定义包含空格的变量
var2="abc def"

# 定义引用旧变量的变量
var3=$var1
var4="${var1}ghi"

# 命令输出作为变量
var5=`whoami`

# 定义只读变量
var6="123"
readonly var6

echo "var1: $var1"
echo "var2: $var2"
echo "var3: $var3"
echo "var4: $var4"
echo "var5: $var5"

# 定义数组
arr1[0]="a"
arr1[1]="b"
arr1[2]="c"
# 定义数组
arr2=(1 2 3)

# 输出数组内容
echo "arr1: ${arr1[*]}"
echo "arr2: ${arr2[@]}"

# 输出数组长度
echo "length of arr1: ${#arr1[*]}"

# 遍历数组，值遍历
echo "遍历数组，值遍历"
for v in ${arr1[*]};
do
  echo $v
done

# 遍历数组，值遍历
echo "遍历数据，值遍历"
for v in ${arr1[@]};
do
  echo $v
done

# 遍历数组 1
for i in "${!arr1[@]}";
do
  echo "index $i: ${arr1[$i]}"
done

# 遍历数组 2
for (( i=0; i<${#arr2[@]}; i++ ));
do
  echo "index $i: ${arr2[$i]}"
done
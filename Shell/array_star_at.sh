#!/usr/bin/env bash

arr=(first "middle element" last)

echo ${arr[*]}
echo ${arr[@]}

for v in ${arr[*]}; # 等价于 for v in first middle element last;
do
  echo $v
done

for v in ${arr[@]}; # 等价于 for v in first middle element last;
do
  echo $v
done

for v in "${arr[*]}"; # 等价于 for v in "first middle element last";
do
  echo $v
done

for v in "${arr[@]}"; # 等价于 for v in first "middle element" last;
do
  echo $v
done
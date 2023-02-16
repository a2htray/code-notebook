#/bin/bash

# 创建一个保存 lo 环回接口信息的文本文件
ip addr show lo | tee lo.txt

# 创建多个具有相同内容的文件
echo 'content x' | tee file1.txt file2.txt

# 去除标准输出的展示
echo 'content y' | tee > /dev/null

# -i 忽略中断
ping 8.8.8.8 | tee -i ping.log
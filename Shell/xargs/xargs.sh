# 将标准输入转换成命令的参数
echo "a b c" | xargs ./three-arguments.sh

# 先利用 awk 进行参数重排序
# 再将标准输入转换成命令的参数
echo "a b c" | awk '{print $3, $2, $1}' | xargs ./three-arguments.sh

# xargs 接 bash 命令
echo "a b c" | xargs bash -c './three-options.sh -A $0 -B $1 -C $2'
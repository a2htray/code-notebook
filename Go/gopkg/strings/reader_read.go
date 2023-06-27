package main

import (
	"fmt"
	"io"
	"strings"
)

func main() {
	r := strings.NewReader("hello world|你好，世界")

	// 读取 hello
	buf := make([]byte, 5, 5)
	r.Read(buf)
	fmt.Println(string(buf)) // hello

	// 读取 world
	r.ReadAt(buf, 6)
	fmt.Println(string(buf)) // world

	// 读取到了空格
	b, _ := r.ReadByte()
	fmt.Printf("%v\n", string([]byte{b}) == " ") // true

	// 读取“你”
	skipBuf := make([]byte, 6, 6)
	r.Read(skipBuf)
	ch, size, _ := r.ReadRune()
	fmt.Printf("%s, 字节数：%d\n", string(ch), size) // 你, 字节数：3

	// 从开始处设置偏移量，偏移量为 0
	r.Seek(0, io.SeekStart)
	b, _ = r.ReadByte()
	fmt.Printf("%v\n", string([]byte{b})) // h

	// 由于上一个 r.ReadByte 读取了 1 个字节
	// 所以使用 UnreadByte 回退 1 个字节，从头开始读
	r.UnreadByte()
	r.Read(buf)
	fmt.Println(string(buf)) // hello
}

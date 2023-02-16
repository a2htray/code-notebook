package main

var a *int

func main() {
	b := 1 // 变量 b 的内存被分配到了堆
	a = &b
}

// go tool compile -m=2 1.9.1_variable_escape.go
// 1.9.1_variable_escape.go:5:6: can inline main with cost 9 as: func() { b := 1; a = &b }
// 1.9.1_variable_escape.go:6:2: b escapes to heap:
// 1.9.1_variable_escape.go:6:2:   flow: {heap} = &b:
// 1.9.1_variable_escape.go:6:2:     from &b (address-of) at 1.9.1_variable_escape.go:7:6
// 1.9.1_variable_escape.go:6:2:     from a = &b (assign) at 1.9.1_variable_escape.go:7:4
// 1.9.1_variable_escape.go:6:2: moved to heap: b

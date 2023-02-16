package main

import "testing"

// 使用 defer 和不使用 defer 的性能差异

// goos: windows
// goarch: amd64
// cpu: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
// BenchmarkSubWithDefer-8         442784984                2.555 ns/op
// BenchmarkSubWithoutDefer-8      1000000000               0.2458 ns/op
// PASS
// ok      command-line-arguments  1.821s

func sub(a, b int) int {
	return a - b
}

func subWithDefer() {
	defer sub(1, 2)
}

func subWithoutDefer() {
	sub(1, 2)
}

func BenchmarkSubWithDefer(b *testing.B) {
	for i := 0; i < b.N; i++ {
		subWithDefer()
	}
}

func BenchmarkSubWithoutDefer(b *testing.B) {
	for i := 0; i < b.N; i++ {
		subWithoutDefer()
	}
}

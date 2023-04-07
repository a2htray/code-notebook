package main

import (
	"errors"
	"fmt"
)

// Divisors 求整数 n 的所有正因数
func Divisors(n int) ([]int, error) {
	if n <= 0 {
		return nil, errors.New("n should be positive")
	}

	ds := make([]int, 0)
	for i := 1; i < n; i++ {
		if n%i == 0 {
			ds = append(ds, i)
		}
	}
	return ds, nil
}

func main() {
	fmt.Println(Divisors(10))
}

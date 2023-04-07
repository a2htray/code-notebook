package main

import "fmt"

func Max[V int | float64](vs []V) V {
	max := vs[0]
	for _, v := range vs[1:] {
		if v > max {
			max = v
		}
	}
	return max
}

func GetMode[V int | float64 | string](ints []V) V {
	m := make(map[V]int)
	for _, v := range ints {
		m[v]++
	}
	counts := make([]int, 0, len(m))
	newM := make(map[int]V)
	for k, v := range m {
		newM[v] = k
		counts = append(counts, v)
	}

	return newM[Max(counts)]
}

func main() {
	vs := []int{1, 2, 3, 1, 2, 1, 2}
	fmt.Println(GetMode(vs))

	vs1 := []string{"A", "A", "B"}
	fmt.Println(GetMode(vs1))
}

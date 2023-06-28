/**
 * 递归版本的归并排序
 */
package main

import "fmt"

func rMerge(left []int, right []int) []int {
	ret := make([]int, 0, len(left)+len(right))
	i := 0
	j := 0
	for i < len(left) && j < len(right) {
		if left[i] < right[j] {
			ret = append(ret, left[i])
			i++
		} else {
			ret = append(ret, right[j])
			j++
		}
	}

	if i < len(left) {
		for _, v := range left[i:] {
			ret = append(ret, v)
		}
	}

	if j < len(right) {
		for _, v := range right[j:] {
			ret = append(ret, v)
		}
	}
	return ret
}

func rMergeSort(s []int) []int {
	if len(s) <= 1 {
		return s
	}
	mid := len(s) / 2
	left := rMergeSort(s[:mid])
	right := rMergeSort(s[mid:])
	return rMerge(left, right)
}

func main() {
	s1 := []int{9, 8, 6, 6, 5, 4, 3, 2, 1}
	fmt.Println(rMergeSort(s1))
	s2 := []int{3, 1, 4, 4, 6, 5, 8}
	fmt.Println(rMergeSort(s2))
}

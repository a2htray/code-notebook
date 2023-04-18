/**
 * related content
 * 	@link https://stackoverflow.com/questions/39984957/is-it-possible-to-initialize-slice-with-specific-values
 */
package main

import "fmt"

func main() {
	// 5: 1 表示 slice 中下标为 5 的元素为 1
	var x = []int{0, 5: 1, 2}
	fmt.Println(len(x))

	for i, v := range x {
		fmt.Println(i, v)
	}
}

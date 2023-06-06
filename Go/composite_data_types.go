package main

import "fmt"

func main() {
	var myArr [3]int
	var myPointer *int
	var myAdd func(a, b int) int
	var mySlice []int
	var myMap map[int]string
	var myChan chan int
	var userStruct struct {
		Name string
		Age  int
	}
	var animalPointer *struct {
		Color string
	}

	fmt.Println(myArr, myPointer, myAdd, mySlice, myMap, myChan, userStruct, animalPointer)
}

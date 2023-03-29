package main

import (
	"fmt"
	"github.com/go-gota/gota/series"
)

func createWithSlice() series.Series {
	ser := series.New([]int{1, 2, 3}, series.Int, "number")
	return ser
}

func createWithSeries() series.Series {
	serOld := createWithSlice()
	serNew := series.New(serOld, series.String, "number string")
	return serNew
}

func main() {
	ser1 := createWithSlice()
	fmt.Println(ser1.String())

	ser2 := createWithSeries()
	fmt.Println(ser2.String())
}

package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
	"gonum.org/v1/gonum/mat"
	"log"
)

func createWithSeries() dataframe.DataFrame {
	df := dataframe.New(
		series.New([]string{"Ann", "John"}, series.String, "name"),
		series.New([]int{17, 18}, series.Int, "age"),
	)
	return df
}

func createWithStructs() dataframe.DataFrame {
	type Student struct {
		Name string
		Age  int
		// gender 字段会被忽略
		gender int
	}
	students := []Student{
		{
			Name:   "Ann",
			Age:    17,
			gender: 2,
		},
		{
			Name:   "John",
			Age:    18,
			gender: 1,
		},
	}
	df := dataframe.LoadStructs(students)
	return df
}

func createWithRecords() dataframe.DataFrame {
	df := dataframe.LoadRecords([][]string{
		{"Ann", "17"},
		{"John", "18"},
	}, dataframe.HasHeader(false), dataframe.Names("name", "age"))
	return df
}

func createWithMaps() dataframe.DataFrame {
	df := dataframe.LoadMaps([]map[string]interface{}{
		{"name": "Ann", "age": "17"},
		{"name": "John", "age": "18"},
	}, dataframe.WithTypes(map[string]series.Type{
		"name": series.String,
		"age":  series.Int,
	}))

	return df
}

func createWithMatrix() dataframe.DataFrame {
	df := dataframe.LoadMatrix(
		mat.NewDense(3, 2, []float64{1.0, 2.0, 3.0, 1.1, 2.2, 3.1}),
	)
	if err := df.SetNames("x", "y"); err != nil {
		log.Fatal(err)
	}
	return df
}

func main() {
	df1 := createWithSeries()
	fmt.Println(df1.String())

	df2 := createWithStructs()
	fmt.Println(df2.String())

	df3 := createWithRecords()
	fmt.Println(df3)

	df4 := createWithMaps()
	fmt.Println(df4)

	df5 := createWithMatrix()
	fmt.Println(df5)
}

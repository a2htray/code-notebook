package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
	"log"
)

func innerJoin() dataframe.DataFrame {
	df1 := dataframe.New(
		series.New([]string{"Ann", "John"}, series.String, "name"),
		series.New([]int{17, 18}, series.Int, "age"),
	)

	df2 := dataframe.New(
		series.New([]string{"Ann", "Jimmy"}, series.String, "name"),
		series.New([]int{2, 1}, series.Int, "gender"),
	)

	df3 := df1.InnerJoin(df2, "name")

	return df3
}

func leftJoin() dataframe.DataFrame {
	df1 := dataframe.New(
		series.New([]string{"Ann", "John"}, series.String, "name"),
		series.New([]int{17, 18}, series.Int, "age"),
	)

	df2 := dataframe.New(
		series.New([]string{"Ann", "Jimmy"}, series.String, "name"),
		series.New([]int{2, 1}, series.Int, "gender"),
	)

	df3 := df1.LeftJoin(df2, "name")

	return df3
}

func rightJoin() dataframe.DataFrame {
	df1 := dataframe.New(
		series.New([]string{"Ann", "John"}, series.String, "name"),
		series.New([]int{17, 18}, series.Int, "age"),
	)

	df2 := dataframe.New(
		series.New([]string{"Ann", "Jimmy"}, series.String, "name"),
		series.New([]int{2, 1}, series.Int, "gender"),
	)

	df3 := df1.RightJoin(df2, "name")

	return df3
}

func outerJoin() dataframe.DataFrame {
	df1 := dataframe.New(
		series.New([]string{"Ann", "John"}, series.String, "name"),
		series.New([]int{17, 18}, series.Int, "age"),
	)

	df2 := dataframe.New(
		series.New([]string{"Ann", "Jimmy"}, series.String, "name"),
		series.New([]int{2, 1}, series.Int, "gender"),
	)

	df3 := df1.OuterJoin(df2, "name")

	return df3
}

func crossJoin() dataframe.DataFrame {
	df1 := dataframe.New(
		series.New([]string{"Ann", "John"}, series.String, "name"),
		series.New([]int{17, 18}, series.Int, "age"),
	)

	df2 := dataframe.New(
		series.New([]string{"Ann", "Jimmy"}, series.String, "name"),
		series.New([]int{2, 1}, series.Int, "gender"),
	)

	df3 := df1.CrossJoin(df2)
	if err := df3.SetNames([]string{"df1_name", "age", "df2_name", "gender"}...); err != nil {
		log.Fatal(err)
	}

	return df3
}

func main() {
	dfInnerJoin := innerJoin()
	fmt.Println(dfInnerJoin)

	dfLeftJoin := leftJoin()
	fmt.Println(dfLeftJoin)

	dfRightJoin := rightJoin()
	fmt.Println(dfRightJoin)

	dfOuterJoin := outerJoin()
	fmt.Println(dfOuterJoin)

	dfCrossJoin := crossJoin()
	fmt.Println(dfCrossJoin)
}

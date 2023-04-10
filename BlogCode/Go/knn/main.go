package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
	"gonum.org/v1/gonum/floats"
	"log"
	"math"
	"math/rand"
	"os"
	"time"
)

// SplitDataset 拆分数据集
func SplitDataset(df dataframe.DataFrame, pct float64) (xTrain, xTest dataframe.DataFrame, yTrain, yTest series.Series) {
	n := df.Nrow()
	nTrain := int(float64(n) * pct)
	indexes := func(n int) []int {
		ret := make([]int, n)
		for i := 0; i < n; i++ {
			ret[i] = i
		}
		return ret
	}(n)
	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(n, func(i, j int) {
		indexes[i], indexes[j] = indexes[j], indexes[i]
	})

	trainData := df.Subset(indexes[:nTrain])
	testData := df.Subset(indexes[nTrain:])
	xTrain = trainData.Select(df.Names()[1:])
	xTest = testData.Select(df.Names()[1:])
	yTrain = trainData.Col("Class")
	yTest = testData.Col("Class")
	return
}

// GetRow 取数据集中的一行记录
func GetRow(df dataframe.DataFrame, i int) series.Series {
	elements := make([]series.Element, df.Ncol())
	for j := 0; j < df.Ncol(); j++ {
		elements[j] = df.Elem(i, j)
	}
	return series.New(elements, series.Float, "value")
}

// GetMode 取 slice 中出现最多的一个值
func GetMode(vs []int) int {
	m := make(map[int]int)
	for _, v := range vs {
		m[v]++
	}

	counts := make([]int, 0, len(m))
	newM := make(map[int]int)
	for k, v := range m {
		counts = append(counts, v)
		newM[v] = k
	}

	max := func(vs []int) int {
		max := vs[0]
		for _, v := range vs[1:] {
			if v > max {
				max = v
			}
		}
		return max
	}(counts)

	return newM[max]
}

func Score(vs1 []int, vs2 []int) float64 {
	n := len(vs1)
	neq := 0.0

	for i, v := range vs1 {
		if v == vs2[i] {
			neq++
		}
	}

	return neq / float64(n)
}

func ReadWineData(filename string) (dataframe.DataFrame, error) {
	f, err := os.Open(filename)
	if err != nil {
		return dataframe.DataFrame{}, err
	}

	columns := []string{
		"Class",
		"Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium",
		"Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
		"Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline",
	}
	df := dataframe.ReadCSV(f, dataframe.Names(columns...), dataframe.WithTypes(map[string]series.Type{
		"Class":                        series.Int,
		"Alcohol":                      series.Float,
		"Malic acid":                   series.Float,
		"Ash":                          series.Float,
		"Alcalinity of ash":            series.Float,
		"Magnesium":                    series.Float,
		"Total phenols":                series.Float,
		"Flavanoids":                   series.Float,
		"Nonflavanoid phenols":         series.Float,
		"Proanthocyanins":              series.Float,
		"Color intensity":              series.Float,
		"Hue":                          series.Float,
		"OD280/OD315 of diluted wines": series.Float,
		"Proline":                      series.Float,
	}))
	return df, nil
}

func main() {
	metric := func(fs1 []float64, fs2 []float64) float64 {
		return floats.Distance(fs1, fs2, 2)
	}

	// 读取数据
	df, err := ReadWineData("./dataset/wine.data")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(df)
	xTrain, xTest, yTrain, yTest := SplitDataset(df, 0.95)

	k := int(math.Sqrt(float64(xTrain.Nrow())))
	fmt.Println("k =", k)

	yPredict := make([]int, yTest.Len())

	for i := 0; i < xTest.Nrow(); i++ {
		ser := GetRow(xTest, i)
		metricValues := make([]float64, xTrain.Nrow())
		for ii := 0; ii < xTrain.Nrow(); ii++ {
			targetSer := GetRow(xTrain, ii)
			metricValues[ii] = metric(ser.Float(), targetSer.Float())
		}
		indexes := make([]int, len(metricValues))
		floats.Argsort(metricValues, indexes)

		yTrain.Subset(indexes[:k])
		vs, _ := yTrain.Subset(indexes[:k]).Int()

		yPredict[i] = GetMode(vs)
	}

	yTestValues, _ := yTest.Int()
	fmt.Println(Score(yPredict, yTestValues))
}

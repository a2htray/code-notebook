package main

import (
	"flag"
	"fmt"
	"strconv"
	"strings"
)

const (
	Delimiter = ","
)

type Elements []int

func (e *Elements) String() string {
	return "elements"
}

func (e *Elements) Set(s string) error {
	tokens := strings.Split(s, Delimiter)
	eles := make([]int, len(tokens))

	for i, token := range tokens {
		v, err := strconv.ParseInt(token, 0, 64)
		if err != nil {
			return err
		}
		eles[i] = int(v)
	}
	*e = eles
	return nil
}

func (e *Elements) All() []int {
	vs := make([]int, len(*e))

	for i, v := range *e {
		vs[i] = v
	}
	return vs
}

func main() {
	var elements Elements
	flag.Var(&elements, "elements", "element list")
	flag.Parse()

	fmt.Println(elements.All())
}

package examples

import (
	"flag"
	"fmt"
)

type PencilTypes []string

func (p *PencilTypes) String() string {
	return "pencil type"
}

func (p *PencilTypes) Set(s string) error {
	*p = append(*p, s)
	return nil
}

func FlagWithValues() {
	pencilTypes := PencilTypes([]string{})
	flag.Var(&pencilTypes, "pencil-type", "pencil type")
	flag.Parse()

	for _, v := range pencilTypes {
		fmt.Println(v)
	}
}

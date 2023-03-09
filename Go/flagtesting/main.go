package main

import (
	"fmt"
	"github.com/a2htray/flagtesting/examples"
)

var list = []string{
	"1) shorthand",
	"2) user defined flag type",
	"3) flag.NewFlagSet",
	"4) flag with values",
}

func main() {
	for _, v := range list {
		fmt.Println(v)
	}
	var seqNo = 0
	fmt.Print("type a sequence no: ")
	fmt.Scanln(&seqNo)

	seqNo--

	if seqNo == 0 {
		examples.ParseFruit()
	} else if seqNo == 1 {
		examples.ParseStudent()
	} else if seqNo == 2 {
		examples.ParseArguments()
	} else if seqNo == 3 {
		examples.FlagWithValues()
	}
}

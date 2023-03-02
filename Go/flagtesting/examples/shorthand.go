package examples

import (
	"flag"
	"fmt"
)

const fruitApple = "apple"
const fruitBanana = "banana"
const fruitOrange = "orange"

var fruit string

func ParseFruit() {
	usage := "a type of fruit"
	flag.StringVar(&fruit, "fruit", fruitApple, usage)
	flag.StringVar(&fruit, "f", fruitApple, usage+" (shorthand)")
	flag.Parse()

	fmt.Printf("fruit: %s\n", fruit)
}

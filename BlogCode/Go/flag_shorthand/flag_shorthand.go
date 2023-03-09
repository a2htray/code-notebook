package main

import (
	"flag"
	"fmt"
)

func main() {
	var debug bool
	var password string
	debugUsage := "run in debug mode"
	passwordUsage := "type password"

	flag.BoolVar(&debug, "d", false, debugUsage)
	flag.BoolVar(&debug, "debug", false, debugUsage)
	flag.StringVar(&password, "p", "", passwordUsage)
	flag.StringVar(&password, "password", "", passwordUsage)
	flag.Parse()

	fmt.Printf("debug: %v\n", debug)
	fmt.Printf("password: %s\n", password)
}

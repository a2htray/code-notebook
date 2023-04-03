package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	line, _, err := r.ReadLine()
	if err != nil {
		fmt.Println(err)
	}

	s := string(line)
	fmt.Println(s, len(s))

	// echo 111 | go run read_console_input.go
}

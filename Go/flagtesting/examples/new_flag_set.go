package examples

import (
	"flag"
	"fmt"
	"os"
)

func Usage() {
	fmt.Println("usage example")
}

func ParseArguments() {
	var commandLine = flag.NewFlagSet(os.Args[0], flag.ExitOnError)
	commandLine.Usage = Usage
	commandLine.SetOutput(os.Stdout)
	
	var name string
	var age int
	commandLine.StringVar(&name, "name", "a2htray", "student name")
	commandLine.IntVar(&age, "age", 18, "student age")
	commandLine.Parse(os.Args[1:])

	fmt.Println(commandLine.Args())
	fmt.Printf("student name (%s) and age (%d)\n", name, age)
	fmt.Fprintf(commandLine.Output(), "%s", "commandLine.Output")
}

package main

import "fmt"

type MyError struct {
	error
}

func (e MyError) String() {

}

func returnError() error {
	var err *MyError = nil
	return err
}

func main() {
	var err *MyError = nil
	fmt.Println(err == nil) // True

	fmt.Println(returnError() == nil) // False
}

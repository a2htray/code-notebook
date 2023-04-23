package main

import "fmt"

type Car struct{}

func (c Car) Drive() {
	fmt.Println("Car.Drive")
}

func (c Car) Stop() {
	fmt.Println("Car.Stop")
}

func main() {
	car := Car{}

	car.Drive() // 可以
	car.Stop()  // 可以

	carPointer := &Car{}

	carPointer.Drive()
	carPointer.Stop()
}

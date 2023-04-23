package main

type Car struct{}

func (c *Car) Drive() {}

type Truck struct {
	*Car
}

func (t *Truck) Attack() {}

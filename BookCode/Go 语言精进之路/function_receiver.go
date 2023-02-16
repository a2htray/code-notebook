package main

type MyInt *int

//func (m MyInt) String() string { // pointer 不能作为 receiver
//	return fmt.Sprintf("%d", *m)
//}

type Counter interface{}

//func (c *Counter)() { // interface 不能作为 receiver
//
//}
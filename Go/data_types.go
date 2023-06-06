package main

import (
	"fmt"
	"unsafe"
)

func main() {
	var b bool = true
	var x int = 123
	var ux uint = 123
	var x8 int8 = 123
	var ux8 uint8 = 123
	var b1 byte = 'a'
	var x16 int16 = 123
	var ux16 uint16 = 123
	var x32 int32 = 123
	var r rune = 123
	var ux32 uint32 = 123
	var x64 int64 = 123
	var ux64 uint64 = 123
	var f32 float32 = 123.0
	var f64 float64 = 123.0
	var c64 complex64 = complex(1, 2)
	var c128 complex128 = complex(2, 1)
	var s string = "1234567890"

	fmt.Println("variable b:", b, ", size of variable b:", unsafe.Sizeof(b))
	fmt.Println("variable x:", x, ", size of variable x:", unsafe.Sizeof(x))
	fmt.Println("variable ux:", ux, ", size of variable ux:", unsafe.Sizeof(ux))
	fmt.Println("variable x8:", x8, ", size of variable x8:", unsafe.Sizeof(x8))
	fmt.Println("variable ux8:", ux8, ", size of variable ux8:", unsafe.Sizeof(ux8))
	fmt.Println("variable b1:", b1, ", size of variable b1:", unsafe.Sizeof(b1))
	fmt.Println("variable x16:", x16, ", size of variable x16:", unsafe.Sizeof(x16))
	fmt.Println("variable ux16:", ux16, ", size of variable x16:", unsafe.Sizeof(ux16))
	fmt.Println("variable x32:", x32, ", size of variable x32:", unsafe.Sizeof(x32))
	fmt.Println("variable r:", r, ", size of variable r:", unsafe.Sizeof(r))
	fmt.Println("variable ux32:", ux32, ", size of variable ux32:", unsafe.Sizeof(ux32))
	fmt.Println("variable x64:", x64, ", size of variable x64:", unsafe.Sizeof(x64))
	fmt.Println("variable ux64:", ux64, ", size of variable ux64:", unsafe.Sizeof(ux64))
	fmt.Println("variable f32:", f32, ", size of variable f32:", unsafe.Sizeof(f32))
	fmt.Println("variable f64:", f64, ", size of variable f64:", unsafe.Sizeof(f64))
	fmt.Println("variable c64:", c64, ", size of variable c64:", unsafe.Sizeof(c64))
	fmt.Println("variable c128:", c128, ", size of variable c128:", unsafe.Sizeof(c128))
	fmt.Println("variable s:", s, ", size of variable s:", unsafe.Sizeof(s))
}

package main

import (
	"bytes"
	"encoding/gob"
	"fmt"
	"log"
)

type Book struct {
	Name string
}

func main() {
	bookSent := Book{Name: "Go Hand Book"}
	var network bytes.Buffer
	enc := gob.NewEncoder(&network)
	dec := gob.NewDecoder(&network)

	if err := enc.Encode(bookSent); err != nil {
		log.Fatal(err)
	}

	var bookReceived Book
	if err := dec.Decode(&bookReceived); err != nil {
		log.Fatal(err)
	}

	fmt.Println(bookReceived.Name)

}

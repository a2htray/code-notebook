package main

import (
	"fmt"
	"github.com/go-co-op/gocron"
	"log"
	"time"
)

func main() {
	scheduler := gocron.NewScheduler(time.UTC)
	_, err := scheduler.Every("1s").Do(func() {
		fmt.Println("hello world")
	})

	if err != nil {
		log.Fatal(err)
	}

	_, err = scheduler.Every("5s").Do(func(message string) {
		fmt.Println(message)
	}, "5s hello world")

	if err != nil {
		log.Fatal(err)
	}

	scheduler.StartBlocking()
}

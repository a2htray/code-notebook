package main

import "sync"

type Singleton struct {
	field1 string
	field2 int
}

func (s *Singleton) SetFields(f1 string, f2 int) {
	s.field1 = f1
	s.field2 = f2
}

var (
	once     sync.Once
	instance Singleton
)

func NewSingleton() *Singleton {
	once.Do(func() {
		instance = Singleton{}
	})
	return &instance
}

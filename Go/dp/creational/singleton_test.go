package main

import "testing"

func TestNewSingleton(t *testing.T) {
	ins1 := NewSingleton()
	ins2 := NewSingleton()

	if ins1 != ins2 {
		t.Errorf("ins1 and ins2 are both same\n")
	}

	ins1.SetFields("f1", 1)

	if ins2.field1 != "f1" {
		t.Errorf("ins2.field1 must be f1, now its value is %s\n", ins1.field1)
	}
}

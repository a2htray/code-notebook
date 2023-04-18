package main

import "testing"

func TestNewConfiger(t *testing.T) {
	configer1 := NewConfiger(ConfigerEnv)
	configer2 := NewConfiger(ConfigerDB)

	if configer1 == configer2 {
		t.Errorf("both configers are not equal")
	}
}
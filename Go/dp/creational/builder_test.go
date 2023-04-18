package main

import "testing"

func TestNewRequestBuilder(t *testing.T) {
	builder := NewRequestBuilder()
	builder.Header("Content-Type", "application/json").Cookie("uid", "uidxxx")

	request := builder.Build()

	if request.Header.Get("Content-Type") != "application/json" {
		t.Errorf("Content-Type must be 'application/json'")
	}
}

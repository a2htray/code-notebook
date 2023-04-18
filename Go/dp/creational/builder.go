package main

import (
	"net/http"
	"time"
)

type RequestBuilder interface {
	Header(name string, value string) RequestBuilder
	Cookie(name string, value string) RequestBuilder
	Build() *http.Request
}

type requestBuilder struct {
	r *http.Request
}

func (r *requestBuilder) Header(name string, value string) RequestBuilder {
	r.r.Header.Set(name, value)
	return r
}

func (r *requestBuilder) Cookie(name string, value string) RequestBuilder {
	c := &http.Cookie{
		Name:       name,
		Value:      value,
		Path:       "/",
		Domain:     "*",
		Expires:    time.Time{},
		RawExpires: "",
		MaxAge:     0,
		Secure:     false,
		HttpOnly:   false,
		SameSite:   0,
		Raw:        "",
		Unparsed:   nil,
	}
	r.r.AddCookie(c)
	return r
}

func (r *requestBuilder) Build() *http.Request {
	return r.r
}

func NewRequestBuilder() RequestBuilder {
	return &requestBuilder{r: &http.Request{
		Header: map[string][]string{},
	}}
}

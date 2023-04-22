package main

type Writer interface {
	Write()
}

type Closer interface {
	Writer
	Close()
}

type DiskCloser struct{}

func (d *DiskCloser) Write() {}

func (d *DiskCloser) Close() {}

package main

import (
	"embed"
	"fmt"
	"log"
	"net/http"
)

var (
	//go:embed version.txt
	version string
	//go:embed version.txt
	versionB []byte
	//go:embed static/js/*
	fs embed.FS
)

func main() {
	http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
		b, _ := fs.ReadFile("static/js/app.js")

		value := fmt.Sprintf(`version: %s
versionB: %s
app.js: %s
`, version, string(versionB), string(b))

		w.Write([]byte(value))
	})

	http.Handle("/static/", http.FileServer(http.FS(fs)))

	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
}

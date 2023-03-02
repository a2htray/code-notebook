package examples

import (
	"crypto/md5"
	"flag"
	"fmt"
)

type Student struct {
	id   string
	Name string
}

func (s *Student) String() string {
	return fmt.Sprintf("%s-%s", s.id, s.Name)
}

func (s *Student) Set(value string) error {
	bs := md5.Sum([]byte(value))

	*s = Student{
		id:   fmt.Sprintf("%x", bs),
		Name: value,
	}

	return nil
}

var student Student

func ParseStudent() {
	flag.Var(&student, "student", "student name")
	flag.Parse()

	fmt.Println(student.String())
}
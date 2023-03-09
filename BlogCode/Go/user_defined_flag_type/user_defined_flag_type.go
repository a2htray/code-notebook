package main

import (
	"errors"
	"flag"
	"fmt"
	"strconv"
	"strings"
)

// Gender 性别
type Gender int

const (
	// genderMale 男性
	genderMale Gender = iota
	// genderFemale 女性
	genderFemale
)

var (
	// ErrUserParse 无法解析用户信息
	ErrUserParse = errors.New("parse user error")
)

// User 自定义选项结构
// 支持以命令行选项的方式实例化，使用 : 作为分隔，选项值形如：`xiaoming:18:0`
type User struct {
	Name   string
	age    int
	gender Gender
}

func (u *User) String() string {
	return "user"
}

// Set 解析传递来的字符串，实例化 User 结构
func (u *User) Set(s string) error {
	tokens := strings.Split(s, ":")
	if len(tokens) != 3 {
		return ErrUserParse
	}
	u.Name = tokens[0]

	v, err := strconv.ParseInt(tokens[1], 0, strconv.IntSize)
	if err != nil {
		return err
	}
	u.age = int(v)

	v, err = strconv.ParseInt(tokens[2], 0, strconv.IntSize)
	if err != nil {
		return err
	}
	gender := Gender(v)
	if !(gender == genderMale || gender == genderFemale) {
		return ErrUserParse
	}
	u.gender = gender

	return nil
}

func main() {
	var user = User{}
	flag.Var(&user, "user", "user information")
	flag.Parse()

	fmt.Printf("name: %s\n", user.Name)
	fmt.Printf("age: %d\n", user.age)
	fmt.Printf("gender: %d\n", user.gender)
}

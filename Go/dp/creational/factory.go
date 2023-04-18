package main

type Configer interface {
	String(key string) string
	Int(key string) int
}

type configerType int

const (
	ConfigerEnv configerType = iota
	ConfigerDB
)

type envConfiger struct{}

func (e *envConfiger) String(key string) string {
	return "your logic"
}

func (e *envConfiger) Int(key string) int {
	// your logic
	return 1
}

func newEnvConfiger() Configer {
	return &envConfiger{}
}

type dbConfiger struct{}

func (d *dbConfiger) String(key string) string {
	return "your logic"
}

func (d *dbConfiger) Int(key string) int {
	// your logic
	return 1
}

func newDBConfiger() Configer {
	return &dbConfiger{}
}

func NewConfiger(ct configerType) Configer {
	switch ct {
	case ConfigerEnv:
		return newEnvConfiger()
	case ConfigerDB:
		return newDBConfiger()
	default:
		panic("configer type error")
	}
}

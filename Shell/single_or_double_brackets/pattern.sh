#!/usr/bin/env bash

name=Alice

[[ $name = *c* ]] && echo "Name includes c"

echo $?

[[ $name =~ ^Ali ]] && echo "Regular expressions can be used"
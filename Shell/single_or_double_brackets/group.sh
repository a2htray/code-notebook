#!/usr/bin/env bash

[[ 3 -eq 3 && (2 -eq 2 && 1 -eq 1) ]] && echo "Parentheses can be used"

[ 3 -eq 3 -a \( 2 -eq 2 -a 1 -eq 1 \) ] && echo "Parentheses can be used"
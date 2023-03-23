#!/usr/bin/env bash

[[ 1 < 2 ]] && echo "1 is less than 2"

[ 1 \< 2 ] && echo "1 is less than 2"

[[ 1 -lt 2 ]] && echo "1 is less than 2"
[ 1 -lt 2 ] && echo "1 is less than 2"

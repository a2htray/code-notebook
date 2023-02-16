#!/bin/bash

if [[ "$#" != 3 ]]; then
    echo "[Error] three arguments required."
    exit 1
fi

echo "the 1st argument is $1"
echo "the 2nd argument is $2"
echo "the 3rd argument is $3"

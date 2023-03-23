#!/usr/bin/env bash

filename="none existent file"
[[ ! -e $filename ]] && echo -n "File doesn't exist;" && echo $filename

[ ! -e "$filename" ] && echo -n "File doesn't exist;" && echo $filename

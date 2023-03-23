#!/usr/bin/env bash

# -b
block_file=my_block_file

# create a block special file using mknod
mknod $block_file b 1 2

[[ -b $block_file ]] && echo "$block_file is a block special file"

# -c
character_file=my_character_file

# create a character special file using mknod
mknod $character_file c 1 2

[[ -c $character_file ]] && echo "$character_file is a character special file"


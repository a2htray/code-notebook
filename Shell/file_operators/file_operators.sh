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

# -d
[[ -d /etc ]] && echo "/etc is a directory"

# -f
[[ -f /etc/passwd ]] && echo "/etc/passwd is a file"

# -g
mkdir SGID_test
chmod g+s SGID_test

[[ -g ./SGID_test ]] && echo "./SGID_test has been set SGID bit"

# -k
mkdir sticky_file
chmod +t sticky_file

[[ -k ./sticky_file ]] && echo "./sticky_file has been set sticky bit"

# -p
mknod named_pipe p
[[ -p ./named_pipe ]] && echo "./named_pipe is a named pipe"

# -u
touch SUID_test
chmod u+s SUID_test
[[ -u ./SUID_test ]] && echo "./SUID_test has been set SUID bit"

# -r
touch readable_file
chmod u+r readable_file
[[ -r ./readable_file ]] && echo "./readable_file is a readable file"

# -w
touch writable_file
chmod u+w writable_file
[[ -w ./writable_file ]] && echo "./writable_file is a writable file"

# -x
touch executable_file
chmod u+x executable_file
[[ -x ./executable_file ]] && echo "./executable_file ia an executable file"

# -s
echo "content" >test_file
[[ -s ./test_file ]] && echo "the size of ./test_file is larger than 0"

# -L
touch origin_file
ln -s origin_file linked_file
[[ -L ./linked_file ]] && echo "./linked_file is a linked file"

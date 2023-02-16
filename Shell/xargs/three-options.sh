#!/bin/bash
# 处理单个字符的选项

while getopts ":A:B:C:" opt; do
    echo $opt
    case $opt in
        A) echo "the argument for option A is $OPTARG, when the OPTIND=$OPTIND";;
        B) echo "the argument for option B is $OPTARG, when the OPTIND=$OPTIND";;
        C) echo "the argument for option C is $OPTARG, when the OPTIND=$OPTIND";;
        ?) echo "unkown option" && exit 1 ;;
    esac
done

shift "$(($OPTIND - 1))"
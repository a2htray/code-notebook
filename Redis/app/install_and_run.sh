#!/bin/bash

pip install -r ./requirements.txt
python list.py
python list_block_ops.py
tail -f /dev/null
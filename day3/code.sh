#!/bin/bash

# Part 1
cat input.txt | grep -oP "mul\\(\d+,\d+\\)" | grep -oP '\d+,\d+' | awk -F, '{ sum += $1 * $2 } END { print sum }'

# Part 2
cat input.txt | grep -oP "mul\\((\d+),(\d+)\\)|do\(\)|don't\(\)" | sed 's/mul//g' | sed 's/(\|)//g' | sed 's/,/ /g' | awk -v flag=1 -v sum=0 '{ if ($1 == "do") { flag=1 } else if ($1 == "don'\''t") { flag=0 } else { if (flag == 1) {sum += $1 * $2} } } END { print sum }'
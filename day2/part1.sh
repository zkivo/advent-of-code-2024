#!/bin/bash

# Part 1
cat input.txt | awk -v first_diff=0 -v sum=0 '{
    for (i = 1; i < NF; i++) {
        if (i == 1) {
            diff = $(i + 1) - $i;
            first_diff = diff;
            if (diff < 1) {
                diff *= -1;
            }
            if (diff < 1 || diff > 3) {
                break;
            }
        } else {
            diff = $(i + 1) - $i;
            if (diff * first_diff < 0) {
                break;
            } else {
                if (diff < 1) {
                    diff *= -1;
                }
                if (diff < 1 || diff > 3) {
                    break;
                }
            }
        }
    }
    if (i == NF) {
        sum++;
    }
} END {
    print sum;
}'
#!/bin/bash

#
#
#           IT DOES NOT WORK!!
#
#   I think is because there is no float in bash, therefore cannot store
#      big numbers. :(
#
#

# Define your regex
regex="mul\\(([0-9]{1,3}),([0-9]{1,3})\\)"
sum=0
# Read from standard input
while read -r line; do
    # Use a while loop with grep -o to find all matches of the regex in the line
    while [[ $line =~ $regex ]]; do
        match="${BASH_REMATCH[0]}" # Extract the matched text
        echo $match ${BASH_REMATCH[1]} ${BASH_REMATCH[2]}
        (( sum += ${BASH_REMATCH[1]} * ${BASH_REMATCH[2]} )) # Add the product to the sum

        # Modify the line to avoid infinite loop (remove the first match)
        line="${line/${BASH_REMATCH[0]}/}"
    done
done

echo $sum
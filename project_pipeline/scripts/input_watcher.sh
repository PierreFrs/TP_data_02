#!/bin/bash

# input directory scan
DIRECTORY="../data/input/"

echo "Checking input directory..."
if [ "$(ls -A $DIRECTORY 2>/dev/null)" ]; then
    echo "Files detected, launching jobs..."
    for f in "$DIRECTORY"*.csv ; do
        
        # Check file empty
        if [[ ! -s "$f" ]]; then
            echo "File is empty"
            exit 1
        fi

        # check column number in rows
        expected_cols=$(head -1 "$f" | tr ',' '\n' | wc -l)
        echo "📊 Expected columns: $expected_cols"

        # Check for inconsistent column counts
        inconsistent=$(awk -F',' -v expected="$expected_cols" '
            NR > 1 && NF != expected { 
                print "Line " NR ": " NF " columns (expected " expected ")" 
            }
        ' "$f")
        
        if [[ -n "$inconsistent" ]]; then
            echo "Inconsistent column counts found:"
            echo "$inconsistent" | head -5
            return 1
        fi
        
        # Check total rows
        total_rows=$(wc -l < "$f")
        echo "Total rows: $total_rows (including header)"
        
        # Show header
        echo "Header:"
        head -1 "$f" | tr ',' '\n' | nl
        
        echo "CSV structure is valid and ready for processing"

        [[ -e "$f" ]] || break
        filename=$(basename "$f")
        echo "Copying $filename to processing directory"
        cp "$f" "../data/processing/"
    done
else
    echo "No file detected in input directory"
fi
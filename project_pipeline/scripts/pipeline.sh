#!/bin/bash

# Check input directory content
chmod 755 ./input_watcher.sh
./input_watcher.sh

# Launch data processing for csv files in processing directory
PROCESSING_DIRECTORY="../data/processing/"

echo "Checking processing directory..."
if [ "$(ls -A $PROCESSING_DIRECTORY 2>/dev/null)" ]; then
    echo "Files detected, launching jobs..."
    for f in "$PROCESSING_DIRECTORY"*.csv ; do
        [[ -e "$f" ]] || break
        filename=$(basename "$f")
        echo "Processing: $filename"
        python3 ./process_data.py "$filename"
    done
fi
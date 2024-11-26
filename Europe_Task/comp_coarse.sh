#!/bin/bash

# Loop through years from 1950 to 2010
for year in $(seq 1950 2010)
do
    echo "Processing year: $year"
    
    # Assuming you have a command to compute coarse data
    # Replace this with your actual command
    python comp_coarse_cutting_pvpot.py --year $year
    
    # Add error checking
    if [ $? -ne 0 ]; then
        echo "Error processing year $year"
        exit 1
    fi
done

echo "Coarse data computation completed for all years"

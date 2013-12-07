#!/bin/bash
length=10
while [ $length -le 1000000 ]; do
echo '------------------------------'
echo "generating length=$length dna in sample/$length"
../tools/genData.py $length > ../sample/$length
let "length=$length*10"
done

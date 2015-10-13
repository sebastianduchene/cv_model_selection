#!/bin/bash

files=`ls *subset.fasta`

for i in $files; do
    ./xml_maker.py $i
done

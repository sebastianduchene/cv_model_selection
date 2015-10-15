#!/bin/bash

trees=`ls runs/*ucld.trees`

for t in $trees; do
    echo doing $t
    ./make_phylogs.py $t
done
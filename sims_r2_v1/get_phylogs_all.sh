#!/bin/bash

trees=`ls runs/*exp.trees`

for t in $trees; do
    echo doing $t
    ./make_phylogs.py $t
done
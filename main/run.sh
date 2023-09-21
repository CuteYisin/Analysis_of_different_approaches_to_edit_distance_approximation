#!/bin/bash

BATCH=5
#BATCH=50-50

#INPUT_FASTA=/data/lobby/lsh_simul/testdata${BATCH}.fa
#INPUT_FASTA=/data/cabins/yxxiang/real/metaFamily_8339.fasta
INPUT_FASTA=/data/cabins/yxxiang/QB/protein_${BATCH}.fa
#INPUT_FASTA=/data/cabins/yxxiang/real/metaFamily_8339.fasta
OUTPUT_DIR=/data/cabins/yxxiang/QB/protein_${BATCH}

make clean
make -j


mkdir ${OUTPUT_DIR}
mkdir ${OUTPUT_DIR}/$1-$2

./distance_space_embedding -w $1 -k $2 -p $3 ${INPUT_FASTA} ${OUTPUT_DIR}

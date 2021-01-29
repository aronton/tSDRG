#!/bin/bash

#$ -q all.q
#$ -S /bin/bash
#$ -cwd
#$ -j y

#$ -pe smp 12
export OMP_NUM_THREADS=12

PATH=/home/liusf/anaconda3/bin:${PATH}
source /home/liusf/intel/bin/compilervars.sh intel64

date
python Dimer-Oz_Metadata_new64.py
echo -e "\ndone.\n\n"
date



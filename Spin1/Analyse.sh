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
python Dimer-ZL_Metadata_Random.py
echo -e "\ndone.\n\n"
date



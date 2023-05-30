#!/bin/bash

start=`date +%s`

cd Pipeline

python3 Main.py

cd ~

gsutil cp -r ~/Results/ gs://hdcmlmed/
gsutil cp slurm* gs://hdcmlmed/Results/
gsutil cp *.pkl gs://hdcmlmed/

end=`date +%s`
echo $((end-start))


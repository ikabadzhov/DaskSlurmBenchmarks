#!/bin/sh

unlink ~/distrdf_timestamps.out  # remove the old logs (if any)
rm *.out
killall python3

while getopts d: flag
do
  case "${flag}" in
    d) dirn=${OPTARG};;
  esac
done

mkdir "${dirn}"

for Nodes in 64 32
do
  for p in 4096 8192
  do
    CMD="python3 02_distrdf.py -c 32 -N ${Nodes} -f 1000 -p ${p}"
    printf "\n\n${CMD}\n" >> ~/distrdf_timestamps.out
    eval "$CMD"
    mkdir "${dirn}/log_p${p}_N${Nodes}"
    mv *.out "${dirn}/log_p${p}_N${Nodes}"  # move the newly produced slurm logs
    mv *.html "${dirn}/log_p${p}_N${Nodes}"
    echo "$CMD was done"
    killall python3
  done
done

mv ~/distrdf_timestamps.out ./${dirn}


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

for Nodes in 64 32 16 8
do
  CMD="python3 01_distrdf.py -c 32 -N ${Nodes}"
  printf "\n\n${CMD}\n" >> ~/distrdf_timestamps.out
  eval "$CMD"
  mkdir "${dirn}/log_c32_N${Nodes}_tmp"
  mv *.out "${dirn}/log_c32_N${Nodes}_tmp"  # move the newly produced slurm logs
  echo "$CMD was done"
  killall python3
done

mv ~/distrdf_timestamps.out ./${dirn}


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

for cores in 8
do
  for nodes in 32 16 8 4 1
  do
    CMD="python3 distrdf.py -c ${cores} -N ${nodes}"
    printf "\n\n${CMD}\n" >> ~/distrdf_timestamps.out
    eval "$CMD"
    mkdir "${dirn}/log_c${cores}_N${nodes}"
    mv *.out "${dirn}/log_c${cores}_N${nodes}"  # move the newly produced slurm logs
    echo "$CMD was done"
    killall python3
  done
done

mv ~/distrdf_timestamps.out ./${dirn}


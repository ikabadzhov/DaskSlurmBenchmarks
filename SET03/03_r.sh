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

for Nodes in 8 16
do
  for p in 512 1024 2048
  do
    for ru in 1 2 3
    do
      CMD="python3 03_distrdf.py -c 32 -N ${Nodes} -f 1000 -p ${p} -r ${ru}"
      printf "\n\n${CMD}\n" >> ~/distrdf_timestamps.out
      eval "$CMD"
      mkdir "${dirn}/p${p}_N${Nodes}_r${ru}"
      mv *.out "${dirn}/p${p}_N${Nodes}_r${ru}"  # move the newly produced slurm logs
      mv *.html "${dirn}/p${p}_N${Nodes}_r${ru}"
      echo "$CMD was done"
      killall python3
    done
  done
done

mv ~/distrdf_timestamps.out ./${dirn}


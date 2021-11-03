#!/bin/sh

unlink ~/distrdf_timestamps.out  # remove the old logs (if any)
rm *.out
killall python3

while getopts d:N:f:p:r: flag
do
  case "${flag}" in
    d) dirn=${OPTARG};;
    N) nodes=${OPTARG};;
    f) files=${OPTARG};;
    p) pts=${OPTARG};;
    r) runs=${OPTARG};;
  esac
done

DIR="D${dirn}_N${nodes}_f${files}_p${pts}_r${runs}"
mkdir ${DIR}

CMD="python3 04_d.py -c 32 -N ${nodes} -f ${files} -p ${pts} -r ${runs}"
printf "\n\n${CMD}\n" >> ~/distrdf_timestamps.out
eval "$CMD"
mv *.out ${DIR}
mv *.html ${DIR}
echo "$CMD was done"
killall python3
mv ~/distrdf_timestamps.out ${DIR}


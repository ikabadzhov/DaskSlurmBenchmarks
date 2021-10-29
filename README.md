# Dask-Slurm-Benchmarks

### Temporary results of performing Dask+Slurm Benchmarks.

The setup should be in the bottom of the this document.

## Reading Results.

Use the summarizer to get an overview of the `distrdf_timestamps.out` logs.

For **SET00**, `runner_1` produced the logs in `28_1541` and `runner_2` produced the logs in `29_0846`. In this set, always the same `distrdf.py` file was used.

Example usage: `python3 summarizer.py SET00/28_1541` or `python3 summarizer.py SET00/29_0846` (pass the path to the logs as `sys.argv[1]`).

## SET00

This directory contains the first set of benchmark, which simply tries to perform computations on at most $32*48=1536$ number of cores.

In particular, the number of files is 365, the number of partitions is fixed to $2*32*48=3072$, requested memory is 8GiB per core. Varying are the number of nodes - 48, 32, 16, 8, 1; and cores 32, 16, 8.

From these initial tests, it is evident that when running on 32 cores, the running time for 8, 16, 32, 48 nodes is similar. After discussed on 29-th of October, possible factor that can lead to this behaviour are:

1. Large C++ event loop overheads. **Proposed Solution:** Increase the number of input files to 1 thousand and keep the number of partitions as before. This result should give us intuition on the I/O bandwidth.

2. Reading from user node might be expensive. **Proposed Solution:** Create a hard copy of the root files in `/tmp/` and perform experiments with 365 files and then 1k files.

Moreover, when asking for less than 16 cores on $N$ nodes, we cannot guarantee that $N$ nodes are allocated. Therefore, we will be passing `--exclusive` flag to the slurm cluster. (Clearly for the tests on 32 nodes this is irrelevant).

**And the test on 1 node with 8 cores was unsuccessful!** Likely, there is a need to change the memory requested. Potential issue is jitting.


## SET01

The number of input files is increased to 1000. The number of partitions is fixed to 8192. Summary of the results:

```
python3 01_distrdf.py -c 32 -N 64
cores=32 Nodes=64: Event Loop=110.8146300315857s
Timer from Base.py 0:01:35.396663
cores=32 Nodes=64: Event Loop=60.047252893447876s
Timer from Base.py 0:00:49.557640
cores=32 Nodes=64: Event Loop=60.26352095603943s
Timer from Base.py 0:00:47.751371

python3 01_distrdf.py -c 32 -N 32
cores=32 Nodes=32: Event Loop=77.42034387588501s
Timer from Base.py 0:00:57.876747
cores=32 Nodes=32: Event Loop=63.256885051727295s
Timer from Base.py 0:00:54.142023
cores=32 Nodes=32: Event Loop=63.057847023010254s
Timer from Base.py 0:00:53.574630

python3 01_distrdf.py -c 32 -N 16
cores=32 Nodes=16: Event Loop=116.56506299972534s
Timer from Base.py 0:01:45.160036
cores=32 Nodes=16: Event Loop=105.65866899490356s
Timer from Base.py 0:01:38.366808
cores=32 Nodes=16: Event Loop=106.29774904251099s
Timer from Base.py 0:01:38.426309

python3 01_distrdf.py -c 32 -N 8
cores=32 Nodes=8: Event Loop=206.1550431251526s
Timer from Base.py 0:03:14.995232
cores=32 Nodes=8: Event Loop=197.26038789749146s
Timer from Base.py 0:03:09.898729
cores=32 Nodes=8: Event Loop=197.8616771697998s
Timer from Base.py 0:03:09.858434
```

The results are yet to be discussed.





## Setup

First a proper conda environment setup is needed. All Installed packages when performing the tests are as follows:
```
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                 conda_forge    conda-forge
_openmp_mutex             4.5                       1_gnu    conda-forge
asyncssh                  2.7.2              pyhd8ed1ab_0    conda-forge
bcrypt                    3.2.0            py39h3811e60_1    conda-forge
bokeh                     2.4.0            py39hf3d152e_0    conda-forge
ca-certificates           2021.10.8            ha878542_0    conda-forge
cffi                      1.14.6           py39h4bc2ebd_1    conda-forge
click                     8.0.3            py39hf3d152e_0    conda-forge
cloudpickle               2.0.0              pyhd8ed1ab_0    conda-forge
cryptography              35.0.0           py39hbca0aa6_0    conda-forge
cytoolz                   0.11.0           py39h3811e60_3    conda-forge
dask                      2021.9.1           pyhd8ed1ab_0    conda-forge
dask-core                 2021.9.1           pyhd8ed1ab_0    conda-forge
dask-jobqueue             0.7.3              pyhd8ed1ab_0    conda-forge
decorator                 5.1.0              pyhd8ed1ab_0    conda-forge
distributed               2021.9.1         py39hf3d152e_0    conda-forge
freetype                  2.10.4               h0708190_1    conda-forge
fsspec                    2021.10.0          pyhd8ed1ab_0    conda-forge
heapdict                  1.0.1                      py_0    conda-forge
jbig                      2.1               h7f98852_2003    conda-forge
jinja2                    3.0.2              pyhd8ed1ab_0    conda-forge
jpeg                      9d                   h36c2ea0_0    conda-forge
krb5                      1.19.2               hcc1bbae_2    conda-forge
lcms2                     2.12                 hddcbb42_0    conda-forge
ld_impl_linux-64          2.36.1               hea4e1c9_2    conda-forge
lerc                      2.2.1                h9c3ff4c_0    conda-forge
libblas                   3.9.0           11_linux64_openblas    conda-forge
libcblas                  3.9.0           11_linux64_openblas    conda-forge
libdeflate                1.7                  h7f98852_5    conda-forge
libedit                   3.1.20191231         he28a2e2_2    conda-forge
libffi                    3.4.2                h9c3ff4c_4    conda-forge
libgcc-ng                 11.2.0              h1d223b6_11    conda-forge
libgfortran-ng            11.2.0              h69a702a_11    conda-forge
libgfortran5              11.2.0              h5c6108e_11    conda-forge
libgomp                   11.2.0              h1d223b6_11    conda-forge
liblapack                 3.9.0           11_linux64_openblas    conda-forge
libopenblas               0.3.17          pthreads_h8fe5266_1    conda-forge
libpng                    1.6.37               h21135ba_2    conda-forge
libsodium                 1.0.18               h36c2ea0_1    conda-forge
libstdcxx-ng              11.2.0              he4da1e4_11    conda-forge
libtiff                   4.3.0                hf544144_1    conda-forge
libwebp-base              1.2.1                h7f98852_0    conda-forge
libzlib                   1.2.11            h36c2ea0_1013    conda-forge
locket                    0.2.0                      py_2    conda-forge
lz4-c                     1.9.3                h9c3ff4c_1    conda-forge
markupsafe                2.0.1            py39h3811e60_0    conda-forge
msgpack-python            1.0.2            py39h1a9c180_1    conda-forge
ncurses                   6.2                  h58526e2_4    conda-forge
numpy                     1.21.2           py39hdbf815f_0    conda-forge
olefile                   0.46               pyh9f0ad1d_1    conda-forge
openjpeg                  2.4.0                hb52868f_1    conda-forge
openssl                   1.1.1l               h7f98852_0    conda-forge
packaging                 21.0               pyhd8ed1ab_0    conda-forge
pandas                    1.3.3            py39hde0f152_0    conda-forge
paramiko                  2.8.0              pyhd8ed1ab_0    conda-forge
partd                     1.2.0              pyhd8ed1ab_0    conda-forge
pillow                    8.3.2            py39ha612740_0    conda-forge
pip                       21.3               pyhd8ed1ab_0    conda-forge
psutil                    5.8.0            py39h3811e60_1    conda-forge
pycparser                 2.20               pyh9f0ad1d_2    conda-forge
pynacl                    1.4.0            py39h3811e60_2    conda-forge
pyopenssl                 21.0.0             pyhd8ed1ab_0    conda-forge
pyparsing                 2.4.7              pyh9f0ad1d_0    conda-forge
python                    3.9.7           hb7a2778_3_cpython    conda-forge
python-dateutil           2.8.2              pyhd8ed1ab_0    conda-forge
python-gssapi             1.7.2            py39hbb49be9_0    conda-forge
python_abi                3.9                      2_cp39    conda-forge
pytz                      2021.3             pyhd8ed1ab_0    conda-forge
pyyaml                    5.4.1            py39h3811e60_1    conda-forge
readline                  8.1                  h46c0cb4_0    conda-forge
setuptools                58.2.0           py39hf3d152e_0    conda-forge
six                       1.16.0             pyh6c4a22f_0    conda-forge
sortedcontainers          2.4.0              pyhd8ed1ab_0    conda-forge
sqlite                    3.36.0               h9cd32fc_2    conda-forge
tblib                     1.7.0              pyhd8ed1ab_0    conda-forge
tk                        8.6.11               h27826a3_1    conda-forge
toolz                     0.11.1                     py_0    conda-forge
tornado                   6.1              py39h3811e60_1    conda-forge
typing_extensions         3.10.0.2           pyha770c72_0    conda-forge
tzdata                    2021c                he74cb21_0    conda-forge
wheel                     0.37.0             pyhd8ed1ab_1    conda-forge
xz                        5.2.5                h516909a_1    conda-forge
yaml                      0.2.5                h516909a_0    conda-forge
zict                      2.0.0                      py_0    conda-forge
zlib                      1.2.11            h36c2ea0_1013    conda-forge
zstd                      1.5.0                ha95c52a_0    conda-forge
```


The [following ROOT version](https://github.com/vepadulano/root/tree/distrdf-dask-optimized) is used for the benchmarks. It is build inside the conda environment via `cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -Dbuiltin_xrootd=ON ../root`.

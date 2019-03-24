#! /bin/bash

module load python/3.6_gcc-7
module load cuda/8.0
module load cudnn/6.0_cuda-8.0
module load python-pytorch/0.4_python-3.6_gcc-5.4_cuda-8.0_cudnn-6.0
module load miniconda/4.5_python3.6

cd ../..

jupyter notebook --no-browser --port=$1

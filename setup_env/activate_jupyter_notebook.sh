#! /bin/bash

# navigate to
cd
cd Group_Software_1/miniconda/bin

source activate jupyter_env

cd ../../..

jupyter notebook --no-browser --port=8889

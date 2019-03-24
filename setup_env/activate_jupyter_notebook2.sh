#! /bin/bash

# navigate to
cd
cd Group_Software/miniconda/bin

source activate jupyter_env

cd ../../..

jupyter notebook --no-browser --port=8889

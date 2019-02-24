#! /bin/bash

function downloadAndInstall {
  url="$1"
  fileName="$softwareFolder/$(basename $url)"

  if [ ! -f "$fileName" ];
  then
    curl -o "$fileName" -L "$url"
    bash "$fileName" -b -p "$2"
    rm "$fileName"
  fi
}

#Navigate to home
cd

#make Software Directory
softwareFolder=Group_Software
mkdir -p $softwareFolder

#installing miniconda
softwareName=$softwareFolder/miniconda
downloadAndInstall "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh" "$softwareName"

#setting up environment for this project
cd $softwareName/bin
./conda create --name jupyter_env -y python=3.7 pandas=0.24.0 numpy=1.16.1 jupyter

source activate jupyter_env
conda install -y r-essentials=1.5.2
conda deactivate

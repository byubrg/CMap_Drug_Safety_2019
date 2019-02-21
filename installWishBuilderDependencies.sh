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

#make Software Directory
cd #Return to home directory
softwareFolder=Software
mkdir -p $softwareFolder

#installing miniconda
softwareName=$softwareFolder/miniconda
downloadAndInstall "https://repo.continuum.io/miniconda/Miniconda3-4.3.27.1-Linux-x86_64.sh" "$softwareName"

#setting up environment for this project
export PATH=$softwareName/bin:$PATH
conda create --name WishBuilderDependencies2 -y python=2.7 pandas=0.20.3 numpy=1.13.0 hdf5=1.10.1 h5py=2.7.1 xlrd=1.1.0


source activate WishBuilderDependencies
conda install -y r-essentials=1.5.2
source deactivate WishBuilderDependencies


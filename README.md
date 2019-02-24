# CMAP DRUG Challenge 2019

## Running Jupyter notebook

1. Install software

```{bash}
bash setup_env/install_env.sh
```

2. Forward port - you will have to run 2 and 3 in a separate terminal

```{bash}
ssh -N -L localhost:8888:localhost:8889 username@ssh.fsl.byu.edu
```

3. Run jupyter notebook on super computer

Navigate to our project folder on the super computer

```{bash}
bash setup_env/activate_jupyter_notebook.sh
```

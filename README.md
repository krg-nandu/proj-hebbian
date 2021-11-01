# proj-hebbian
To run basic script use

CUDA_VISIBLE_DEVICES=[0,1..] python main.py

# New user on serre-nodes
```
mkdir /media/data/conda/$USER
touch /media/data/conda/$USER/test && ls -al /media/data/conda/$USER/test
cp ~/.bashrc ~/bashrc.backup

export CONDA_PKGS_DIRS="/media/data/conda/pkgs"
export CONDA_ENVS_DIRS="/media/data/conda/$USER/envs"
export PATH=/media/data/anaconda/bin:$PATH

conda init
```

Edit ~/.bashrc and add following before the # >>> conda initialize >>> line
```
export CONDA_PKGS_DIRS="/media/data/conda/pkgs"
export CONDA_ENVS_DIRS="/media/data/conda/$USER/envs"
```
Exit session and log back in!

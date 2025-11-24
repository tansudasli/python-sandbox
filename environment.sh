# create env
conda create -n core python=3

conda install -n core ipykernel
conda install -n core numpy scipy pandas #matplotlib scikit-learn jupyterlab seaborn

conda activate core 
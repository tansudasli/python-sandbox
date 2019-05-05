#!/usr/bin/env bash
# create an GCP compute instance from ubuntu image, then ssh

# download anaconda
wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
bash Anaconda3-2019.03-Linux-x86_64.sh
source .bashrc

jupyter notebook --generate-config


echo "c = get_config()" >> .jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.ip = 'localhost'" >> .jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.open_browser = False" >> .jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.port = 5000" >> .jupyter/jupyter_notebook_config.py


jupyter notebook --ip=0.0.0.0 --port=5000 --no-browser &

#open external_ip:5000 in your browser

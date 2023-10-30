# LinRec

All files are conducted in the RecBole framework, and the link to RecBole is https://www.recbole.io/do.

The requirements are the same as RecBole as below:
torch>=1.10.0
numpy>=1.17.2
scipy>=1.6.0
hyperopt==0.2.5
pandas>=1.0.5
tqdm>=4.48.2
scikit_learn>=0.23.2
pyyaml>=5.1.0
colorlog==4.7.2s
colorama==0.4.4
tensorboard>=2.5.0
thop>=0.1.1.post2207130030
ray>=1.13.0
tabulate>=0.8.10 
plotly>=4.0.0
RecBole requires Python version 3.7 or later.
RecBole requires torch version 1.7.0 or later. If you want to use RecBole with GPU,
please ensure that CUDA or cudatoolkit version is 9.2 or later.
This requires NVIDIA driver version >= 396.26 (for Linux) or >= 397.44 (for Windows 10).

Then, you may substitute the 'Layers' file (recbole/model) in Recbole. Also, other special configuration files (e.g., 'ml-1m.yaml') are included. You must replace them in RecBole (recbole/properties). Otherwise, errors may occur.

Now, You can run the run.py

You can follow the instructions of RecBole for other operations. 

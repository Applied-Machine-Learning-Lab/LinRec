# LinRec

Source code of [LinRec: Linear Attention Mechanism for Long-term Sequential Recommender Systems](https://dl.acm.org/doi/10.1145/3539618.3591717)

All files are conducted in the RecBole framework, and the link to RecBole is [https://github.com/RUCAIBox/RecBole](https://github.com/RUCAIBox/RecBole).
## Environments
The requirements are the same as RecBole as below: <br>
torch>=1.10.0 <br>
numpy>=1.17.2 <br>
scipy>=1.6.0 <br>
hyperopt==0.2.5 <br>
pandas>=1.0.5 <br>
tqdm>=4.48.2 <br>
scikit_learn>=0.23.2 <br>
pyyaml>=5.1.0 <br>
colorlog==4.7.2 <br>
colorama==0.4.4 <br>
tensorboard>=2.5.0 <br>
thop>=0.1.1.post2207130030 <br>
ray>=1.13.0 <br>
tabulate>=0.8.10  <br>
plotly>=4.0.0 <br>
RecBole requires Python version 3.7 or later.
RecBole requires torch version 1.7.0 or later. If you want to use RecBole with GPU,
please ensure that CUDA or cudatoolkit version is 9.2 or later.
This requires NVIDIA driver version >= 396.26 (for Linux) or >= 397.44 (for Windows 10).
## Implementations
Then, you may substitute the 'layers.py' file ('recbole/model') in Recbole. 

- Config: Other special configuration files (e.g., 'overall.yaml', 'ml-1m.yaml') are included. You must replace them in RecBole ('overall.yaml' -> 'recbole/properties/'; 'ml-1m.yaml' -> 'recbole/properties/dataset/'). Otherwise, errors may occur.

- Data: You have to download the datasets to be used: e.g., **ml-100k**, **ml-1m**, **gowalla**, where we provide the **ml-1m** for convenience. Then put the downloaded dataset into the 'dataset/' directory in Recbole, like **ml-100k**.

- Hyperpara: The most critical parameters are $N$ ('MAX_ITEM_LIST_LENGTH') and $d$ ('hidden_size'), which are set in 'ml-1m.yaml' and 'run.py'. Please make sure the values conform to settings in the paper, e.g., $N=200$, $d=128$ for the ml-1m dataset.

Now, You can run the **run.py** file for a quick start.
You can follow the instructions of RecBole for other operations. 

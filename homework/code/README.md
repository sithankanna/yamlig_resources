# Homework

## Repo Structure  

```bash
├── README.md
├── data
│   ├── ...csv
│   ├── ...csv
├── output
│   └── ....
├── docs
│   └── ....
├── env.yml
├── notebooks
│   ├── JaneDoe_Homework.ipynb
└── src
    ├── eda.py
    └── main.py
```

* The source code is in `src/`
* A Notebook that runs the model with some explanatory text is in `notebooks/JaneDoe_Homework.ipynb`


## Setup

Creating a conda environment with the `env.yml` file will create a conda environment called `homework` with all the dependencies needed to run the notebook and python script.

```bash
conda env create -f env.yml
conda activate homework
jupyter-notebook
```

## Generating the Output

Navigate to the `code` folder and run 
```bash
conda activate homework
python src/main.py
```



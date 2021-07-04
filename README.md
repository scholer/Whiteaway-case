Whiteaway-2021
==============================

Whiteaway case opgave Juni-Juli 2021.






Environment
-----------

Conda environment:

```cmd
conda create -n data-whiteaway python numpy pandas notebook seaborn networkx requests sphinx coverage flake8
conda install -c conda-forge --no-deps python_abi python-dotenv
conda activate data-whiteaway
```

Alternatively, from conda-forge

```cmd
conda create -n whiteaway-cf -c conda-forge python numpy pandas notebook seaborn holoviews bokeh hvplot panel param networkx requests sphinx coverage flake8 python-dotenv
conda activate data-whiteaway-cf
conda config --prepend channels conda-forge  # --prepend same as --add
conda config --remove channels defaults      # only needed if you really want to exclude default channels.
```


### Reproducible/locked environments:

Options for creating reproducible/locked environments:

* With `conda`: use `conda list --export > envs/conda-list-export.txt` 
  to create exact package specification. 
  You can re-create environment with `conda create --name <env> --file <this file>`.
  (You should make a manual note of the conda channels used to install the packages.)

* With `pipenv`, use `pipenv lock`. This will create `Pipenv.lock` file.
  Recreate environment using `pipenv install`.



Running tests
--------------

Tests are run using pytest (from the project root):

    python -m pytest



Project Organization
---------------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


File layout with datadriven's default V1 cookie cutter template:

```
cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
```




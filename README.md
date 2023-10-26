# Science template

This is a minimal template for my (data) science projects. Requires [poetry](https://python-poetry.org/).

# Usage

After creating a new repository from this template simply run ```make install```.

The template has the following structure:

```
.
├── Makefile
├── README.md
├── computations
├── config
│   └── main.yaml
├── data
│   ├── 00_external
│   ├── 01_raw
│   ├── 02_interim
│   └── 03_processed
├── notebooks
│   └── X.0X-template.ipynb
├── output
├── poetry.lock
├── pyproject.toml
├── scripts
│   └── execute_notebooks.sh
└── src
    ├── __init__.py
    └── utils
        ├── __init__.py
        ├── colors.py
        └── styling.py
```

This is a reduced version of what you might find when using the standard ```cookiecutter-data-science``` template with the addition of relying on [poetry](https://python-poetry.org/) for package management.

```data``` holds all necessary external, raw and derived data. All ```jupyter```-notebooks are supposed to in ```notebook```. Visual output is placed in ```output```.

```scripts``` holds all shell-scripts and other potential helpers. Modify ```execute_notebooks.sh``` in order to execute a chosen set of ```jupyter```-notebooks. This is pretty useful when you have a couple of ```jupyter```-notebooks that put figures into ```output``` and want to run all of them at once.

```src``` is installed in the project's virtual environment. Use it to package code that you want to use in your notebooks. Includes a small collection of preset functionality that I typically need.

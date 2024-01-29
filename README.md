# Data science template

This is a minimal template for my (data) science projects. Requires [poetry](https://python-poetry.org/).

# Usage

After creating a new repository from this template simply run ```make install```.

The template has the following structure:

```
.
├── Makefile                        # frequently used commands, see the file for details
├── README.md                       #
├── computations                    # computations and results go here
├── config                          # config files for hydra
│   └── main.yaml                   #     
├── data                            # data folder
│   ├── 00_external                 # data from external sources
│   ├── 01_raw                      # raw and unaltered input data  
│   ├── 02_interim                  # interim or partly processed data
│   └── 03_processed                # final data for analysis
├── notebooks                       # all jupyter notebooks
│   └── X.0X-template.ipynb         # a basic template with a hydra setup
├── output                          # figures and other output
├── pyproject.toml                  # basic poetry setup
├── scripts                         # bash scripts
│   └── execute_notebooks.sh        # execute jupyter notebooks from the command line
└── src                             # package source code
    ├── __init__.py                 #   
    ├── template.py                 # again, a minimal template for source files including hydra
    └── utils                       # frequently used helpers 
        ├── __init__.py             #    
        ├── colors.py               # my custom colors for creating figures
        ├── db_utils.py             # connect to a PostgreSQL database
        └── styling.py              # custom styling for matplotlib figures
```

This is a reduced version of what you might find when using the standard ```cookiecutter-data-science``` template with the addition of relying on [poetry](https://python-poetry.org/) for package management.

```data``` holds all necessary external, raw and derived data. All ```jupyter```-notebooks are supposed to be placed in ```notebooks```. Visual output is put in ```output```. If you use the template notebook a new timestampled subfolder is created under ```output``` whenever you restart the jupyter kernel. This is to keep track of older versions of figures. 

```scripts``` holds all shell-scripts and other potential helpers. Modify ```execute_notebooks.sh``` in order to execute a chosen set of ```jupyter```-notebooks. This is pretty useful when you have a couple of ```jupyter```-notebooks that put figures into ```output``` and you want to run all of them at once.

```src``` is installed in the project's virtual environment. Use it to package code that you want to use in your notebooks. Includes a small collection of preset functionality that I typically need.

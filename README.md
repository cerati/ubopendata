# ubopendata


## Local Setup

These set of notebooks can be run from a conda environment (or similar setup) that includes the following packages and their dependents: python=3.7, scipy, jupyter, matplotlib, h5py\[version='>=2.9',build=mpi*\], plotly, pandas, particle, mpi4py.
Plus the pynuml package for helper functions used to easily access information in the files.

Recipe:
```
to do
```

## Overview of the notebooks

Each notebook can be independently executed and serves a specific purpose. 

We recommend starting from `Sample Exploration.ipynb`, as it provides simple instructions about accessing basic information from the input files, as well an introduction to other tools made available for understanding the detector properties.

`Hit Labeling.ipynb`

`WireImage.ipynb`

`Pandora metrics.ipynb`

`Optical Information.ipynb`

`detector_utils.py`

`plot_utils.py`


## Structure and content of input files

The structure and content of the hdf5 input files can be found at this document:
https://docs.google.com/spreadsheets/d/1ri2RgiwiRhoG6BNuaD5g3u9WDbD_K7AQXj3jWWWSWUU/edit?usp=sharing,
where each element in the file is documented in terms of its name, type, size, and a human readable description.

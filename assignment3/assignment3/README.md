
Install after downloading:  Navigate to folder in CMD and install running pip install .
pip install -e . will make the package editable

Description: Package that applies filtering to a picture of choice, color2gray OR color2sepia

Dependencies: importlib-metadata, numpy, numba, pillow, matplotlib, cython, line_profiler

Versions: platform win32 -- Python 3.8.0, pytest-7.1.3, numpy == 1.21.5, numba 0.56.2, Cython version 0.29.32, pillow (9.2.0), importlib-1.0.4, matplotlib  (1.16.0), line_profiler (3.5.1)

versions can be installed from CMD --> python pip install numpy/

Cython:
To run Cython files, you need a C - compiler installed
Change setup.py --> use_cython == True
Wen changes are made to the Cython-code run python(version) build_ext --inplace

INSTRUCTIONS:

Run from terminal:
- navigate to folder assignment3 --> get instructions with instapy test/rain.jpg

Add file e.g test/rain.jpg, conditional
For filtered image: test/rain.jpg -i python/numba/numpy/cython -se sepia/-g gray
For saving: -s save - saves file in package directory 
For resizing: -re resize (used for time consuming resolutions)
For timing: python(version) -m instapy.timing

Example: instapy test/rain.jpg -i python -se sepia -s save
This will save an imp of pure python with sepia filter to file in assignment3/test folder

Testing:
- install pytest --> pytest -v test/test_package.py
- run pytest from terminal in assignment3 folder
 

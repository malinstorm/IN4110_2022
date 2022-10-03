
Install after downloading:  Navigate to folder in CMD and install running pip install .
pip install -e . will make the package editable

Description: Package that applies filtering to a picture of choice, color2gray OR color2sepia
Dependencies: importlib-metadata, numpy, numba,pillow, matplotlib, cython, line_profiler
versions: platform win32 -- Python 3.8.0, pytest-7.1.3, 
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

 

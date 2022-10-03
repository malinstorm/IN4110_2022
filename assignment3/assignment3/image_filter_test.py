# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:36:15 2022

@author: 61144
"""

import numpy as np
#cimport numpy as np
from PIL import Image
from numba import jit
from numpy import arange
#from in_out import *

from instapy.io import *
from instapy.python_filters import *
from instapy.numpy_filters import *
from instapy.numba_filters import *
from instapy.cython_filters import *

# import the picture
filename = "test/rain.jpg" #jazzmaster.jpg
pixels = read_image(filename) #converting pic to np.array
#image = Image.fromarray(pixels)
#display(pixels)

#grayscale conversion Pure Python
#image1 = python_color2gray(pixels)
#display(image1)

#grayscale conversion Numpy
#image2 = numpy_color2gray(pixels)
#display(image2)

#grayscale conversion jit
#image3 = numba_color2gray(pixels)
#display(image3)

#grayscale conversion cython
#image4 = cython_color2gray(pixels)
#display(image4)

#sepia python
#sepia1 = python_color2sepia(pixels)
#display(sepia1)

#sepia numpy
sepia2 = numpy_color2sepia(pixels)
display(sepia2)
#sepia numba
#sepia3 = numba_color2sepia(pixels)
#display(sepia3)

#sepia cython
#sepia4 = cython_color2gray(pixels)
#display(sepia4)

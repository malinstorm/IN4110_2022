import numpy as np
cimport numpy as np
from PIL import Image
from instapy.io import *

def cython_color2gray(np.ndarray[np.uint8_t, ndim=3] image): #image
#getting shape, defining array
  cdef int height=image.shape[0], width=image.shape[1]
  cdef np.ndarray[np.float64_t, ndim=3] gray_image = np.empty(shape=(height, width, 3), dtype=np.float64)
  cdef int i, j
#iterating through pixels
  for i in range(height):
           for j in range(width):
              gray_image[i,j,0] =  gray_image[i,j,1] = gray_image[i,j,2] = 0.21 * image[i,j,0] + 0.72 * image[i,j,1] +  0.07 * image[i,j,2]
  return gray_image.astype("uint8")


def cython_color2sepia(np.ndarray[np.uint8_t, ndim=3] image):
#getting shape, defining arrays, defining sepia-matrix
  cdef int height = image.shape[0], width = image.shape[1]
  cdef np.ndarray[np.float64_t, ndim=3] sepia = np.empty(shape=(height, width, 3), dtype=np.float64)
  cdef np.ndarray[np.float64_t, ndim=2] sepia_matrix = np.array([[0.393,0.769,0.189],[0.349,0.686,0.168],[0.272,0.534,0.131]])

  cdef int i, j
  cdef int max = 255
  cdef float red, green, blue

  for i in range(height):
    for j in range(width):
# adding the values on each channel
      red = image[i,j,0] * sepia_matrix[0][0] + image[i,j,1] * sepia_matrix[0][1] + image[i,j,2] * sepia_matrix[0][2]
      green = image[i,j,0] * sepia_matrix[1][0] + image[i,j,1] * sepia_matrix[1][1] + image[i,j,2] * sepia_matrix[1][2]
      blue = image[i,j,0] * sepia_matrix[2][0] + image[i,j,1] * sepia_matrix[2][1] + image[i,j,2] * sepia_matrix[2][2]
# setting max = 255 for values that override
      if red > max:
        sepia[i,j,0] = max
      else:
        sepia[i,j,0] = red
      if green > max:
        sepia[i,j,1] = max
      else:
        sepia[i,j,1] = green
      if blue > max:
        sepia[i,j,2] = max
      else:
        sepia[i,j,2] = blue

  return sepia.astype("uint8")

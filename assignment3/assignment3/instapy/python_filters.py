"""pure Python implementation of image filters"""

import numpy as np


def python_color2gray(image: np.array) -> np.array:
     #making a copy of original array
    gray_image = np.empty_like(image)
    width,height,rgb = len(image[0]),len(image),len(image[0][1]) #values of dimensions for array

    red, green, blue = 0.21, 0.72, 0.07 # weighting for RGB

    # iterate through the , and apply the grayscale transform
    for i in range(height): #299
        for j in range(width): #168
            #for k in range(rgb):
            gray_image[i,j,0] =  gray_image[i,j,1] = gray_image[i,j,2] = red * image[i,j,0] + green * image[i,j,1] +  blue * image[i,j,2]

    gray_image = gray_image.astype("uint8")

    return gray_image



def python_color2sepia(image: np.array) -> np.array:

    sepia_matrix = np.array([[0.393,0.769,0.189],[0.349,0.686,0.168],[0.272,0.534,0.131]])
    sepia = np.empty_like(image)
    max = 255
    width,height = len(image[0]),len(image)

    for i in range(height):
        for j in range(width):
            red = image[i,j,0] * sepia_matrix[0][0] + image[i,j,1] * sepia_matrix[0][1] + image[i,j,2] * sepia_matrix[0][2]
            green = image[i,j,0] * sepia_matrix[1][0] + image[i,j,1] * sepia_matrix[1][1] + image[i,j,2] * sepia_matrix[1][2]
            blue = image[i,j,0] * sepia_matrix[2][0] + image[i,j,1] * sepia_matrix[2][1] + image[i,j,2] * sepia_matrix[2][2]

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
    

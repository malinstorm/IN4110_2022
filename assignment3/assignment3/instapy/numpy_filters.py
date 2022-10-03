"""numpy implementation of image filters"""

from typing import Optional
import numpy as np

def numpy_color2gray(image: np.array) -> np.array:
    # defining array same size as image
    gray_image = np.empty_like(image)

    r, g, b = 0.21, 0.72, 0.07 # weighting for RGB
    # slicing the array
    gray_image[:,:,0] =  gray_image[:,:,1] = gray_image[:,:,2] = r * image[:,:,0] + g * image[:,:,1] +  b * image[:,:,2]

    return gray_image.astype("uint8")


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """k (float): amount of sepia filter to apply (optional)
    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.
    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)
    """
    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")
    
    # defining sepia matrix
    sepia_matrix = np.array([[0.393,0.769,0.189],[0.349,0.686,0.168],[0.272,0.534,0.131]])
    sepia_image = np.empty_like(image)
    max = 255
    width,height = len(image[0]),len(image)

    #tar verdiene
    red = image[:,:,0] * sepia_matrix[0][0] + image[:,:,1] * sepia_matrix[0][1] + image[:,:,2] * sepia_matrix[0][2]
    green = image[:,:,0] * sepia_matrix[1][0] + image[:,:,1] * sepia_matrix[1][1] + image[:,:,2] * sepia_matrix[1][2]
    blue = image[:,:,0] * sepia_matrix[2][0] + image[:,:,1] * sepia_matrix[2][1] + image[:,:,2] * sepia_matrix[2][2]

    #sjekker at verdiene ikke overstiger max = 255
    red[red > max] = max
    green[green > max] = max
    blue[blue > max] = max

    sepia_image[:,:,0], sepia_image[:,:,1], sepia_image[:,:,2] = red, green, blue

    return sepia_image.astype("uint8")

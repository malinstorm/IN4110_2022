from instapy.python_filters import python_color2gray, python_color2sepia
from instapy.io import *
from instapy.__init__ import get_filter

def test_color2gray(image):
    color2gray = get_filter("color2gray","python") #henter funksjonsnavn
    #run color2gray
    test = color2gray(image)
    #test shape, dim, array
    assert np.shape(test) == np.shape(image)
    assert test.ndim == image.ndim == 3
    assert type(test) == type(image) == np.ndarray

    #tester ppt på alle akser
    assert test[100][0][0] == test[100][0][1] == test[100][0][2]
    assert test[160][179][0] == test[160][179][1] == test[160][179][2]
    assert test[100][319][0] == test[100][319][1] == test[100][319][2]

    # check that the result has the right shape, type = uint8 np.ndarray
    #assert r[0] == r[1] == r[2]
    # assert uniform r,g,b values ER DE LIKE PÅ HVER LINJE?
    ...

def test_color2sepia(image):
    color2sepia = get_filter("color2sepia","python") #henter funksjonsnavn
    #run color2sepia
    test = color2sepia(image)
    #test shape, dim, array
    assert np.shape(test) == np.shape(image)
    assert test.ndim == image.ndim == 3
    assert type(test) == type(image) == np.ndarray

    #tester at verdiene for en kanal ikke overstiger 255
    assert test[100][0][0] and test[100][0][1] and test[100][0][2] < 255
    assert test[160][179][0] and test[160][179][1] and test[160][179][2] < 255
    assert test[100][319][0] and test[100][319][1] and test[100][319][2] < 255

    # check that the result has the right shape, type = uint8 np.ndarray
    ...
    # verify some individual pixel samples F EKS IKKE STØRRE ENN 255
    # according to the sepia matrix

filename = "rain.jpg"
pixels = read_image(filename)
test_color2gray(pixels)
test_color2sepia(pixels)

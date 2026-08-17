from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
from instapy.io import *
from instapy.__init__ import get_filter
import numpy.testing as nt


def test_color2gray(image, reference_gray):
    color2gray = get_filter("color2gray","numpy") #henter funksjonsnavn
    #run color2gray
    test = color2gray(image)

    print(np.shape(test))
    print(np.shape(reference_gray))
    #test shape, dim, array
    assert np.shape(test) == np.shape(image)
    assert test.ndim == image.ndim == 3
    assert type(test) == type(image) == np.ndarray

    #tester ppt på alle akser
    assert test[100][0][0] == test[100][0][1] == test[100][0][2]
    assert test[160][179][0] == test[160][179][1] == test[160][179][2]
    assert test[100][319][0] == test[100][319][1] == test[100][319][2]

    #sjekker at verdiene holder seg innenfor et tolererbart nivå
    nt.assert_allclose(test,reference_gray)
    np.allclose(test,reference_gray)

def test_color2sepia(image, reference_sepia):
    color2sepia = get_filter("color2sepia","numpy") #henter funksjonsnavn
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

    #sjekker at verdiene holder seg innenfor et tolererbart nivå
    nt.assert_allclose(test,reference_sepia,1)
    np.allclose(test,reference_sepia)


filename = "test/rain.jpg"
pixels = read_image(filename)
ref_filter1 = get_filter("color2gray","python")
test_color2gray(pixels, ref_filter1(pixels))
ref_filter2 = get_filter("color2sepia","python")
test_color2sepia(pixels, ref_filter2(pixels))

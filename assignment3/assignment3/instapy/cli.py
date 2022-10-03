"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from instapy.io import *
from instapy.python_filters import *
from instapy.__init__ import get_filter

def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "",
    filter: str = "",
    scale: int = 1, #if there is need for resizing
    ) -> None:
    #Run the selected filter
    # load the image from a file
    image = read_image(file) #array
    
    if scale != 1:
        # Resize image, if needed
        resized = np.resize(image, (image.shape[0] // 2, image.shape[1] // 2,3))
        # Apply the filter
        filter_string = get_filter(filter,implementation) #henter streng fra get_filter
        filtered = filter_string(resized)
    else:
    # Apply the filter
        filter_string = get_filter(filter,implementation) #henter streng fra get_filter
        filtered = filter_string(image)
    # save the file
    if out_file:
        write_image(filtered,"test/filtered.jpg")
    else:
        # not asked to save, display it instead
        display(filtered)


def main(argv=None):
    #Parse the command-line and call run_filter with the arguments
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-help",help="Show this help message and exit" )
    parser.add_argument("-o", "--out", help="The output filename")
    parser.add_argument("-g", "--gray", help="Select Gray filter")
    parser.add_argument("-se", "--sepia", help="Select Sepia filter")
    parser.add_argument("-i", "--implementation", help={"python","numba","numpy","cython"})
    parser.add_argument("-s","--save", help="Save to file")
    parser.add_argument("-re","--resize", help="Resize image if too large resolution")
    # Add required arguments
    args = parser.parse_args()

    # run Options menu and makes sure that program doesen't try running if wrong conditions
    if args.file and not(args.implementation):
        print("Package that applies filtering to a picture of choice, color2gray OR color2sepia")
        print("Instructions:")
        print("Add file e.g test/rain.jpg, conditional.")
        print("For filtered image: test/rain.jpg -i python/numba/numpy/cython -se sepia/-g gray")
        print("For saving: -s save")
        print("For resizing: -re resize")
        print("For timing: python(version) -m instapy.timing")
        # parse arguments and call run_filter
    if args.sepia and args.implementation:
        filter = "color2sepia"
        if args.resize:
            scale = 2
        else: scale = 1
        if args.save:
            save = "Yes"
        else: save = ""
        run_filter(args.file,save,args.implementation,filter,scale)

    if args.gray and args.implementation:
        filter = "color2gray"
        if args.resize:
            scale = 2
        else: scale = 1
        if args.save:
            save = "Yes"
        else: save = ""
        run_filter(args.file,save,args.implementation,filter,scale)

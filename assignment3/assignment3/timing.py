"""
Timing our filter implementations.

Can be executed as `python3 -m instapy.timing`

For Task 6.
"""
import time
import instapy
#from . import io
from instapy.io import *
from typing import Callable
import numpy as np

from instapy.__init__ import get_filter
from instapy.python_filters import *
from instapy.numba_filters import *
from instapy.numpy_filters import *
from instapy.cython_filters import *

def time_one(filter_function: Callable, arguments, calls: int = 3) -> float:

    timer = 0 #for å summere for hvert kall på funksjon
    start_time = time.process_time() #CPU starttid

    for i in range(calls):
        image = filter_function(arguments) #kaller funksjon fra instapy.*_filters
        end_time = time.process_time() #CPU endetid
        timer += end_time - start_time #totaltid summert
    if timer == 0.0: #to avoid division by zero
        raise Exception("Your machine is too fast, try again")

    return float(timer/calls) #returnerer gjennomsnitt på antall kall

def make_reports(filename: str = "test/rain.jpg", calls: int = 3):

    # load the image
    pixels = read_image(filename) #converts image to np.array
    # print the image name, width, height
    print("Image name:", filename," ",(len(pixels)),"x",len(pixels[0]))

    filter_names = ["color2gray","color2sepia"] #til utprint

    file = open('timing-report.txt','w') #åpner for skriving til fil før løkke starter
    # iterate through the filters
    for filter_name in range(len(filter_names)): # kjører 2 ganger
        # get the reference filter function
        reference_filter = get_filter(filter_names[filter_name],"python") #filter_names[filter_name] #mat til funksjon time_one()
        # time the reference implementation
        reference_time = time_one(reference_filter,pixels,calls) #kaller timer

        print(
            f"Reference (pure Python) filter time {filter_names[filter_name]}: {reference_time:.3}s ({calls=})"
        )
        file.write("%s %s%s %s%s %s %s%s" %("Reference (pure Python) filter time", filter_names[filter_name],":",reference_time,"s", "calls =",calls,"\n"))

        implementations = ["numpy","numba","cython"]
            # iterate through the implementations
        for implementation in range(len(implementations)):

            if filter_name == 0: #sjekker index for å skille mellom color2gray og Sepia
                implementation_name = "color2gray"
            else:
                implementation_name = "color2sepia"

            filter = get_filter(implementation_name,implementations[implementation])#filter_implementation_name[implementation] #mat til time_one()

            # time the filter
            filter_time = time_one(filter,pixels,calls) #kaller timer for å kunne sammenligne med ref pure python
            # compare the reference time to the optimized time
            speedup = float(reference_time/filter_time)

            print(
                f"Timing: {implementations[implementation]} {implementation_name}: {filter_time:.3}s ({speedup=:.2f}x)"
            )
            file.write("%s %s %s%s %s%s %s %s%s%s" %("Timing:",implementations[implementation],implementation_name,":",filter_time,"s", "speedup=",speedup,"x","\n"))
    file.close() #lukker fil på utsiden av løkke for å unngå at noe overskrives

if __name__ == "__main__":
    # run as `python -m instapy.timing`
    make_reports()

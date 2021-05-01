#!/usr/bin/env python3

import sys
from PIL import Image
import numpy as np

#chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))

#chars = np.asarray(list('@%#*+=-:. '))

chars = np.asarray(list("\u2588\u2589\u258a\u258b\u258c\u258d\u258e\u258f\u2593\u2592\u2591"))
chars = np.asarray(list("\u2593\u2592\u2591"))


#chars = np.asarray(list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "))

filename="default.jpg.2"
scaling=.05
intensity_corr=1.0
width_corr=7/4

img = Image.open(filename)
newsize = ( round(img.size[0]*scaling*width_corr), round(img.size[1]*scaling) )

img = np.sum( np.asarray( img.resize(newsize) ), axis=2)
print(img)
img -= img.min()
print(img)
img = (1.0 - img/img.max())**intensity_corr*(chars.size-1)
print(img)
#print( "\n".join( ("".join(r) for r in chars[img.astype(int)]) ) )

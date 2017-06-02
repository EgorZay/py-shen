import glob
import struct
import imghdr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

def get_image_size(fname):
    '''Determines the image type of fhandle and returns its size in pixels.
    Input: ``fname`` -- path to file;
    Returns: tuple of width and height of an ``fname``.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return width, height

# No need to understand the module above in case you wonder

size = []
for fname in glob.glob('*.jpg'):  # glob is to iterate through files in a directory
    size.append(get_image_size(fname))  # receives width and height tuple

size = pd.DataFrame(size)
w = np.max(size[0]); h = np.max(size[1])  # receives the highest width and height pixel values of the largest image in a directory

#TODO: prohibit plt from showing as it increases idling

T1 = time.time()
for fname in glob.glob('*.jpg'):  # it actually places images in a directory to the center of a plot with w, h axes
    img = plt.imread(fname)
    fig = plt.figure(figsize=(float(w) / float(500), float(h) / float(500)), dpi=100)
    plt.figimage(img, cmap='Greys', xo=w / 2 - img.shape[1] / 2, yo=h / 2 - img.shape[0] / 2)
    plt.savefig('centered_' + fname, dpi=500)
    plt.close()
T2 = time.time()
print('Take taken to reprocess images (min): {}'.format(60*(T2-T1)))

# use this if you try to reprocess images and normalize them for machine learning
# i have once stumbled on a problem where i had enough data to build a model
# but all the inputs (.jpg images) were differently sized
# so i had to approach the problem of normalization
# basic rescaling is not a valid choice and rather obsolete
# this script preserves initial input sizes and structure
# and in general is a better option to perform a normalization

import PIL.Image as Image
import scipy.misc as smisc
import os
import glob

img_path = '/path/to/default/images/'
resized_path = '/path/to/resized/images'
resized_path_2 = '/path/to/resized_2/images/'
count = 0  # iterator
w = 1706  # default width
h = 1089  # default height

os.chdir(img_path)
for fname in glob.glob('*.png'):
    img = Image.open(fname)
    img_resized = smisc.imresize(img, (109, 171))
    smisc.imsave(resized_path + fname, img_resized)
    count += 1
    print(count)

os.chdir(resized_path)
for fname in glob.glob('*.png'):
    img = Image.open(fname)
    img_resized = smisc.imresize(img, (28, 43))
    smisc.imsave(resized_path_2 + fname, img_resized)
    count += 1
    print(count)

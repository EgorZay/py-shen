# .py

### Python basic snippets leading to better understanding of its shell

#### alignment of images in ``matplotlib`` library

Added .py to approach a problem of normalization of image inputs

Basic rescaling is not robust in general so i have added another option to normalize inputs. Choose this option if the inputs are differently sized.

Basically, the algorithm is the following:

1. ``align_image_to_center_of_plot.py`` iterates through the available data inputs in a directory

2. Loads and stores image sizes in a list of tuples as width and height

3. Chooses the highest WIDTH and HEIGHT found

4. Creates a canvas without axes with the appropriate sizes, where X - WIDTH, Y - HEIGHT

5. Plots an image to the exact center of a canvas with cmap='Greys' (greyscaled color map)

6. Saves an image.jpg with the appropriate sizes

7. Repeats until deadend. Prints runtime

E.

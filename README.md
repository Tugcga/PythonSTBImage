# What is it

This is Python Windows bindings for stb_image and stb_image_write c++ libraries ([link](https://github.com/nothings/stb)). These libraries used for reading and writing images in png, jpg, bmp, tga and hdr formats. Created by using [PyBind11](https://github.com/pybind/pybind11). Works in Python 2.7 and 3.x, but use different binary modules for different versions of the Pyhon.

# How to use

Import module

```python
import stbi
```

The module contains 4 functions: two function for loading images and two ones for writing it.

```python
stbi.load(filepath)
stbi.load_float(filepath)
```

These functions load image by it full path and return the tuple (width, height, channels, pixels). Pixels are plane list of integers or floats (for `load_float` function), which contains data for each pixel of the image. At first it contains several values for the first pixel, then for the second one and so on...

When an image is loaded in float mode (by using `load_float` function), then pixels values returned without gamma compensation. For example, if the pixel in LDR mode has values `[128, 128, 128]` then in HDR mode it has values `[0.22, 0.22, 0.22]`.

```python
stbi.write(filepath, width, height, components, pixels)
stbi.write_float(filepath, width, height, components, pixels)
```

These function write pixels to images. Input parameters have the same sense as in load functions. Each write function return `True`, if the file was created successfully and `False` in other case.
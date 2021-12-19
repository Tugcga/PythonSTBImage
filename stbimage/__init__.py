import sys
if sys.version_info[0] == 2:
    import PyStbImage_py27 as pystbi
else:
    if sys.version_info[1] == 6:
        from . import PyStbImage_py36 as pystbi
    elif sys.version_info[1] == 7:
        from . import PyStbImage_py37 as pystbi
    elif sys.version_info[1] == 8:
        from . import PyStbImage_py38 as pystbi
    else:
        from . import PyStbImage_py39 as pystbi

def load(filepath):
    '''Load image from the file. Supports png, jpg, tga, bmp and hdr formats

    Input:
        filepath - full path to the image file

    Output:
       tuple (width, height, channels, pixels), where width and height - are size of the loaded image, channels - the number of components per pixel (3 for RGB and 4 for RGBA), pixels - plane array of integers (from 0 to 255)
       Pixels list contains channels data for the first pixel, then for the second one and so on...
    '''
    return pystbi.load(filepath)


def load_float(filepath):
    '''Load image from the file, but return pixels in float format. Supports png, jpg, tga, bmp and hdr image formats

    Input:
        filepath - full path to the image file

    Output:
       tuple (width, height, channels, pixels), where width and height - are size of the loaded image, channels - the number of components per pixel (3 for RGB and 4 for RGBA), pixels - plane array of floats
       Pixels list contains channels data for the first pixel, then for the second one and so on...
    '''
    return pystbi.load_float(filepath)


def write(filepath, width, height, components, pixels, jpg_quality=100):
    '''Save pixels data to an image file. Supports png, jpg, tga and bmp image formats

    Input:
        filepath - full path to the file
        width - width of the image to save
        height - height of the image to save
        components - the number of channels of the image to save (3 if it should contains only RGB and 4 if RGBA)
        pixels - array of integers of the size width * height * components, which contains plane data of pixels. Each element shold be integer from 0 to 255
        jpg_quality - optional parameter, used when the image saved in jpg-format. Quality form 0 (low quality) to 100 (high quality)

    Outpt:
        True, if the file was saved successfully and False otherwise
    '''
    return pystbi.write(filepath, width, height, components, pixels, jpg_quality)


def write_float(filepath, width, height, components, pixels, jpg_quality=100):
    '''Save pixels data to an image file. Supports png, jpg, tga, bmp and hdr image formats

    Input:
        filepath - full path to the file
        width - width of the image to save
        height - height of the image to save
        components - the number of channels of the image to save (3 if it should contains only RGB and 4 if RGBA)
        pixels - array of floats of the size width * height * components, which contains plane data of pixels. Each element shold be float
        jpg_quality - optional parameter, used when the image saved in jpg-format. Quality form 0 (low quality) to 100 (high quality)

    Outpt:
        True, if the file was saved successfully and False otherwise
    '''
    return pystbi.write_float(filepath, width, height, components, pixels, jpg_quality)

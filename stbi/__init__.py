import sys
if sys.version_info[0] == 2:
    import PyStbImage_py2 as pystbi
else:
    from . import PyStbImage_py3 as pystbi


def load(filepath):
    return pystbi.load(filepath)


def load_float(filepath):
    return pystbi.load(filepath)


def write(filepath, width, height, components, pixels, jpg_quality=100):
    return pystbi.write(filepath, width, height, components, pixels, jpg_quality)


def write_float(filepath, width, height, components, pixels, jpg_quality=100):
    return pystbi.write_float(filepath, width, height, components, pixels, jpg_quality)

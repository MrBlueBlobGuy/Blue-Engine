import pywavefront
from vbo import BaseVBO

class wavefront_object:
    def __init__(self, filepath) -> None:
        _object = pywavefront.Wavefront(filepath, cache=True)
        print(_object.parse())

# wavefront_object('assets/cube.obj')
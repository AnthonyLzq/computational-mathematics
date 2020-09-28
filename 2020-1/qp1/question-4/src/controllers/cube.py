import numpy as np
from constants.cube.vertices import vertices as cube_vertices
from constants.cube.indices import indices as cube_indices


class Cube:
    def __init__(self):
        self._vertices = np.array(cube_vertices, dtype=np.float32)
        self._indices = np.array(cube_indices, dtype=np.uint32)

    def get_vertices(self):
        return self._vertices

    def get_indices(self):
        return self._indices

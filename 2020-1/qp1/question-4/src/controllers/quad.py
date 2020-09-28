import numpy as np
from constants.quad.vertices import vertices as quad_vertices
from constants.quad.indices import indices as quad_indices


class Quad:
    def __init__(self):
        self._vertices = np.array(quad_vertices, dtype=np.float32)
        self._indices = np.array(quad_indices, dtype=np.uint32)

    def get_vertices(self):
        return self._vertices

    def get_indices(self):
        return self._indices

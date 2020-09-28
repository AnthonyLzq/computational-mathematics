import numpy as np
from constants.triangle.vertices import vertices as triangle_vertices
from constants.triangle.colors import colors as triangle_colors


class Triangle:
    def __init__(self):
        self._vertices = np.array(triangle_vertices, dtype=np.float32)
        self._colors = np.array(triangle_colors, dtype=np.float32)

    def get_vertices(self):
        return self._vertices

    def get_colors(self):
        return self._colors

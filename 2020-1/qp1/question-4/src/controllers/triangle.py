import numpy as np
from constants.triangle.vertices import vertices as triangle_vertices


class Triangle:
    def __init__(self):
        self._vertices = np.array(triangle_vertices, dtype=np.float32)

    def get_vertices(self):
        return self._vertices

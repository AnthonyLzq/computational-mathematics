import glfw
import pyrr
import math
import time
from OpenGL.GL import *

from .cube import Cube
from .quad import Quad
from .shader import shader_maker
from .triangle import Triangle
from constants.rotation_matrix import rotation


class Window:
    def __init__(self, width: int, height: int, title: str, figure=''):
        # Initializing glfw library
        if not glfw.init():
            raise Exception('Glfw can not be initialized!')

        # Creating the window
        self._win = glfw.create_window(width, height, title, None, None)

        # Check if window was created
        if not self._win:
            glfw.terminate()
            raise Exception('Glfw window could not be created!')

        # Set window position
        glfw.set_window_pos(self._win, 400, 200)

        # Making the window resizeable
        glfw.set_window_size_callback(self._win, self.window_resize)

        # Make the context current
        glfw.make_context_current(self._win)
        # Creating our shader
        self.shader = shader_maker()

        if figure == 'triangle':
            # Setup for drawing a triangle
            self._triangle = self._draw_triangle()
        else:
            self._triangle = False

        if figure == 'quad':
            # Setup for drawing a quad
            self._quad = self._draw_quad()
        else:
            self._quad = False

        if figure == 'cube':
            # Setup for drawing a quad
            self._cube = self._draw_cube()
        else:
            self._cube = False

        glUseProgram(self.shader)
        glClearColor(34/255, 34/255, 34/255, 1)  # 222222
        glEnable(GL_DEPTH_TEST)
        self._rotation_location = glGetUniformLocation(self.shader, 'rotation')

    # Main application loop
    def main_loop(self):
        current_angle = -2*math.pi/3
        print(f'Rotated angle: {current_angle}rad')
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            if self._triangle:
                glDrawArrays(GL_TRIANGLES, 0, 3)

            elif type(self._quad) == list and self._quad[0]:
                glDrawElements(
                    GL_TRIANGLES,
                    self._quad[1].get_indices().shape[0],
                    GL_UNSIGNED_INT,
                    None
                )

            elif type(self._cube) == list and self._cube[0]:
                glDrawElements(
                    GL_TRIANGLES,
                    self._cube[1].get_indices().shape[0],
                    GL_UNSIGNED_INT,
                    None
                )

            # time.sleep(0.5)
            # if current_angle >= -2*math.pi/3:
            glUniformMatrix4fv(
                self._rotation_location,
                1,
                GL_FALSE,
                pyrr.matrix44.create_from_matrix33(rotation(current_angle))
            )
            # if current_angle < -2*math.pi/3:
            #     current_angle = 0

            # current_angle -= 0.001
            glfw.swap_buffers(self._win)

        # Terminate glfw, free up allocated resources
        glfw.terminate()

    def _draw_triangle(self):
        triangle = Triangle()

        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(
            GL_ARRAY_BUFFER,
            triangle.get_vertices().nbytes,
            triangle.get_vertices(),
            GL_STATIC_DRAW
        )

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(
            0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0)
        )

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(
            1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12)
        )

        return True

    def _draw_quad(self):
        quad = Quad()

        # Vertex buffer object
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(
            GL_ARRAY_BUFFER,
            quad.get_vertices().nbytes,
            quad.get_vertices(),
            GL_STATIC_DRAW
        )

        # Element buffer object
        EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(
            GL_ELEMENT_ARRAY_BUFFER,
            quad.get_indices().nbytes,
            quad.get_indices(),
            GL_STATIC_DRAW
        )

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(
            0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0)
        )

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(
            1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12)
        )

        return [True, quad]

    def _draw_cube(self):
        cube = Cube()

        # Vertex buffer object
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(
            GL_ARRAY_BUFFER,
            cube.get_vertices().nbytes,
            cube.get_vertices(),
            GL_STATIC_DRAW
        )

        # Element buffer object
        EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(
            GL_ELEMENT_ARRAY_BUFFER,
            cube.get_indices().nbytes,
            cube.get_indices(),
            GL_STATIC_DRAW
        )

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(
            0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0)
        )

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(
            1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12)
        )

        return [True, cube]

    def window_resize(self, window, width, height):
        glViewport(0, 0, width, height)

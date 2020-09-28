import glfw
from OpenGL.GL import *
from .triangle import Triangle


class Window:
    def __init__(self, width: int, height: int, title: str, figure='', operations=False):
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

        # Make the context current
        glfw.make_context_current(self._win)
        glClearColor(34/255, 34/255, 34/255, 1)  # 222222

        if figure == 'triangle':
            # Setup for drawing a triangle
            self._triangle = self._draw_triangle()
        else:
            self._triangle = False

        self._operations = operations

    # Main application loop
    def main_loop(self):
        while not glfw.window_should_close(self._win):
            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT)

            if self._triangle:
                if self._operations:
                    self._triangle_easy_operations()
                glDrawArrays(GL_TRIANGLES, 0, 3)

            glfw.swap_buffers(self._win)

        # Terminate glfw, free up allocated resources
        glfw.terminate()

    def _draw_triangle(self):
        triangle = Triangle()
        # Setup for the vertices
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, triangle.get_vertices())
        # Setup for the colors
        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(3, GL_FLOAT, 0, triangle.get_colors())

        return True

    def _triangle_easy_operations(self):
        glRotatef(1, 1, 0, 0)  # (theta, x, y, z)

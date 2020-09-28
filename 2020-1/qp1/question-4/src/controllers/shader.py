from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from constants.shaders.vertex import vertex_src
from constants.shaders.fragment import fragment_src


def shader_maker():
    return compileProgram(
        compileShader(vertex_src, GL_VERTEX_SHADER),
        compileShader(fragment_src, GL_FRAGMENT_SHADER)
    )

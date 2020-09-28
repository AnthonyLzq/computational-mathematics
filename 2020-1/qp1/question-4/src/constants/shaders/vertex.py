vertex_src = '''
#version 310 es

precision mediump float;

layout(location = 0)in vec3 a_position;
layout(location = 1)in vec3 a_color;

uniform mat4 rotation;

out vec3 v_color;

void main(){
  gl_Position = rotation * vec4(a_position, 1.0);
  v_color = a_color;
}
'''

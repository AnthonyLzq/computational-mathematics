import OpenGL
import glfw

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pyrr import Vector3,Quaternion,Matrix44
from random import random
import functools

keys = 150*[False]

class Object:
	objects = []
	
	def __init__(self):
		self.pos = Vector3()
		self.ori = Quaternion()
		self.dir = Vector3([0.,0.,1.])
		self.size = 0.5
		Object.objects.append(self)
	
	def setPos(self,*pos):
		self.pos = Vector3(pos)
	def setOri(self,ori):
		self.ori = ori
		
	def draw(self):
		glPushMatrix()
		glTranslatef(*self.pos)
		glMultMatrixf(Matrix44(self.ori).T)
		glScalef(*(self.size,)*3)
		# Cambiar por modelos más complejos
		self.model()
		glPopMatrix()
	
	def model(self):
		pass
	
	def frame(self):
		pass
		
	def destroy(self):
		Object.objects.remove(self)

class Player(Object):

	speed = 0.12
	rot_speed = 0.025
	rot_acc = 0.001
	
	def __init__(self):
		super(Player,self).__init__()
		self.rot_speed = 0.
	
	def frame(self):
		turning = False
		if keys[b's'[0]]:
			self.ori = self.ori * Quaternion.from_x_rotation(-self.rot_speed)
			turning = True
		if keys[b'w'[0]]:
			self.ori = self.ori * Quaternion.from_x_rotation(+self.rot_speed)
			turning = True
		if keys[b'a'[0]]:
			self.ori = self.ori * Quaternion.from_y_rotation(+self.rot_speed)
			turning = True
		if keys[b'd'[0]]:
			self.ori = self.ori * Quaternion.from_y_rotation(-self.rot_speed)
			turning = True
		if keys[b'q'[0]]:
			self.ori = self.ori * Quaternion.from_z_rotation(-self.rot_speed)
			turning = True
		if keys[b'e'[0]]:
			self.ori = self.ori * Quaternion.from_z_rotation(+self.rot_speed)
			turning = True
		
		if self.rot_speed < Player.rot_speed and turning:
			self.rot_speed += Player.rot_acc
		elif self.rot_speed > 0:
			self.rot_speed -= Player.rot_acc
		
		self.dir = self.ori * Vector3((0.,0.,1.))
		self.pos = self.pos + Player.speed * self.dir
		
		if self.pos.length > 35.:
			self.ori = self.ori * Quaternion.from_y_rotation(3.14159265)
		
	def model(self):
		glPushMatrix()
		glColor3f(.5,.5,.5)
		glTranslatef(0,0,-1)
		glRotatef(180,1,0,1)
		glScalef(1.5,0.15,1)
		glutSolidTetrahedron()
		glPopMatrix()
		glPushMatrix()
		glColor3f(1.,0.,0.)
		glTranslatef(-.5,.15,-1.2)
		glRotatef(15,0,0,1)
		glRotatef(-95,0,1,0)
		glScalef(1.2,.3,.1)
		glutSolidTetrahedron()
		glPopMatrix()
		glPushMatrix()
		glColor3f(1.,0.,0.)
		glTranslatef(.5,.15,-1.2)
		glRotatef(-15,0,0,1)
		glRotatef(-85,0,1,0)
		glScalef(1.2,.3,.1)
		glutSolidTetrahedron()
		glPopMatrix()

class Cube(Object):
	def __init__(self):
		super(Cube,self).__init__()
		self.pos = 50.*Vector3((random()-.5,random()-.5,random()-.5))
		self.ori = Quaternion((random()-.5,random()-.5,random()-.5,random()-.5))
		self.size = 0.5 + 1*random()
	
	def model(self):
		glColor3f(1.,1.,1.)
		glutSolidCube(1.)
	
class Beam(Object):
	speed = 0.5
	destroyed = 0

	def __init__(self,pos,ori):
		super(Beam,self).__init__()
		self.pos = pos
		self.ori = ori
	
	def frame(self):
		self.dir = self.ori * Vector3((0.,0.,1.))
		self.pos = self.pos + Beam.speed * self.dir
		if (self.pos - Beam.player.pos).length > 20.:
			self.destroy()
		for obj in Object.objects:
			if isinstance(obj,Cube) and (self.pos-obj.pos).length < obj.size:
				obj.destroy()
				self.destroy()
				Beam.destroyed += 1
				print(Beam.destroyed)
				Object.objects.append(Cube())
		
	def model(self):
		glColor3f(0.,0.,1.)
		glutSolidCube(.1)
		
class Camera:
	def __init__(self):
		self.pos = Vector3()
		self.ori = Quaternion()
	
	def calc(self):
		# glMultMatrixf(Matrix44(~self.ori).T)
		# glTranslatef(*-self.pos)
		center = self.pos + self.ori*Vector3((0.,0.,1.))
		up = self.ori*Vector3((0.,1.,0.))
		gluLookAt(*self.pos,*center,*up)
		

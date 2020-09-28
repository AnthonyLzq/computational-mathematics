from gamedefs import *

display = (800, 600)

camera = Camera()
cam_queue = 8*[(Vector3(),Quaternion())]

player = Player()
Beam.player = player

def frame():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	glMaterialfv(GL_FRONT,GL_DIFFUSE,(1.,1.,1.,1.))
	glEnable(GL_COLOR_MATERIAL)
	
	for obj in Object.objects:
		obj.frame()
	
	# Camera
	cam_queue.append((player.pos - player.ori*Vector3((0.,.25,3.)), player.ori))
	camera.pos,camera.ori = cam_queue.pop(0)
	camera.calc()
	
	# Graphing
	for obj in Object.objects:
		obj.draw()
		if isinstance(obj,Cube) and (obj.pos-player.pos).length < 0.75*obj.size:
			print('hit')
			# exit()
			player.pos = Vector3()
			Beam.destroyed = 0
			while (obj.pos-player.pos).length < 0.75*obj.size:
				player.pos = 30.*Vector3((random()-.5,random()-.5,random()-.5))
	glutSwapBuffers()

def key_down(key,*args):
	if not keys[b' '[0]] and key==b' ':
		Beam(player.pos,player.ori)
	keys[key[0]] = True
	
def key_up(key,*args):
	keys[key[0]] = False
	
def mouse_pos(x,y):
	pass

# Main
for i in range(40):
	Cube()
	
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(*display)
glutCreateWindow("Asteroids 3d")

glClearColor(0.,0.,0.,1.)
glShadeModel(GL_SMOOTH)
glEnable(GL_CULL_FACE)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
lightZeroPosition = [0.,0.,10.,1.]
lightZeroColor = [1.0,1.0,1.0,1.0]
glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
glEnable(GL_LIGHT0)

glutDisplayFunc(frame)
glutIdleFunc(frame)
glutKeyboardFunc(key_down)
glutKeyboardUpFunc(key_up)
glutPassiveMotionFunc(mouse_pos)

glMatrixMode(GL_PROJECTION)
gluPerspective(45,display[0]/display[1], 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glPushMatrix()
glutMainLoop()

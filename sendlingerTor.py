from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
from numpy import *
import sys 


def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,1,1,0)
    draw()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


torreUm = (
	(1, -3, -1),
	(1, 1, -1),
	(-1, 1, -1),
	(-1, -3, -1),
	(1, -3, 1),
	(1, 1, 1),
	(-1, 1, 1),
	(-1, -3, 1),
	(0, 2, 0)
	)


torreDois = (
	(7, -3, -1),
	(7, 1, -1),
	(5, 1, -1),
	(5, -3, -1),
	(7, -3, 1),
	(7, 1, 1),
	(5, 1, 1),
	(5, -3, 1),
	(6, 2, 0)
	)

edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,6),
	(7,6),
	(7,4),
	(7,3),
	(5,1),
	(5,6),
	(5,4),
	(8,1),
	(8,2),
	(8,5),
	(8,6),
	)

portao = (
	(1, -3, -1),
	(1, 0, -1),
	(1, -3, 1),
	(1, 0 ,1),
	(2, -3, -1),
	(5, 0, -1),
	(2, -3, 1),
	(5, 0, 1),
	(4, -3, 1),
	(4, -3, -1),
	(5, -3, 1),
	(5, -3, -1),
	)

portaoEdges = (
	(0,4),
	(1,5),
	(1,3),
	(2,6),
	(3,7),
	(2,3),
	(5,7),
	(8,10),
	(9,11),
	)

def draw() :
	glBegin(GL_LINES)
	
	for edge in edges:
		for vertex in edge:
			glVertex3fv(torreUm[vertex])
		for vertex in edge:
			glVertex3fv(torreDois[vertex])
	
	for edge in portaoEdges:
		for vertex in edge:
			glVertex3fv(portao[vertex])

	glEnd()

	glBegin(GL_LINE_STRIP)
	
	glVertex3f(2,-3,-1)
	for x in arange(-1,1,0.01):
		y = -2*x**2 -1
		glVertex3f(x+3,y,-1)
	glVertex3f(4,-3,-1)
	
	glEnd()

	glBegin(GL_LINE_STRIP)
	
	glVertex3f(2,-3,1)
	for x in arange(-1,1,0.01):
		y = -2*x**2 -1
		glVertex3f(x+3,y, 1)
	glVertex3f(4,-3,1)

	glEnd()

	glBegin(GL_LINE_STRIP)
	z = 1	
	glVertex3f(2,-3,1)
	for x in arange(-1,1,0.01):
		y = -2*x**2 -1
		z = z * -1
		glVertex3f(x+3,y, z)
	glVertex3f(4,-3,1)
	glEnd()



def main() :
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glEnable(GL_MULTISAMPLE)
	glEnable(GL_DEPTH_TEST)

	glutInitWindowSize(1000,600)
	glutCreateWindow("Sendlinger Tor")
	glClearColor(0.,0.,0.,1.)
	glutDisplayFunc(display)
	gluPerspective(45,1000.0/600,0.1,150.0)
	glTranslatef(0.0,0.0,-12)
	glRotatef(0,0,0,0)
	glutTimerFunc(50,timer,1)
	glutMainLoop()

main()

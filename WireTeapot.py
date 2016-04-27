from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import sys 


def draw() :
	glClear(GL_COLOR_BUFFER_BIT)
	glutWireTeapot(0.5)
	glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(450,450)
glutInitWindowPosition(200,500)
glutCreateWindow("Wire Teapot")
glutDisplayFunc(draw)
glutMainLoop()

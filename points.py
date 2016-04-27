from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import sys 

def init() :
	glClearColor(0.0, 0.0, 0.0, 1.0)
	gluOrtho2D(-11.0, 11.0, -11.0, 11.0)

def plotpoints() :
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 1.0, 1.0)

	glLineWidth(2.0)
	#glPointSize(3.0)
	glBegin(GL_LINES)
	#glVertex2f(0.0, 0.0)
	
	glVertex2f(0.0, 0.0)
	glVertex2f(10.0, 0.0)
	glVertex2f(10.0, 0.0)
	glVertex2f(10.0, 10.0)
	glVertex2f(10.0, 10.0)
	glVertex2f(0.0, 0.0)

	glVertex2f(0.0, 0.0)
	glVertex2f(10.0, 0.0)
	glVertex2f(10.0, 0.0)
	glVertex2f(10.0, -10.0)
	glVertex2f(10.0, -10.0)
	glVertex2f(0.0, 0.0)

	glVertex2f(0.0, 0.0)
	glVertex2f(-10.0, 0.0)
	glVertex2f(-10.0, 0.0)
	glVertex2f(-10.0, -10.0)
	glVertex2f(-10.0, -10.0)
	glVertex2f(0.0, 0.0)

	glVertex2f(0.0, 0.0)
	glVertex2f(-10.0, 0.0)
	glVertex2f(-10.0, 0.0)
	glVertex2f(-10.0, 10.0)
	glVertex2f(-10.0, 10.0)
	glVertex2f(0.0, 0.0)
	
	glVertex2f(-10.0, 10.0)
	glVertex2f(10.0, 10.0)
	glVertex2f(10.0, 10.0)
	glVertex2f(0.0, 0.0)
	glVertex2f(0.0, 0.0)
	glVertex2f(-10.0, -10.0)

	glVertex2f(-10.0, -10.0)
	glVertex2f(10.0, -10.0)
	glVertex2f(10.0, -10.0)
	glVertex2f(0.0, 0.0)
	glVertex2f(0.0, 0.0)
	glVertex2f(-10.0, -10.0)

	glEnd()

	glFlush()

def main() :
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(100, 400)
	glutCreateWindow("Points")
	glutDisplayFunc(plotpoints)

	init()
	glutMainLoop()

main()
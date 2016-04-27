from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
from math import *
from numpy import *
import sys 



### Torre ###
vertices = (
	#base
	(1,-1,-1),#0
	(-1,-1,-1),#1
	(-1,-1,1),#2
	(1,-1,1),#3
	#topo
	(1,3,-1),#4
	(-1,3,-1),#5
	(-1,3,1),#6
	(1,3,1),#7
	#Telhado
	(1.5,3,-1.5),#8
	(-1.5,3,-1.5),#9
	(-1.5,3,1.5),#10
	(1.5,3,1.5),#11
	(0,5,0)#12
	)
linhas = (
	(0,1),
	(1,2),
	(2,3),
	(3,0),
	(4,5),
	(5,6),
	(6,7),
	(7,4),
	(0,4),
	(1,5),
	(2,6),
	(3,7),
	#telhado
	(8,9),
	(9,10),
	(10,11),
	(11,8),
	(8,12),
	(9,12),
	(10,12),
	(11,12)
	)
faces = (
	(0,1,2,3),
	(4,5,6,7),
	(0,1,5,4),
	(2,3,7,6),
	(1,2,6,5),
	(0,3,7,4),
	#telhado
	(8,9,10,11),
#	(8,9,12,12),
#	(9,10,12,12),
#	(10,11,12,12),
#	(11,8,12,12),
	)


vertices_telhado = (
	(1.5,3,-1.5),#8 0
	(-1.5,3,-1.5),#9 1 
	(-1.5,3,1.5),#10 2
	(1.5,3,1.5),#11 3
	(0,5,0)#12 4
	)

faces_telhado = (
	(0,1,4),
	(1,2,4),
	(2,3,4),
	(3,0,4),
	)

### Muro ###
vertices_Muro = (
	(1,-1,-1),#0
	(1,-1, 1),#1
	(1, 2,-1),#2
	(1, 2, 1),#3
	#Topo
	(9,-1,-1),#4
	(9,-1, 1),#5
	(9, 2, 1),#6
	(9, 2,-1)#7
	)
faces_muro = (
	(0,1,3,2),
	(4,5,6,7),
	(0,2,7,4),
	(1,3,6,5),
	(2,3,6,7),
	(0,1,5,4),
	)

### Portao ###
vertices_Portao = (
	#Laterais
	(1,-1,-1),#0
	(1,-1, 1),#1
	(1, 2,-1),#2
	(1, 2, 1),#3
	(3,-1,-1),#4
	(3,-1, 1),#5
	(3, 2,-1),#6
	(3, 2, 1),#7
	(7,-1,-1),#8
	(7,-1, 1),#9
	(7, 2,-1),#10
	(7, 2, 1),#11
	(9,-1,-1),#12
	(9,-1, 1),#13
	(9, 2,-1),#14
	(9, 2, 1)#15
	)
faces_Portao = (
	#Esquerda
	(0,1,3,2),
	(0,1,5,4),
	(2,3,7,6),
	(1,5,7,3),
	(0,4,6,7),
	#Direita
	(8,9,11,10),
	(8,9,13,12),
	(12,13,15,14),
	(10,11,15,14),
	(9,11,15,13),
	(8,10,14,12)
	)


def calculaNormalFace(face,vertices):
    x = 0
    y = 1
    z = 2
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x])) 
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
   # print N[0], N[1], N[2]
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def calculaNormalArco(face):
    x = 0
    y = 1
    z = 2
    v0 = face[0]
    v1 = face[1]
    v2 = face[2]
    U = ( v2[x]+v0[x], v2[y]+v0[y], v2[z]+v0[z] )
    V = ( v1[x]+v0[x], v1[y]+v0[y], v1[z]+v0[z] )
    N = ( (U[y]*V[z]+U[z]*V[y]),(U[z]*V[x]+U[x]*V[z]),(U[x]*V[y]+U[y]*V[x])) 
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
   # print N[0], N[1], N[2]
    return ( N[x]/NLength, N[y]/NLength, (N[z]/NLength))

def criaTorre(x,z):
	torre = []
	for vertice in vertices:
		torre_vertice = []
		torreX = vertice[0] + x
		torreY = vertice[1]
		torreZ = vertice[2] + (z*-1) 

		torre_vertice.append(torreX)
		torre_vertice.append(torreY)
		torre_vertice.append(torreZ)

		torre.append(torre_vertice)
	return torre

def criaTelhado(x,z):
	telhado = []
	for vertice in vertices_telhado:
		telhado_vertice = []
		telhadoX = vertice[0] + x
		telhadoY = vertice[1]
		telhadoZ = vertice[2] + (z*-1) 

		telhado_vertice.append(telhadoX)
		telhado_vertice.append(telhadoY)
		telhado_vertice.append(telhadoZ)

		telhado.append(telhado_vertice)
	return telhado


def criaMuro(x,z,horizontal):
	muro = []
	if not horizontal:
		for vertice in vertices_Muro:
			muro_vertice = []
			muroX = vertice[0] + x
			muroY = vertice[1]
			muroZ = vertice[2] + (z*-1)

			muro_vertice.append(muroX) 
			muro_vertice.append(muroY)
			muro_vertice.append(muroZ)

			muro.append(muro_vertice)
		return muro
	else:
		for vertice in vertices_Muro:
			muro_vertice = []
			muroX = vertice[2] + z
		
			muroY = vertice[1]
			muroZ = -vertice[0]

			muro_vertice.append(muroX) 
			muro_vertice.append(muroY)
			muro_vertice.append(muroZ)

			muro.append(muro_vertice)
		return muro

def criaArco():
	Arco = []

	for x in arange(-2,2,0.01):
		arco_vertice = []
		y = (-x**2)/2 +1

		arco_vertice.append(x+5)
		arco_vertice.append(y)
		arco_vertice.append(1)
		Arco.append(arco_vertice)

		for i in range(1) :
			arco_vertice = []
			arco_vertice.append(x+5)
			arco_vertice.append(y)
			arco_vertice.append(-1)
			Arco.append(arco_vertice)
			#print y
	
	## So existe este condicional para poder minimizar no Sublime
	## esta parte grande e mecanica do codigo para definir pontos

	if True :
		arco_vertice = []
		arco_vertice.append(7)
		arco_vertice.append(2)
		arco_vertice.append(1)
		Arco.append(arco_vertice)
		
		arco_vertice = []
		arco_vertice.append(7)
		arco_vertice.append(2)
		arco_vertice.append(-1)
		Arco.append(arco_vertice)
		
		arco_vertice = []
		arco_vertice.append(3)
		arco_vertice.append(2)
		arco_vertice.append(1)
		Arco.append(arco_vertice)

		arco_vertice = []
		arco_vertice.append(3)
		arco_vertice.append(2)
		arco_vertice.append(-1)
		Arco.append(arco_vertice)

		arco_vertice = []
		arco_vertice.append(3)
		arco_vertice.append(-1)
		arco_vertice.append(1)
		Arco.append(arco_vertice)

		arco_vertice = []
		arco_vertice.append(3)
		arco_vertice.append(-1)
		arco_vertice.append(-1)
		Arco.append(arco_vertice)
	
	
	for i in Arco[0:799]:
		arco_vertice = []	
		
		arco_vertice.append(i[0])
		arco_vertice.append(i[1])
		arco_vertice.append(i[2])
		
		Arco.append(arco_vertice)

		arco_vertice = []
		arco_vertice.append(i[0])
		arco_vertice.append(2)
		arco_vertice.append(i[2])
		
		Arco.append(arco_vertice)
		


	return Arco

def draw () :
	### Criando as Torres ###
	glBegin(GL_QUADS)
	z = 0
	for i in range(2):
		x = 0	
		for j in range(2):
			torre = criaTorre(x,z)
			glColor3fv((0.5,0.2,0.2))
			for face in faces:
				glNormal3fv(calculaNormalFace(face,torre))
				for vertice in face:
					glVertex3fv(torre[vertice])
			x += 10
		z += 10
	glEnd()
	#Telhado
	glBegin(GL_TRIANGLES)
	z = 0
	for i in range(2):
		x = 0	
		for j in range(2):
			telhado = criaTelhado(x,z)
			glColor3fv((0.5,0.2,0.2))
			for face in faces_telhado:
				glNormal3fv(calculaNormalFace(face,telhado))
				for vertice in face:
					glVertex3fv(telhado[vertice])
			x += 10
		z += 10
	glEnd()

	### Criando Muros ###
	glBegin(GL_QUADS)
	muro = criaMuro(0,10,False)
	for face in faces_muro:
		glNormal3fv(calculaNormalFace(face,muro))
		for vertice in face:
			glVertex3fv(muro[vertice])
	
	z = 0
	for i in range(2):
		muro = criaMuro(0,z,True)
		for face in faces_muro:
			glNormal3fv(calculaNormalFace(face,muro))
			for vertice in face:
				glVertex3fv(muro[vertice])
		z += 10
	glEnd()

	### Criando Portao ###
	glBegin(GL_QUADS)
	glColor3fv((0,0,5))
	for face in faces_Portao:
		glNormal3fv(calculaNormalFace(face,vertices_Portao))
		for vertice in face:
			glVertex3fv(vertices_Portao[vertice])

	glEnd()


	### Criando o maldito arco ###
	glBegin(GL_QUAD_STRIP)
	glColor3fv((0,1,0))
	
	Arco = criaArco()
	x = 0 	
	
		
	for j in range(len(Arco)):
		face = []
		if len(Arco) > x:
			face.append(Arco[x])
			
			x += 1
			face.append(Arco[x])
			x += 1
			face.append(Arco[x])
			x += 2
			glNormal3fv(calculaNormalArco(face))
		else:
			break
	for i in range(len(Arco)):	
		glVertex3fv(Arco[i])
	
	


	glEnd()



def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(0,1,1,0)
    draw()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.01,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #gluLookAt(5,10,20,5,1,0,0,1,0)
    gluLookAt(-20,10,25,5,1,0,0,1,0)

def init():
    mat_ambient = (1, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (1.0, 1.0, 1.0, 1.0)
    mat_shininess = (50,)
    light_position = (0, -5, -5, 0)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(1028,798)
    glutCreateWindow("Castelo")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()

    glutMainLoop()

main()




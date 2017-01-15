[points]:https://i.imgsafe.org/8a9f246807.png
[teapot]:https://i.imgsafe.org/8ab27cddb5.png
[sendlingerTor]:https://i.imgsafe.org/8b77f21172.jpg
[sendlingerTorLines]:https://i.imgsafe.org/8b77d70a2f.jpg
[sendlingerTorSolid]:https://i.imgsafe.org/8b77d063ab.jpg
[castleColors]:https://i.imgsafe.org/8b779aacb5.jpg
[castleColorsCam]:https://i.imgsafe.org/8b77a72eb6.jpg
[castleLight]:https://i.imgsafe.org/8b77ad4f11.jpg
[castleLightCam]:https://i.imgsafe.org/8b77b9ca42.jpg


# ComputacaoGrafica-CEFET
This repository was dedicated to my works at Computer graphics class while doing my Bachelors in Computer Science in CEFET-RJ.

**All programs here were written using OpenGL for Python.**

## Prologue
In the beginning of this class, I was doing a student exchange program in Germany, sponsored by the brazilian government. Thats why I needed to figure it out how to learn Computer graphics whitout the Professor's help. So I started learning from the very basics of this subject till something more complex.

### Points.py
Nothing could be easier to create in Computer Graphics as some bunch of points on screen. But it was so easy to create that I connected those points with lines too. Creating a sort of "art" (at least for the "early me" on the past).

![points]

### Teapot
Every OpenGL lib I had seen has a built-in function to create a wireframe from a teapot. I know, it is not that hard to implement that, but it was my first steps in that subject.

![teapot]

###Sendlinger Tor
While my exchange program, I saw a really nice place in Munich. Its name is **Sendlinger Tor**, it is an old medieval gate at a square in Munich's city center. That was my inspiration to a nicer work with OpenGL.

#### The real Sendlinger tor
![sendlingerTor]

So I started coding its lines and found a real problem. I needed to find a perfect equation to reproduce the central arch.
```python
	for x in arange(-1,1,0.01):
		y = -2*x**2 -1
		glVertex3f(x+3,y,-1)
	
	for x in arange(-1,1,0.01):
		y = -2*x**2 -1
		glVertex3f(x+3,y, 1)

```
![sendlingerTorLines]

But I wasn't happy with the result, I wanted more! I wanted to start giving it a appearance of a solid. In that time I wasn't reading about solids already, so I needed to improvise!

![sendlingerTorSolid]

### My first castle
So it was time to move on, learn something new and a bit more harder. I was going to deal with solids. In Germany I had the oportunity of visiting a lot of castles, and I was fascinated with it since ever! So why not building my own castle?

#### Making my job easier
Every castle needs walls and towers, mine too! But I was creating a really humble castle, so every tower and wall had the same size. Well it makes things easier! I just needed to calculate the tranposition of its coordinates.

* Creating Towers
```python
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
```
```python
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
				glNormal3fv(calculaNormalFace(face))
				for vertice in face:
					glVertex3fv(torre[vertice])
			x += 10
		z += 10
	glEnd()
```

* Creating walls
```python
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
```
```python
### Criando Muros ###
	glBegin(GL_QUADS)
	muro = criaMuro(0,10,False)
	for face in faces_muro:
		glNormal3fv(calculaNormalFace(face))
		for vertice in face:
			glVertex3fv(muro[vertice])
	z = 0
	
for i in range(2):
		muro = criaMuro(0,z,True)
		for face in faces_muro:
			glNormal3fv(calculaNormalFace(face))
			for vertice in face:
				glVertex3fv(muro[vertice])
		z += 10
	glEnd()
```

Let's put some colors on it and we are good to go!

![castleColors]

### Shine bright like a diamond!
As you can see, I had a solid big fancy castle! But the sun was not shining my kingdom! I needed light and learn how to reflect this light on my castle! That was time to learn about **Normal and Light's behavior**.

![castleLight]

*As you can see, there is some bug with my normal for the gate, but I was really ok with that.*

Now was time to play around with camera, let's simulate that we are at the Castle's main gate!
![castleLightCam]

### End
That was how I learned the basics of Computer graphics in 3 weeks of study with PyOpenGL before reaching my country and University. 

You can read my my full report (in Portuguese) [here](https://drive.google.com/file/d/0B0yZCFuI97VkS2dVc2RpR2s5WFJIRFNoRWt4SHloeE55dzYw/view?usp=sharing).

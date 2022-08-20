from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

cores = ( (0,1,0), (0,0,1)) # vetor de cores
a = 0

x0 = -2 # Define o início do intervalo em X que será usado 
xn = 2 # Define o final do intervalo em X que será usado

y0 = -2 # Define o início do intervalo em Y que será usado
yn = 2 # Define o final do intervalo em Y que será usado

n = 30 # Define o número de passos usados
dx = (xn - x0)/n # Define o tamanho do passo em X
dy = (yn - y0)/n # Define o tamanho do passo em Y

def fc(x,y):
    # Paraboloide circular
    return x**2+y**2

def fh(x,y):
    # Paraboloide hiperbólico
    return x**2-y**2
   

def desenhaParaboloideHiper(): # desenha o paraboloide hiperbólico
    y = y0
    for i in range(n):
        x = x0
        
        glBegin(GL_TRIANGLE_STRIP)
        
        for j in range(n): 

            glColor3fv(cores[(i+1)%len(cores)])

            glVertex3f(x, y, fh(x, y))
            glVertex3f(x, y + dy, fh(x, y + dy))
            
            x += dx
        
        glEnd()
        
        y += dy

def desenhaParaboloideCircular(): # desenha o paraboloide circular
    y = y0
    for i in range(n):
        x = x0
        
        glBegin(GL_TRIANGLE_STRIP)
        
        for j in range(n):  

            glColor3fv(cores[(i+1)%len(cores)])

            glVertex3f(x, y, fc(x, y))
            glVertex3f(x, y + dy, fc(x, y + dy))
            
            x += dx
        
        glEnd()
        
        y += dy



a = 0
def desenha(): #função que chama as funções de desenho
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(-a,2,1,0)
    desenhaParaboloideHiper() # chama a função que desenha o paraboloide hiperbólico 
    #desenhaParaboloideCircular() # chama a função que desenha o paraboloide circular
    glPopMatrix()

    glutSwapBuffers()
    a += 1
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Funcao Implicita - Paraboloide Hiperbolico")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()
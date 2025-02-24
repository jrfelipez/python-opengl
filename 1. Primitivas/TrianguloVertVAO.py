from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GL import shaders
import numpy as np
 
codigoShaderVertice = """

#version 330 core
layout (location = 0) in vec2 aVertices;
void main() {
  gl_Position = vec4(aVertices, 0.0, 1.0);
}
 
"""

codigoShaderFragmento = """

#version 330 core
precision highp float;
uniform vec4 uColor;
out vec4 color;
void main() {
  color = uColor;
}

"""

"""
        2
       /\
      /  \
     /    \
    /      \
   /________\
  0          1  
"""
vertices = [-0.5, -0.5, # 0
            0.5, -0.5,  # 1
            0.0, 0.5]   # 2 

# Variables globales
VAO = None # Vertex Array Objects
programaID = None

# Variables Uniformes
uColor = None
 
def init():
    global VAO
    global programaID
    global uColor

    # Compila el shader de vértice
    shaderDeVertice = shaders.compileShader(codigoShaderVertice, GL_VERTEX_SHADER)
    
    # Compila el shader de fragmento
    shaderDeFragmento = shaders.compileShader(codigoShaderFragmento, GL_FRAGMENT_SHADER)
     
    # Se enlaza ambos shader
    programaID = shaders.compileProgram(shaderDeVertice, shaderDeFragmento)

    # Obtiene los ID de las variables de entrada de los shaders
    uColor = glGetUniformLocation(programaID, "uColor")

    # Crea un objeto arreglo de numpy
    bufVertices = np.array(vertices, dtype=np.float32)
    
    # Se genera un nombre (código) para el buffer
    VAO = glGenVertexArrays(1)
    
    # Se activa el VAO
    glBindVertexArray(VAO)
    
    # Se genera un nombre (código) para el buffer
    codigoVertices = glGenBuffers(1)
    
    # Se asigna un nombre (código) al buffer
    glBindBuffer(GL_ARRAY_BUFFER, codigoVertices)

    # Se transfiere los datos desde la memoria nativa al buffer de la GPU
    glBufferData(GL_ARRAY_BUFFER, bufVertices.nbytes, bufVertices, GL_STATIC_DRAW)

    # Se habilita el arreglo de los vértices (indice = 0)
    glEnableVertexAttribArray(0)

    # Se especifica el arreglo de vértices
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
    
    # Se desactiva el VAO
    glBindVertexArray(0)

    # Se deshabilita el acceso a los arreglos
    glDisableVertexAttribArray(0)
    
    # Se desasigna el buffer
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    
    # Color de fondo
    glClearColor(0, 0, 0, 1)
 
 
def display():

    # Inicializa el buffer de color
    glClear(GL_COLOR_BUFFER_BIT)
 
    # Se utiliza el programa de los shaders
    glUseProgram(programaID)

    # Se activa el VAO
    glBindVertexArray(VAO)

    # Se establece el color en (r,g,b,a)
    glUniform4f(uColor, 1, 0, 0, 1)

    # Renderiza las primitivas desde los datos de los arreglos (vértices, colores)
    glDrawArrays(GL_TRIANGLES, 0, 3)

    # Se desactiva el VAO
    glBindVertexArray(0)
    
    # Se deja de utilizar el programa de los shaders
    glUseProgram(0)

    # Intercambia los buffers
    glutSwapBuffers()
 
def main():
    
    # Solicita a windows abrir una ventana
    glutInit([])
    
    # Utiliza un buffer y selecciona el color RGB 
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)

    # Se le otorga un tamaño a la ventana
    glutInitWindowSize(512, 512)
    
    # Se define la posición inicial de la ventana
    glutInitWindowPosition(100, 100)

    # Crea la ventana
    glutCreateWindow(b"Triangulo")

    # Inicia OpenGL
    init()

    # Redibuja la ventana con el método display
    glutDisplayFunc(display)
    
    # Cede el control del programa a la libreria FREEGLUT
    glutMainLoop()
 
if __name__ == '__main__':
    main()

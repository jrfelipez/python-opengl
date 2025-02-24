from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GL import shaders
import numpy as np

codigoShaderVertice = """

#version 330 core
layout (location = 0) in vec2 aVertices;
layout(location = 1) in vec4 aColores;
out vec4 vColores;
void main() {
    vColores = aColores;
    gl_Position = vec4(aVertices, 0.0, 1.0);
}
 
"""

codigoShaderFragmento = """

#version 330 core
precision highp float;
in vec4 vColores;
out vec4 color;
void main() {
    color = vColores;
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
vertices = [-1, -1, # 0
             1, -1, # 1
             0, 1]  # 2 

colores = [1, 0, 0, 1, # 0
           0, 1, 0, 1, # 1
           0, 0, 1, 1] # 2 

indices = [0, 1, 2]

# Objeto del arreglo de vértices (VAO)
VAO = None # Vertex Array Object

# ID del programa generado
programaID = None

def init():
    global programaID
    global VAO

    # Compila el shader de vértice
    shaderDeVertice = shaders.compileShader(codigoShaderVertice, GL_VERTEX_SHADER)
    
    # Compila el shader de fragmento
    shaderDeFragmento = shaders.compileShader(codigoShaderFragmento, GL_FRAGMENT_SHADER)
     
    # Se enlaza ambos shader
    programaID = shaders.compileProgram(shaderDeVertice, shaderDeFragmento)


    # Crea los objetos de arreglos de numpy
    bufVertices = np.array(vertices, dtype=np.float32)
    bufColores = np.array(colores, dtype=np.float32)
    bufIndices = np.array(indices, dtype=np.uint32)
    
    
    # Se crea el objeto del arreglo de vértices (VAO)
    VAO = glGenVertexArrays(1)
    
    # Se activa el objeto
    glBindVertexArray(VAO)
    

    # Genera un objeto del buffer de vértices
    codigoVertices = glGenBuffers(1) # Vertex Buffer Object

    # Se asigna el objeto a los vértices
    glBindBuffer(GL_ARRAY_BUFFER, codigoVertices)

    # Se transfiere los datos desde la memoria nativa al buffer de la GPU
    glBufferData(GL_ARRAY_BUFFER, bufVertices.nbytes, bufVertices, GL_STATIC_DRAW)
    
    # Se habilita el arreglo de los vértices (indice = 0)
    glEnableVertexAttribArray(0)
    
    # Se especifica el arreglo de vértices
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
    
    
    # Genera un objeto del buffer de vértices
    codigoColores = glGenBuffers(1) # Vertex Buffer Object
    
    # Se asigna el objeto a los colores
    glBindBuffer(GL_ARRAY_BUFFER, codigoColores)

    # Se transfiere los datos desde la memoria nativa al buffer de la GPU
    glBufferData(GL_ARRAY_BUFFER, bufColores.nbytes, bufColores, GL_STATIC_DRAW)
    
    # Se habilita el arreglo de los colores (indice = 1)
    glEnableVertexAttribArray(1)
    
    # Se especifica el arreglo de colores
    glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 0, None)
    
    
    # Genera un objeto del buffer de indices
    iboID = glGenBuffers(1) # Index Buffer Object
    
    # Se asigna el objeto a los indices
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, iboID)
    
    # Se transfiere los datos desde la memoria nativa al buffer de la GPU
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, bufIndices.nbytes, bufIndices, GL_STATIC_DRAW)
    

    # Se desvincula y se deshabilita
    glBindVertexArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)


    # Color de fondo
    glClearColor(0, 0, 0, 1)
    
def display():

    # Inicializa el buffer de color
    glClear(GL_COLOR_BUFFER_BIT)
 
    # Se utiliza el programa de los shaders
    glUseProgram(programaID)


    # Se activa el objeto del arreglo de vértices (VAO)
    glBindVertexArray(VAO)

    # Renderiza las primitivas desde los datos de los arreglos (vértices, colores e índices)
    glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_INT, None)
    
    # Se desactiva el objeto del arreglo de vértices (VAO)
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

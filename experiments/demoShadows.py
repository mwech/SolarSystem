
"""
download and install:
-python-2.3.5.exe
-pygame-1.6.win32-py2.3.exe
-PyOpenGL-2.0.2.01.py2.3-numpy23.exe (the only one i know which have extension required)
-cgkit-1.1.0.win32-py2.3.exe (mat4)

double click on demoShadows.py
"""

#import openGL
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *

#import pygame..
import pygame
from pygame.locals import *

#
#import shadowsDef
from math import sin, cos
from array import array
from struct import unpack

window_x=800.0
window_y=600.0
INCR = 0.25
#import extension for shadows..
from OpenGL.GL.ARB.shadow import *
from OpenGL.GL.ARB.depth_texture import *
from OpenGL.GL.ARB.transpose_matrix import *


shadowMapSize = 512
spotFOV = 100.0

def CreateTextureShadow():
    'before loop, crate a texture obj to store shadow map'
    id = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, id)

    glTexImage2D(   GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT,
                    shadowMapSize, shadowMapSize, 0,
                    GL_DEPTH_COMPONENT, GL_UNSIGNED_BYTE, None
                    )

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

    return id

def CreateShadowBefore(position):
    """every frame render objs which casts shadows from light point of view
    position --> light position
    return --> projection matrix of the shadow map created"""
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    gluPerspective(spotFOV, 1.0, 0.1, 100.0)

    lightProjectionMatrix = glGetFloatv(GL_PROJECTION_MATRIX)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()
    gluLookAt(  position[0],
                position[1],
                position[2],
                0.0, 10.0, 0.0,
                0.0, 1.0, 0.0 )
    lightViewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    #Use viewport the same size as the shadow map
    glViewport(0, 0, shadowMapSize, shadowMapSize)

    #Draw back faces into the shadow map
    glCullFace(GL_FRONT)

    #Disable lighting, texture, use flat shading for speed
    glShadeModel(GL_FLAT)
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_LIGHTING)

    #Disable color writes
    glColorMask(0, 0, 0, 0)

    glPolygonOffset(0.5, 0.5)
    glEnable(GL_POLYGON_OFFSET_FILL)

    glClear( GL_DEPTH_BUFFER_BIT )

    #eval projection matrix
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()

    glLoadMatrixf(  [   [0.5, 0.0, 0.0, 0.0],
                        [0.0, 0.5, 0.0, 0.0],
                        [0.0, 0.0, 0.5, 0.0],
                        [0.5, 0.5, 0.5, 1.0] ])

    glMultMatrixf(lightProjectionMatrix)
    glMultMatrixf(lightViewMatrix)

    resMatrix = glGetFloatv(GL_TRANSPOSE_MODELVIEW_MATRIX)

    glPopMatrix()
    return resMatrix

def CreateShadowAfter(shadowMapID):
    'write texture into texture obj and reset gl params'
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, shadowMapID)
    glCopyTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 0, 0, shadowMapSize, shadowMapSize)

    glCullFace(GL_BACK)
    glShadeModel(GL_SMOOTH)
    glColorMask(1, 1, 1, 1)

    glDisable(GL_POLYGON_OFFSET_FILL)
    glDisable(GL_TEXTURE_2D)

def RenderShadowCompareBefore(shadowMapID, textureMatrix):
    'eval where draw shadows using ARB extension'
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, shadowMapID)

    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glEnable(GL_TEXTURE_GEN_R)
    glEnable(GL_TEXTURE_GEN_Q)

    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_EYE_LINEAR)
    glTexGenfv(GL_S, GL_EYE_PLANE, textureMatrix[0])

    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_EYE_LINEAR)
    glTexGenfv(GL_T, GL_EYE_PLANE, textureMatrix[1])

    glTexGeni(GL_R, GL_TEXTURE_GEN_MODE, GL_EYE_LINEAR)
    glTexGenfv(GL_R, GL_EYE_PLANE, textureMatrix[2])

    glTexGeni(GL_Q, GL_TEXTURE_GEN_MODE, GL_EYE_LINEAR)
    glTexGenfv(GL_Q, GL_EYE_PLANE, textureMatrix[3])

    #Enable shadow comparison
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_COMPARE_MODE_ARB, GL_COMPARE_R_TO_TEXTURE_ARB)

    #Shadow comparison should be true (in shadow) if r>texture
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_COMPARE_FUNC_ARB, GL_GREATER)

    #Shadow comparison should generate an INTENSITY result
    glTexParameteri(GL_TEXTURE_2D, GL_DEPTH_TEXTURE_MODE_ARB, GL_INTENSITY)

    #Set alpha test to discard false comparisons
    glAlphaFunc(GL_EQUAL, 1.0)
    glEnable(GL_ALPHA_TEST)

    glLightfv(GL_LIGHT0, GL_DIFFUSE, ( 0.6,0.6,0.6,1.0 ))   # Diffuse Light for shadows

def RenderShadowCompareAfter():
    'reset gl params after comparison'
    glDisable(GL_TEXTURE_2D)

    glDisable(GL_TEXTURE_GEN_S)
    glDisable(GL_TEXTURE_GEN_T)
    glDisable(GL_TEXTURE_GEN_R)
    glDisable(GL_TEXTURE_GEN_Q)

    glDisable(GL_ALPHA_TEST)


def Set_screen():
    'init pygame-video'
    pygame.display.init()
    pygame.display.set_mode((int(window_x),int(window_y)), HWSURFACE|OPENGL|DOUBLEBUF,)
    pygame.display.set_caption('shadow DEMO','shadow DEMO')


def initGL():
    'init openGL'
    glClearColor(0.6,0.6,0.6,1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)                                    

    glEnable(GL_LIGHTING)
    glEnable(GL_NORMALIZE)
    glEnable(GL_POLYGON_SMOOTH)
    glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    
    glShadeModel(GL_SMOOTH)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

def cameraLoop():
    'camera at (22,28,-18) looking at (0,0,0)'
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    gluPerspective(65.0, (window_x/window_y), 0.1, 200.0)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()
    gluLookAt(  22.0, 28.0, -18.0,
                0.0, 0.0, 0.0,
                0.0, 1.0, 0.0 )

    glViewport(0, 0, int(window_x), int(window_y))

def lightLoop(position):
    'light which change position every frame'
    
    position = list(position)
    position.append(1.0)

    glPushMatrix()
    glDisable(GL_LIGHTING)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glColor4f(1.0,1.0,1.0,1.0)
    glVertex4fv(position)
    glEnd()
    glPopMatrix() 

    glLightfv(GL_LIGHT0, GL_DIFFUSE, ( 1.0,1.0,1.0,1.0 ))   # Setup The Diffuse Light 
    glLightfv(GL_LIGHT0, GL_SPECULAR, ( 0.6,0.6,0.6,1.0 ))  # Setup The Specular Light
    glLightfv(GL_LIGHT0, GL_AMBIENT, ( 0.1,0.1,0.1,1.0 ))   # Setup The Ambient Light 
    glLightfv(GL_LIGHT0, GL_POSITION, position)             # Position of The Light  

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
    glEnable(GL_LIGHT0)
    
    glEnable(GL_LIGHTING)
    
def listFromFile(_file):
    'open _file and create a glList'
    all_vtx_data = array('f')
    mat_attr = array('f')

    f = open(_file, 'rb')
    all_vtx_data.fromfile(f, int(unpack('f',f.read(4))[0])*8 )
    mat_attr.fromfile(f, 11)
    f.close()

    trasparency = mat_attr[3]
    shine = mat_attr[4] 

    matAmb = [ 0.05, 0.05, 0.05, 1.0 ]
    matDiff = [mat_attr[0], mat_attr[1], mat_attr[2], trasparency ]            
    matSpec = [mat_attr[5], mat_attr[6], mat_attr[7], trasparency ]
    matEmis = [mat_attr[8], mat_attr[9], mat_attr[10], trasparency ]

    id_list = glGenLists(1)
    glNewList (id_list, GL_COMPILE)
    
    glMaterialfv(GL_FRONT, GL_DIFFUSE, matDiff)
    glMaterialfv(GL_FRONT, GL_AMBIENT, matAmb)
    glMaterialfv(GL_FRONT, GL_SPECULAR, matSpec)
    glMaterialfv(GL_FRONT, GL_EMISSION, matEmis)
    glMaterialf(GL_FRONT, GL_SHININESS, shine)

    glBegin(GL_TRIANGLES)
    for i in range(0, len(all_vtx_data), 8):
        glNormal3fv((all_vtx_data[i+0], all_vtx_data[i+1], all_vtx_data[i+2]))
        glVertex3fv((all_vtx_data[i+5], all_vtx_data[i+6], all_vtx_data[i+7]))      
    glEnd()     

    glEndList()
    
    return id_list

def renderFloor(listID):
    'render floor'
    glPushMatrix()
    glCallList(listID)
    glPopMatrix()
    
def renderObj(listID, rot):
    'render (really easy) animated object'
    glPushMatrix()
    glRotate(rot*0.5, 0.0, 1.0, 0.0)
    glTranslate(2.0, 10.0, 2.0)
    glRotate(-rot, 1.0, -1.0, 1.0)    
    glCallList(listID)
    glPopMatrix()    

#main
def main():
    'main loop'
    pause = False

    incrObjRotY = 0.0
    amply = 10.0

    Set_screen()
    initGL()

    #lists
    floorID = listFromFile('./floor.msh')
    objID = listFromFile('./obj.msh')    
    #shadow Map
    textureMapID = CreateTextureShadow()
        
    while True:
        #just to animate things..
        lightPosition = (sin(incrObjRotY*.01)*amply,20.0,cos(incrObjRotY*.01)*amply)
        if not pause:
            incrObjRotY += INCR
        
        #press 'q' or ESCAPE to quit..
        event = pygame.event.poll()
        if event.type == KEYUP and (event.key == K_ESCAPE or event.key == K_q):
            break
        #press 'p' to pause anims..
        if event.type == KEYUP and event.key == K_p:
            pause = not pause
            
        #render obj(s) casting shadows
        textureMatrix = CreateShadowBefore( position=lightPosition )
        renderObj(objID,incrObjRotY)
        renderFloor(floorID)
        CreateShadowAfter(textureMapID)
        
        #render camera
        cameraLoop()
        #set glLight
        lightLoop( position=lightPosition )
        
        #render all-----------------------------------
        renderObj(objID,incrObjRotY)
        renderFloor(floorID)
        #render all-----------------------------------
        
        #render obj(s) where shadows cast
        RenderShadowCompareBefore(textureMapID,textureMatrix)
        #renderObj(objID,incrObjRotY)
        renderFloor(floorID)
        RenderShadowCompareAfter()
        
        #flip
        pygame.display.flip()
        

#starts demo..        
if __name__ == "__main__":
    main()        

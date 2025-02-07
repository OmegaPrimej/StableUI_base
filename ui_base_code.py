!pip install pyopengl pyopengl-accelerate moderngl numpy

Import libraries
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
import moderngl

Set up display (commented for github)
from google.colab import output
output.enable_custom_gui()

Stable UI base code
def run_stable_ui():
  glutInit()
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(3840, 2160)
  glutInitWindowPosition(0, 0)
  glutCreateWindow(b"Stable UI Base")
  glClearColor(0.0, 0.0, 0.0, 0.0)
  glClear(GL_COLOR_BUFFER_BIT)
  glutDisplayFunc(lambda: glClear(GL_COLOR_BUFFER_BIT) or glutSwapBuffers())
  glutIdleFunc(lambda: glutPostRedisplay())
  glutMainLoop()
  
run_stable_ui()

Enable anti-aliasing and advanced lighting
def enable_enhancements():
  from OpenGL.GL import GL_MULTISAMPLE, GL_SAMPLE_ALPHA_TO_COVERAGE, GL_SAMPLE_COVERAGE
  glEnable(GL_MULTISAMPLE)
  glEnable(GL_SAMPLE_ALPHA_TO_COVERAGE)
  glEnable(GL_SAMPLE_COVERAGE)
  glSampleCoverage(0.5, True)
  
enable_enhancements()

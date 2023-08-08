import moderngl
import numpy
import glm
import pygame

class FrameBuffer:
    def __init__(self, scene, app):
        self.app = app
        self.ctx:moderngl.Context = app.ctx
        self.buffer
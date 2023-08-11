#!/usr/bin/env python3

"""game.py: Game class."""

from __future__ import annotations

import pygame
import sys
import time

# Libraries for OpenGL
import moderngl
import numpy as np

from src.settings import Settings
settings = Settings()

def surface_to_texture(ctx: moderngl.Context, surface: pygame.Surface) -> moderngl.Texture:
    """Converts a pygame.Surface to a moderngl.Texture."""
    texture: moderngl.Texture = ctx.texture(surface.get_size(), 4)
    texture.filter = moderngl.NEAREST, moderngl.NEAREST
    texture.swizzle = 'BGRA'
    texture.write(surface.get_view('1'))
    return texture
        
class Game:
    def __init__(self) -> None:
        from src.scenes.loading import LoadingState
        from src.scenes.transition import TransitionState
        from src.scenes.menu import MenuState

        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT),
                                                              pygame.DOUBLEBUF | pygame.OPENGL)
        self.display: pygame.Surface = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.ctx: moderngl.Context = moderngl.create_context()

        self.vbo: moderngl.Buffer = self.ctx.buffer(np.array([
            # position (x, y), uv coords (x, y)
            -1.0, -1.0, 0.0, 1.0,   # bottomleft
            1.0, -1.0, 1.0, 1.0,    # bottomright
            1.0,  1.0, 1.0, 0.0,    # topright
            -1.0,  1.0, 0.0, 0.0    # topleft
            ], dtype='f4'))
        
        self.vert_shader: str = open('src/shaders/vert_shader.vert', 'r').read()
        self.frag_shader: str = open('src/shaders/frag_shader.frag', 'r').read()

        self.program: moderngl.Program = self.ctx.program(vertex_shader=self.vert_shader,
                                                          fragment_shader=self.frag_shader)
        self.render_object: moderngl.VertexArray = self.ctx.vertex_array(self.program,
                                                                         [(self.vbo, '2f 2f', 'vert', 'texcoord')])

        self.clock: pygame.time.Clock = pygame.time.Clock()

        pygame.display.set_caption(settings.TITLE)
        pygame.display.set_icon(pygame.image.load(settings.ICON))

        self.state: State = LoadingState(self, settings.LOADING_TIME_MS, TransitionState, 1000, MenuState)

    def change_state(self, state: State) -> None:
        self.state = state

    def run(self) -> None:
        while True:
            Settings.DELTA_TIME = (time.time() - Settings.LAST_TIME) * settings.FPS
            Settings.LAST_TIME = time.time()
            
            self.events()
            self.update()
            self.draw()
    
    def quit(self) -> None:
        pygame.quit()
        sys.exit()
    
    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            self.state.events(event)
        
    def update(self) -> None:
        self.state.update()

        frame_texture: moderngl.Texture = surface_to_texture(self.ctx, self.display)
        frame_texture.use(0)
        self.program['tex'] = 0
        self.render_object.render(mode=moderngl.TRIANGLE_FAN)
        
        pygame.display.flip()

        frame_texture.release()

        self.clock.tick(settings.FPS)

    def draw(self) -> None:
        self.state.draw()

from src.scenes.state import State

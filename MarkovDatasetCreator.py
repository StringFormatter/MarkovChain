import os
import sys
import pygame
from ezscroll.ezscroll import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._size = self._width, self._height = 1920, 1080
        self._size1 = 500, 500

    def on_init(self):
        pygame.init()
        icon = pygame.image.load("AAMarkovicon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Markov Dataset Creator")
        group = pygame.sprite.RenderPlain()    
        self._clock = pygame.time.Clock()
        self._color_inactive = pygame.Color('lightskyblue3')
        self._color_active = pygame.Color('dodgerblue2')
        self._color_red = pygame.Color(120, 0, 0)
        self._color = pygame.Color('lightskyblue3')
        #self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf = pygame.display.set_mode(self._size)
        self._font = pygame.font.Font(None, 32)
        self._running = True
        self._scrollspeed = 5
        self._tactive = False
        self._text = ''
        self._textrect = pygame.Rect(10, 50, 790, 1010)
        self._bubblerect = pygame.Rect(802, 50, 1106, 1010)
        #self._textwd = pygame.Surface(self._size1)
        #self._bubblewd = pygame.Surface(self._size1)
        self._sRect = pygame.Rect(0, 0, 500, 20)
        self._textbg = pygame.Surface((1920, 1080)).convert()

        self._textsb = ScrollBar(
            group,
            790,
            self._sRect,
            self._textbg,
            0,
            ((0, 20), self._size1),
            4,
            True,
            20,
            (0, 0, 120),
            (0, 40, 170),
            (250, 250, 250),
            (70, 0, 0))
        
    def on_event(self, event):
        self._textsb.update(event)
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._textrect.collidepoint(event.pos):
                self._tactive = not self._tactive
            else:
                self._tactive = False
            self._color = self._color_active if self._tactive else self._color_inactive
        if event.type == pygame.KEYDOWN:
            if self._tactive:
                if event.key == pygame.K_RETURN:
                    self._textrect.top += 10
                elif event.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                else:
                    self._text += event.unicode
            
    def on_loop(self):
        pass
    
    def on_render(self):
        self._display_surf.fill((30, 30, 30))
        self._txt_surface = self._font.render(self._text, True, (255, 255, 255))
        twidth = 790
        self._textrect.w = twidth
        
        
        changes = self._textsb.draw(self._textbg)
        self._display_surf.blit(self._textbg, (20,0),(self._textsb.get_scrolled(), (500-20,20)))
        self._display_surf.blit(self._txt_surface, (12,52))
        
        
        #self._display_surf.blit(self._txt_surface, (12, 52))
        pygame.draw.rect(self._display_surf, self._color, pygame.Rect(10, 50, 790, 1010), 2)
        pygame.draw.rect(self._display_surf, self._color_red, self._bubblerect, 2)


        pygame.display.flip()
        self._clock.tick(30)

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    MainWin = App()
    MainWin.on_execute()

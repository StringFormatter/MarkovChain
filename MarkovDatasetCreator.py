import pygame

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 1920, 1080
 
    def on_init(self):
        pygame.init()
        icon = pygame.image.load("AAMarkovicon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Markov Dataset Creator")
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._textrect = pygame.Rect(10, 10, 1000, 1060)
        self._color_inactive = pygame.Color('lightskyblue3')
        self._color_active = pygame.Color('dodgerblue2')
        self._color = pygame.Color('lightskyblue3')
        self._font = pygame.font.Font(None, 32)
        self._text = ''
        self._scrollspeed = 5
        self._clock = pygame.time.Clock()
        self._tactive = False
        self._running = True
 
    def on_event(self, event):
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
                    self._text += "\n"
                elif event.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                else:
                    self._text += event.unicode

    def on_loop(self):
        pass
    
    def on_render(self):
        self._display_surf.fill((30,30,30))
        txt_surface = self._font.render(self._text, True, self._color)
        twidth = max(700, 790)
        self._textrect.w = twidth
        self._display_surf.blit(txt_surface, (self._textrect.x+5, self._textrect.y+5))
        pygame.draw.rect(self._display_surf, self._color, self._textrect, 2)
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

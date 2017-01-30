import pygame

class DrawingBrush():
    def __init__(self, size, color, radius):
        self.drawSurface = pygame.Surface(size, pygame.SRCALPHA, 32).convert_alpha()
        self.drawColor = color
        self.size = radius
        self.winSize = size
        self.winSurface = pygame.display.get_surface()

    def Draw(self, pos):
        pygame.draw.circle(self.drawSurface, self.drawColor, pos, self.size)

    def Clear(self):
        self.drawSurface = pygame.Surface(self.winSize, pygame.SRCALPHA, 32).convert_alpha()

    def Update(self):
        self.winSurface.blit(self.drawSurface, [0,0])

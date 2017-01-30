import pygame, os.path

class TextGUI(pygame.sprite.Sprite):
    #pos = array, centered = array
    def __init__(self, pos, text, color, fontSize, font, centered):
        self.x = pos[0]
        self.y = pos[1]
        self.centered = centered
        self.color = color
        self.fontSize = fontSize
        self.font = self.InitFont(font, fontSize)
        self.renderText = self.font.render(text, True, self.color)
        self.parentWin = pygame.display.get_surface()

    def InitFont(self, font, size):
        if os.path.isfile(font):
            return pygame.font.Font(font, size)
        else:
            return pygame.font.SysFont(font, size)

    def SetText(self, text):
        self.renderText = self.font.render(text, True, self.color)
                                           
    def Update(self):
        finalRect = self.renderText.get_rect()
        
        if self.centered[0]:
            finalRect.centerx = self.parentWin.get_rect().centerx

        if self.centered[1]:
            finalRect.centery = self.parentWin.get_rect().centery
            
        
        self.parentWin.blit(self.renderText, finalRect)

class ButtonGUI(pygame.sprite.Sprite):
    def __init__(self, pos, onImage, offImage, function, toggleable):
        self.x = pos[0]
        self.y = pos[1]
        self.state = False
        self.imgOn = pygame.image.load(onImage).convert_alpha()
        self.imgOff = pygame.image.load(offImage).convert_alpha()
        self.img = self.imgOff
        self.parentWin = pygame.display.get_surface()
        self.action = function
        self.toggleable = toggleable
        self.pressTime = 0

    def OnPress(self):
        if self.state == False:
            self.img = self.imgOn
            self.state = True
        else:
            self.img = self.imgOff
            self.state = False

        if self.action != None:
            self.action()

        self.pressTime = pygame.time.get_ticks()

    def GetState(self):
        return self.state

    def SetState(self, state):
        self.state = state
        if state == True:
            self.img = self.imgOn
        else:
            self.img = self.imgOff

    def GetRect(self):
        rect = self.img.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect

    def Update(self):
        if self.state == True and self.toggleable == False:
            if self.pressTime < pygame.time.get_ticks() - 50:
                self.SetState(False)
        
        self.parentWin.blit(self.img, [self.x, self.y])
        

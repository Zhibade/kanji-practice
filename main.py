# -*- coding: utf-8 -*-

#
#   Simple Kanji Drawing Practice Application
#       Author: Jose Ivan Lopez Romo
#


import pygame, sys
from pygame.locals import *

from gui import *
from drawing import *
from data import *


# Main

pygame.init()

winSize = [256, 256]
screen = pygame.display.set_mode(winSize)
pygame.display.set_caption("Kanji Writing Practice")

bgColor = pygame.Color(106, 89, 69)

fpsLimit = pygame.time.Clock()


# Data

kanjiList = KanjiData("Source/data.json")


# Drawing

isDrawing = False
drawColor = pygame.Color(155, 138, 119)
brushSize = 5
brush = DrawingBrush(winSize, drawColor, brushSize)


# GUI Init

latinFont = "verdana"
latinFontSize = 30
jpnFont = "SazanamiFont/sazanami-gothic.ttf"
jpnFontSize = 150
textColor = pygame.Color(155, 138, 119)

buttonOn = "Source/buttonOn.png"
buttonOff = "Source/buttonOff.png"
nextButtonOn = "Source/nextBtnOn.png"
nextButtonOff = "Source/nextBtnOff.png"

englishText = TextGUI([10, 10], "TestWord", textColor, latinFontSize, latinFont, [True, False])
kanji = TextGUI([25, 25], u"春", textColor, jpnFontSize, jpnFont, [True, True])


# GUI Buttons

def NextKanji():
    data = kanjiList.GetRandomCharacter()
    englishText.SetText(data[0])
    kanji.SetText(data[1])


hintButton = ButtonGUI([215, 221], buttonOn, buttonOff, None, True)
nextButton = ButtonGUI([15, 221], nextButtonOn, nextButtonOff, NextKanji, False)

displayObjs = [englishText, kanji, hintButton, nextButton]
buttonObjs = [hintButton, nextButton]


while True:
    fpsLimit.tick(60)

    screen.fill(bgColor)


    # Input handling

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousePos = pygame.mouse.get_pos()
            clickButton = False

            for button in buttonObjs:
                rect = button.GetRect()

                if rect.collidepoint(mousePos):
                    button.OnPress()
                    clickButton = True
                    brush.Clear()

            if clickButton == False:
                isDrawing = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            isDrawing = False
            clickButton = False


    # Brush flow

    if isDrawing == True:
        mousePos = pygame.mouse.get_pos()
        brush.Draw(mousePos)


    brush.Update()


    # Kanji flow

    for obj in displayObjs:
        if obj == kanji:
            if hintButton.GetState() == False:
                continue

        obj.Update()

    pygame.display.update()

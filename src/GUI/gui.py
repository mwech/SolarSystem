__author__ = 'arif'
# Mini-GUI demo

import pygame

BUTTON_NORMAL = 0
BUTTON_HOVER = 1
BUTTON_ACTIVE = 2


class Surface:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def collides(self, surface):
        return self.y < surface.top + surface.height and self.y + self.h > surface.top and self.x < surface.left + surface.width and self.x + self.w > surface.left

    def getCoords(self):
        return (self.x, self.y)

    def draw(self, surface):
        pass


class GUIElement(Surface):
    def __init__(self, id, x, y, w, h, color):
        super(GUIElement, self).__init__(x, y, w, h, color)
        self.id = id


class Textbox(GUIElement):
    def __init__(self, id, x, y, w, h, color):
        super(Textbox, self).__init__(id, x, y, w, h, color)
        self.data = ""

    # TODO: update and draw


class Button(GUIElement):
    def __init__(self, id, text, x, y, w, h):
        super(Button, self).__init__(id, x, y, w, h, None)
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.state = BUTTON_NORMAL
        self.normalColor = None
        self.hoverColor = None
        self.activeColor = None

    def decorate(self, normalColor, hoverColor, activeColor):
        self.normalColor = normalColor
        self.hoverColor = hoverColor
        self.activeColor = activeColor
        self.color = self.normalColor

    def update(self, mouseCoords, mousePressed):
        (up, down, middle) = mousePressed
        if len(mouseCoords) < 4: mouseCoords = pygame.Rect(mouseCoords[0], mouseCoords[1], 1, 1)

        if not self.collides(mouseCoords):
            self.state = BUTTON_NORMAL
            self.color = self.normalColor
            return

        if up:
            self.state = BUTTON_ACTIVE
            self.color = self.activeColor
        else:
            self.state = BUTTON_HOVER
            self.color = self.hoverColor

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
        surface.blit(self.font.render(self.text, 1, (255, 255, 255)), self.getCoords())
__author__ = 'arif'
import sys, pygame
from pygame.locals import *
from gui import *



def input(events):
    for e in events:
        if e.type == QUIT:
            pygame.quit()
            sys.exit()


pygame.init()
pygame.display.set_caption("GUI Demo")

window = pygame.display.set_mode((1020, 720))
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)
button = Button("btn_1", "Play", 0, 0, 100, 80)
button.decorate((255, 0, 0), (0, 255, 0), (0, 0, 255))

button2 = Button("btn_2", "Zoom", 100, 0, 300, 80)
button2.decorate((255, 255, 0), (0, 255, 0), (0, 0, 255))

button3 = Button("btn_3", "Light", 420, 0, 100, 80)
button3.decorate((255, 100, 0), (0, 255, 0), (0, 0, 255))

button4 = Button("btn_4", "Move", 520, 0, 100, 80)
button4.decorate((255, 100, 0), (0, 255, 0), (0, 0, 255))

button5 = Button("btn_5", "Rotate 1", 620, 0, 100, 80)
button5.decorate((255, 100, 0), (0, 255, 0), (0, 0, 255))

button6 = Button("btn_6", "Rotate 2", 720, 0, 100, 80)
button6.decorate((255, 100, 0), (0, 255, 0), (0, 0, 255))

button7 = Button("btn_6", "Reset", 820, 0, 100, 80)
button7.decorate((255, 100, 0), (0, 255, 0), (0, 0, 255))

button8 = Button("btn_6", "Quit", 920, 0, 100, 80)
button8.decorate((255, 100, 0), (0, 255, 0), (0, 0, 255))

while True:
    screen.fill((200, 120, 50))
    input(pygame.event.get())
    button.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    button2.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    button3.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    button4.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    button5.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    button6.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    button7.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    button8.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    button.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)
    button5.draw(screen)
    button6.draw(screen)
    button7.draw(screen)
    button8.draw(screen)
    pygame.display.flip()
import pygame
import pygame.font
pygame.init()
display=pygame.display.set_mode((500,500))
pygame.display.set_caption("DIRECTION CONTROL")
display_font = pygame.font.Font(None, 40)
text_position = text.get_rect(centerx=250)
text = display_font.render('Give Directions Using Arrow Keys', 1,(0,255,255))
display.blit(text)
pygame.display.update()



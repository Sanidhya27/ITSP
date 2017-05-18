import pygame
import pygame.font
import motor_control
def pygame_setup():
	pygame.init()
	display=pygame.display.set_mode((500,500))
	pygame.display.set_caption("DIRECTION CONTROL")
	display_font = pygame.font.Font(None, 40)
	text_position = text.get_rect(centerx=250)
	text = display_font.render('Give Directions Using Arrow Keys', 1,(0,255,255))
	display.blit(text)
	pygame.display.update()
def get_directions():
	try:
		while True:
			command=""
			event=pygame.event.get()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					command="LEFT"
				if event.key==pygame.K_RIGHT:
					command="RIGHT"
				if event.key==pygame.K_UP:
					command="FORWARD"
				if event.key==pygame.K_DOWN:
					command="BACK"
			if event.type==pygame.KEYUP:
				command="no command"	
			print(command)		
			instructions(command)	
	except KeyboardInterrupt:
		pygame.quit()
def main():
    """Main function"""
    motor_contol.gpio_setup()
    pygame_setup()
    get_directions()

if __name__ == '__main__':
    main()


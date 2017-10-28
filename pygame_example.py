import io
import pygame
import pygame.font
import time
import picamera
from PIL import Image

import motor_control
def pygame_setup():
    pygame.init()
    display=pygame.display.set_mode((500,500))
    pygame.display.set_caption("DIRECTION CONTROL")
    display_font = pygame.font.Font(None, 40)
    text = display_font.render('Give Directions Using Arrow Keys', 1,(0,255,255))
    text_position = text.get_rect(centerx=250)
    display.blit(text,text_position)
    pygame.display.update()
def get_directions():
    clock=pygame.time.Clock()
<<<<<<< HEAD
    with picamera.PiCamera() as camera:
        camera.resolution = (800,300)
        camera.framerate = 24
        camera.start_preview()
        time.sleep(2)
        try:
            while True:
                for event in pygame.event.get():
                    command=""
                    
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_LEFT:
                            command="LEFT"
                        if event.key==pygame.K_RIGHT:
                            command="RIGHT"
                        if event.key==pygame.K_UP:
                            command="FORWARD"
                        if event.key==pygame.K_DOWN:
                            command="BACK"
                    elif event.type==pygame.KEYUP:
                        command="no command"
                print(command)
                motor_control.instructions(command)
                stream = io.BytesIO()
                camera.capture(stream, format='jpeg', use_video_port=True)
                """Save image"""
                stream.seek(0)
                image = Image.open(stream)
                image.save("/home/pi/ITSP/%s/image%s.jpg" % (command,"-" + command + "-"+ str(time.time())), format="JPEG")
                stream.flush()
                clock.tick(30)
        except KeyboardInterrupt:
            pygame.quit()
=======
    try:
        while True:
            for event in pygame.event.get():
                command=""
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        command="LEFT"
                    if event.key==pygame.K_RIGHT:
                        command="RIGHT"
                    if event.key==pygame.K_UP:
                        command="FORWARD"
                    if event.key==pygame.K_DOWN:
                        command="BACK"
                elif event.type==pygame.KEYUP:
                    command="no command"
            print(command)
            stream = io.BytesIO()
        	camera.capture(stream, format='jpeg', use_video_port=True)
        	"""Save image"""
    		stream.seek(0)
   			image = Image.open(stream)
    		image.save("C:/Users/Sanidhya garg/itsp/%s/image%s.jpg" % (command,"-" + command + "-"+ str(time.time())), format="JPEG")
        	stream.flush()
            clock.tick(10)
    except KeyboardInterrupt:
        pygame.quit()
>>>>>>> 25668b80b89e1df32a172012446d6e300992b655


def main():
    """Main function"""
    #motor_control.gpio_setup()
    pygame_setup()
    get_directions()

if __name__ == '__main__':
    main()


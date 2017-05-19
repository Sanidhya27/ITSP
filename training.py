import pygame_example
import os
labels={"FORWARD":[1,0,0,0],"BACK":[0,1,0,0],"RIGHT":[0,0,1,0],"LEFT":[0,0,0,1]}
for direction,label in labels.items():
	for img in os.listdir("path/%s" % (label))

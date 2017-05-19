import pygame_example
import os
import tensorflow as tf
from scipy.misc import imread,imresize

labels={"FORWARD":[1,0,0,0],"BACK":[0,1,0,0],"RIGHT":[0,0,1,0],"LEFT":[0,0,0,1]}
x = tf.placeholder(tf.float32, [None, 784])

for direction,label in labels.items():
	for img in os.listdir("path/%s" % (direction)):
		image_array = imread(filename, flatten=True)
        resized_image_array = imresize(image_array, (28,28))
        feed_dict=(x:resized_image_array.flatten(),y:label)


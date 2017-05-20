import tensorflow as tf
from numpy import r_,array, zeros
import glob
from scipy.misc import imread, imresize



def load_images_to_array(classification_label_and_values):
    """Loads images to array"""
    training_image_array = array([[zeros(IMAGE_DIMENSIONS[0] * IMAGE_DIMENSIONS[1])]])
    training_image_value = array([[0, 0, 0, 0, 0]])
    print("Loading images to array...")
    
    for class_label, class_value in classification_label_and_values.iteritems():
        for filename in glob.glob("./"+class_label+"/*"):
            image_array = imread(filename, flatten=True)
            resized_image_array = imresize(image_array, IMAGE_DIMENSIONS)
            
            training_image_array = r_[training_image_array, [resized_image_array.flatten()]]
            training_image_value = r_[training_image_value, [class_value]]
    
    return zip(training_image_array,training_image_value)


CLASSIFICATION_LABELS_AND_VALUES = {
    'forward': [1, 0, 0, 0, 0],
    'reverse': [0, 1, 0, 0, 0],
    'left': [0, 0, 1, 0, 0],
    'right': [0, 0, 0, 1, 0],
    'idle': [0, 0, 0, 0, 1]
}
all_img_label = load_images_to_array(CLASSIFICATION_LABELS_AND_VALUES[1:,:])

x  = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 5])
w1 = tf.Variable(tf.zeros([784, hidden_layer_size]))
b1 = tf.Variable(tf.zeros([hidden_layer_size]))
y1 = tf.sigmoid(tf.matmul(x, w1) + b1)
w2 = tf.Variable(tf.zeros([hidden_layer_size,5]))
b2 = tf.Variable(tf.zeros([5]))
y2 = tf.sigmoid(tf.matmul(y1, w2) + b2)

first_term  = - y_ * tf.log(y2)
second_term = (1 - y_) * tf.log(1 - y2)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()


for _ in range(1000):
    batch_xs,batch_ys= zip(*random.sample(all_img_label,100))
    #batch_xs = [row[0] for row in batch]
    #batch_ys = [row[1] for row in batch]
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})


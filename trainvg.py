def load_images_to_array(classification_label_and_values):
    """Loads images to array"""
    training_image_array = array([zeros(IMAGE_DIMENSIONS[0] * IMAGE_DIMENSIONS[1])])
    training_image_value = array([[0, 0, 0, 0, 0]])
    print("Loading images to array...")
    for class_label, class_value in classification_label_and_values.iteritems():
        for filename in glob.glob("./"+class_label+"/*"):
            image_array = imread(filename, flatten=True)
            resized_image_array = imresize(image_array, IMAGE_DIMENSIONS)
            training_image_array = r_[training_image_array, [resized_image_array.flatten()]]
            training_image_value = r_[training_image_value, [class_value]]
    return c_(training_image_array, training_image_value)

CLASSIFICATION_LABELS_AND_VALUES = {
    'forward': [1, 0, 0, 0, 0],
    'reverse': [0, 1, 0, 0, 0],
    'left': [0, 0, 1, 0, 0],
    'right': [0, 0, 0, 1, 0],
    'idle': [0, 0, 0, 0, 1]
}
all_img_label = load_images_to_array(CLASSIFICATION_LABELS_AND_VALUES)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()


for _ in range(1000):
    batch = random.sample(all_img_label,100)
    batch_xs = [row[0] for row in batch]
    batch_ys = [row[1] for row in batch]
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})


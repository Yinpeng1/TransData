import tensorflow3 as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow3 as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
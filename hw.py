from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#### Softmax ####
# x = images, arbitrarily many 28x28px large
x = tf.placeholder(tf.float32, [None, 784])

# Weights (784 different pixel inputs -> 10 different number outputs) LEARNED
W = tf.Variable(tf.zeros([784, 10]))

# Biases LEARNED
b = tf.Variable(tf.zeros([10]))

evidence = tf.matmul(x, W) + b
y = tf.nn.softmax(evidence)



#### Training ####

# The true value
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# Use gradient decent with learning rate 0.5 to try to minimize the cross_entropy function
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.initialize_all_variables()

session = tf.Session()
session.run(init)

for i in range(1000):
    batch_images, batch_labels = mnist.train.next_batch(100)
    session.run(train_step, feed_dict={x: batch_images, y_: batch_labels})


#### Evaluating ####
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(session.run(accuracy, feed_dict={x:mnist.test.images, y_: mnist.test.labels}))



def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.variable(initial)


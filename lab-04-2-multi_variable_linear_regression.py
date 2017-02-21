# Lab 4 Multi-variable linear regression
import tensorflow as tf

x_data = [[1., 0.], [0., 2.], [3., 0.], [0., 4.], [5., 0.]]
y_data = [1, 2, 3, 4, 5]

W = tf.Variable(tf.random_uniform(
    shape=[2, 1], minval=-1.0, maxval=1.0, dtype=tf.float32))
b = tf.Variable(tf.random_uniform(
    shape=[1], minval=-1.0, maxval=1.0, dtype=tf.float32))

# Hypothesis
hypothesis = tf.matmul(x_data, W) + b

# Simplified cost function
cost = tf.reduce_mean(tf.square(hypothesis - y_data))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# Initialize variable
init = tf.global_variables_initializer()

# Launch graph
sess = tf.Session()
sess.run(init)

for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(cost), sess.run(W), sess.run(b))
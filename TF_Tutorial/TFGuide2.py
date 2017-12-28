import tensorflow as tf
#initialized Session
sess= tf.Session()
#Model arbitrary inputs
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
#tf.Variable changes initialized when init
#tf.constant doesnt and are initialized when called
x = tf.placeholder(tf.float32)
linear_model = W * x + b

init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(linear_model, {x:[1,2,3,4]}))

# to evaluate a model we ned a y placeholder
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)

#how far apart is the current model from the provided data
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

# change values for tf.Variable with tf.assign
fixW = tf.assign(W,[-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW,fixb])
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

#optimizer the change the variables to minimize the loss function
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

sess.run(init)# reset los valores
for i in range (1000):
    sess.run(train,{x:[1,2,3,4], y:[0,-1,-2,-3]})

print(sess.run([W,b]))

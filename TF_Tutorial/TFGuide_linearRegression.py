import tensorflow as tf

#Parametros del model
W = tf.Variable([.3], dtype= tf.float32)
b = tf.Variable([-.3], dtype= tf.float32)
#Inputs and Outputs del modelo
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)

#loss
loss = tf.reduce_sum(tf.square(linear_model - y))#Sumatoria de los cuadrados

#optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)


#Training la data
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]

#Training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000):
    sess.run(train, {x: x_train, y: y_train})

    #evaluar la accuracy of the Training
    curr_W, curr_b, curr_loss = sess.run([W,b,loss], {x: x_train, y: y_train})
    print("W: %s b: %s loss: %s" %(curr_W, curr_b, curr_loss))

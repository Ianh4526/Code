import tensorflow as tf

#Nodes
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)
print(node1,node2)#estructura de los nodos

#Sessions
sess= tf.Session()
print(sess.run([node1,node2]))#valores de los nodos

#Operaciones con Nodos
node3 = tf.add(node1,node2)#Sumatoria
print("node3:", node3)
print("sess.run(node3):", sess.run(node3))

#PlaceHolders algo asi como variables
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b #shortcut para tf.add(a,b)

print(sess.run(adder_node, {a:3, b:4.5}))
print(sess.run(adder_node, {a:[1,3], b:[2,4]}))

add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a:3, b: 4.5}))

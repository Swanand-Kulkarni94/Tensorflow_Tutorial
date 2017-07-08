#Program 1, introducing Session and Matrix multiplication

import tensorflow as tf 

m1 = tf.constant([[2, 2]])
m2 = tf.constant([[3], [3]])

dot_operation = tf.matmul(m1, m2)
"""
#Method_1
sess = tf.Session(
result = sess.run(dot_operation)
print (result)
sess.close()
"""
#Method_2
with tf.Session() as Sess:
	result_ = Sess.run(dot_operation)
	print(result_)

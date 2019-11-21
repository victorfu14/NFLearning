#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[4]:


import tensorflow as tf
import numpy as np
x = tf.placeholder(tf.float32, shape=(None, 784))
y = tf.placeholder('float')
def multilayer_perceptron(x, weights, biases):
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    out_layer = tf.matmul(layer_1, weights['out']) + biases['out']
    return out_layer

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 1

def n_n(x):
    hidden_1_layer = {'weights':tf.Variable(tf.random_normal([784, n_nodes_hl1])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

    hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}

    out_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}
    x1=multilayer_perceptron(x, hidden_1_layer['weights'], hidden_1_layer['biases'])
    x2=multilayer_perceptron(x1,hidden_2_layer['weights'],hidden_2_layer['biases'])
    x3=multilayer_perceptron(x2,out_layer['weights'],out_layer['biases'])
    return x3

def train(x,y):
    pred=n_n(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred, y))
    optimizer = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(cost)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(20):
            _, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y: epoch_y})
        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))  
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

x=np.zeros((10,784))
y=np.zeros((10,1))
train(x,y)


# In[ ]:





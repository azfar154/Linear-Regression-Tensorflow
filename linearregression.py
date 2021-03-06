# -*- coding: utf-8 -*-
"""LinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/azfar154/Linear-Regression/blob/master/LinearRegression.ipynb
"""

import numpy as np
import tensorflow as tf
class LinearRegression:
  def fit(self,X_train,y_train,show_weights = False,epochs = 300,not_numpy = True):
    learning_rate=0.02
    training_epochs=3000
    display_step=50
    if not_numpy:
      X_train = X_train.to_numpy()
      y_train = y_train.to_numpy()
    samples =X_train.shape[0]
    X=tf.placeholder('float')
    Y=tf.placeholder('float')
    self.X = X
    self.Y = Y
    W=tf.Variable(np.random.randn(),name="Weight")
    b=tf.Variable(np.random.randn(),name="bias")
    predicted=tf.add(tf.multiply(X,W),b)
    loss=tf.reduce_sum(tf.pow(predicted-Y,2)/(2*samples))
    optimizer=tf.train.GradientDescentOptimizer(learning_rate).minimize(loss) 
    sess = tf.Session()
    self.sess = sess
    self.loss = loss
    init=tf.global_variables_initializer()
    epochs = epochs
    sess.run(init)
    for epoch in range(epochs):
      for x,y in zip(X_train,y_train):
        sess.run(optimizer,feed_dict = {X:x,Y:y})
      if epoch % 50 == 0:
        if show_weights == True:
          weights = sess.run(W)
          for x in weights:
            print(x)
        error_val = sess.run(loss, feed_dict={X:x,Y:y})
        print("Epoch",epoch,"Bias=",sess.run(b),"Error",error_val)
    self.bias = sess.run(b)
    self.weights = sess.run(W)
  def show_weights(self):
    print(self.weights)
  def score(self,x_test,y_test):
    loss = self.sess.run(self.loss,feed_dict={self.X:x_test,self.Y:y_test})
    print("The loss is",loss)

import pandas as pd

from sklearn import datasets 
data = datasets.load_boston()

data.target

new_data = pd.DataFrame(data.data, columns=data.feature_names)
target = pd.DataFrame(data.target, columns=["MEDV"])

X = new_data["RM"]
y = target["MEDV"]

from sklearn.model_selection import train_test_split
X_train,x_test,y_train,y_test = train_test_split(X,y,random_state =0)

model = LinearRegression()

model.fit(X_train,y_train,epochs=50)

model.score(x_test,y_test)

model.show_weights()
import tensorflow as tf

import pandas as pd
data1=pd.read_csv("training_data.csv")
pd1=data1.drop(["Year", "Week", "Home", "Away"], axis=1)
pd2=pd1.drop(pd1.columns[0], axis = 1) 
finallabel=pd2.Win.values
finaltraining=pd2.drop(["Win"], axis=1)
finaltraining=finaltraining.values
print(finallabel.shape)
print(finaltraining.shape)


data2=pd.read_csv("testing_data.csv")
pdt=data2.drop(["Year", "Week", "Home", "Away"], axis=1)
pdt2=pdt.drop(pdt.columns[0], axis = 1) 
teslabel=pdt2.Win.values
testinp=pdt2.drop(["Win"], axis=1).values


#(x_train, y_train),(x_test, y_test) = tf.keras.datasets.cifar10.load_data()
#print(x_train.shape,y_train.shape)
#x_train, x_test = x_train / 255.0, x_test / 255.0
#x1=np.zeros((60000,28,28))
#y1=np.zeros((60000,1))
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1200, activation='relu'),
    tf.keras.layers.Dropout(0.9),
    tf.keras.layers.Dense(780, activation='relu'),
    tf.keras.layers.Dropout(0.9),
    tf.keras.layers.Dense(520, activation='relu'),
    tf.keras.layers.Dropout(0.9),
    tf.keras.layers.Dense(259, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(finaltraining, finallabel, epochs=10)
model.evaluate(testinp, teslabel)
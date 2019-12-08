import tensorflow as tf

import pandas as pd
data1=pd.read_csv("training_data-2.csv")
pd1=data1.drop(["Year", "Week", "Home", "Away","ScoreDiff"], axis=1)
pd2=pd1.drop(pd1.columns[0], axis = 1) 
finallabel=pd2.Win.values
finaltraining=pd2.drop(["Win"], axis=1)
finaltraining=tf.math.sigmoid(finaltraining.values).numpy()
print(finallabel.shape)
print(finaltraining.shape)


data2=pd.read_csv("testing_data-2.csv")
pdt=data2.drop(["Year", "Week", "Home", "Away","ScoreDiff"], axis=1)
pdt2=pdt.drop(pdt.columns[0], axis = 1) 
teslabel=pdt2.Win.values
testinp=tf.math.sigmoid(pdt2.drop(["Win"], axis=1).values).numpy()


#(x_train, y_train),(x_test, y_test) = tf.keras.datasets.cifar10.load_data()
#print(x_train.shape,y_train.shape)
#testinp, finaltraining = testinp / 10.0, finaltraining / 10.0
#x1=np.zeros((60000,28,28))
#y1=np.zeros((60000,1))
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(120, input_shape=(11,),activation='relu'),
    tf.keras.layers.Dense(60,activation='relu'),
    tf.keras.layers.Dense(23,activation='relu'),
    tf.keras.layers.Dense(9, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(finaltraining, finallabel, epochs=7)
model.evaluate(testinp, teslabel)
#tf.saved_model.save(model,"/Users/sunao2000/Desktop/the latest")
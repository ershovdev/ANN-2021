from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Convolution2D, MaxPooling2D, Dense, Dropout, Flatten
from tensorflow.keras import utils
import numpy as np
import matplotlib.pyplot as plt

# Задание параметров модели
batch_size = 32
num_epochs = 200
kernel_size = 3
pool_size = 2
conv_depth_1 = 32
conv_depth_2 = 64
drop_prob_1 = 0.25
drop_prob_2 = 0.5
hidden_size = 512

# Загрузка и предварительная обработка данных
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
num_train, depth, height, width = X_train.shape
num_test = X_test.shape[0]
num_classes = np.unique(y_train).shape[0]

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= np.max(X_train)
X_test /= np.max(X_train)
Y_train = utils.to_categorical(y_train, num_classes)
Y_test = utils.to_categorical(y_test, num_classes)

# Создание модели
inp = Input(shape=(depth, height, width))

conv_1 = Convolution2D(conv_depth_1, kernel_size, padding='same', activation='relu')(inp)
conv_2 = Convolution2D(conv_depth_1, kernel_size, padding='same', activation='relu')(conv_1)
pool_1 = MaxPooling2D(pool_size=(pool_size, pool_size))(conv_2)
drop_1 = Dropout(drop_prob_1)(pool_1)

conv_3 = Convolution2D(conv_depth_2, kernel_size, padding='same', activation='relu')(drop_1)
conv_4 = Convolution2D(conv_depth_2, kernel_size, padding='same', activation='relu')(conv_3)
pool_2 = MaxPooling2D(pool_size=(pool_size, pool_size))(conv_4)
drop_2 = Dropout(drop_prob_1)(pool_2)

flat = Flatten()(drop_2)
hidden = Dense(hidden_size, activation='relu')(flat)
drop_3 = Dropout(drop_prob_2)(hidden)
out = Dense(num_classes, activation='softmax')(drop_3)

model = Model(inputs=inp, outputs=out)
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Обучение и оценка модели
history = model.fit(X_train, Y_train,
          batch_size=batch_size, epochs=num_epochs,
          verbose=1, validation_split=0.1)

model.evaluate(X_test, Y_test, verbose=1)

epochs = np.arange(0, num_epochs, 1)
tr_loss = history.history["loss"]
val_loss = history.history["val_loss"]
plt.plot(epochs, tr_loss, color = "blue", label="train_loss")
plt.plot(epochs, val_loss, color = "red", label="val_loss")
plt.legend()
plt.title("Loss")
plt.show()

tr_acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]
plt.plot(epochs, tr_acc, color = "blue", label="train_acc")
plt.plot(epochs, val_acc, color = "red", label="val_acc")
plt.legend()
plt.title("Accuracy")
plt.show()
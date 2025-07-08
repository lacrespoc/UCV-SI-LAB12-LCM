import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense

# Datos de entrada (matriz de caracteristicas) y etiquetas
x_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([0, 1, 1, 0])

#Creación del modelo
model = Sequential()
model.add(Dense(2, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#Compilación del modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#Entrenamiento del modelo
model.fit(x_train, y_train, epochs=1000, batch_size=1)

#Evaluación del modelo en los datos de entrenamiento
scores = model.evaluate(x_train, y_train)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

#Hacer predicciones con el modelo entrenado
x_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predictions = model.predict(x_test)
rounded = [round(x[0]) for x in predictions]
print(rounded)
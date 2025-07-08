import sklearn
print(sklearn.__version__)
from sklearn.linear_model import Perceptron

#DATOS DE ENTRADA Y SALIDA PARA LA OPERACIÓN "AND"
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]

#CREACIÓN DE UN OBJETO PERCETRÓN
perceptron = Perceptron()

#ENTRENAMIENTO DEL PERCENTRÓN
perceptron.fit(X, y)

#REALIZAR PREDICCIONES
predicciones = perceptron.predict(X)

#IMPRIMIR PREDICCIONES
for entrada, prediccion in zip(X, predicciones):
    print(f'Entrada: {entrada} - Predicción: {prediccion}')

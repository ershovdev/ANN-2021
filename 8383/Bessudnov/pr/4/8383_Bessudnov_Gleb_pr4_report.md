# Практическое задание №4

## Задание

Необходимо реализовать нейронную сеть вычисляющую результат заданной логической операции. Затем реализовать функции, которые будут симулировать работу построенной модели. Функции должны принимать тензор входных данных и список весов. Должно быть реализовано 2 функции:

- Функция, в которой все операции реализованы как поэлементные операции над тензорами
- Функция, в которой все операции реализованы с использованием операций над тензорами из NumPy

Для проверки корректности работы функций необходимо:

1. Инициализировать модель и получить из нее веса 
2. Прогнать датасет через не обученную модель и реализованные 2 функции. Сравнить результат.
3. Обучить модель и получить веса после обучения
4. Прогнать датасет через обученную модель и реализованные 2 функции. Сравнить результат.
   
**Вариант3.** (a and b) or c

## Данные 
Ниже приведены таблица истинности, которая использовалась в данном эксперимента: 
| a | b | c |val| 
|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

## Выполнение
В ходе выполнения работы были реализованы некоторые функции: 
Реализация функции relu и sigmoid:
```Python
def naive_relu(x):
    assert len(x.shape) == 2
    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = max(x[i, j], 0)
    
    return x

def sigmoid(x):
    return 1/(1 + np.exp(x))    
```

Функция скалярного умножения векторов и умножения матриц: 
```Python
def naive_vector_vector_dot(x, y):
    assert len(x.shape) == 1
    assert len(y.shape) == 1

    max_lenght = np.maximum(y.shape[0], x.shape[0])  
    
    z = 0
    for i in range(x.shape[0]):
        z += x[i % max_lenght] * y[i % max_lenght]

    return z        

def naive_matrix_matrix_dot(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 2

    z = np.zeros((x.shape[0], y.shape[1]))
    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            z[i, j] = naive_vector_vector_dot(x[i, :], y[:, j]) 
    return z  
```    

Функция для симуляции модели посредством библиотеки numpy:
```Python
def numpy_predict(layers, input):
    k = len(layers) - 1
    res = input
    for i in range(k):
        res = np.maximum(np.dot(res, layers[i].get_weights()[0]) + layers[i].get_weights()[1], 0)
    res = sigmoid(np.dot(res, layers[k].get_weights()[0]) + layers[k].get_weights()[1])

    return 1-res
```

Функция для симуляции модели с поэлементными операциями:
```Python
def naive_predict(layers, input):
    k = len(layers) - 1
    res = input
    for i in range(k):
        res = naive_relu(naive_matrix_matrix_dot(res, layers[i].get_weights()[0]) + layers[i].get_weights()[1])
    res = sigmoid(naive_matrix_matrix_dot(res, layers[k].get_weights()[0]) + layers[k].get_weights()[1])

    return 1-res 
```

## Результаты 
Результаты до тренировки модели:
|Standard  |NumPy     |Tensors   |
|         -|         -|         -|    
|0.5       |0.5       |0.5       |
|0.50248295|0.50248293|0.50248293|
|0.5       |0.5       |0.5       |
|0.6269548 |0.6269548 |0.6269548 |
|0.5       |0.5       |0.5       |
|0.5347896 |0.53478961|0.53478961|
|0.5       |0.5       |0.5       |
|0.53281283|0.53281281|0.53281281| 


Результаты после тренировки модели:
|Standard  |NumPy     |Tensors   |
|         -|         -|         -|    
|0.26652074|0.2665207 |0.2665207 |
|0.99918234|0.99918233|0.99918233|
|0.26652074|0.2665207 |0.2665207 |
|0.9999499 |0.9999499 |0.9999499 |
|0.26652074|0.2665207 |0.2665207 |
|0.26652074|0.2665207 |0.2665207 |
|0.26652074|0.2665207 |0.2665207 |
|0.994081  |0.994081  |0.994081  | 

Видно, что во всех трех случаях результаты примерно одинаковые как до тренировки, так и после. Сомения в том какой метод использовать целесообразнее могут возникнуть в вопросах гибкости функций, скороcти написания кода и скорости его работы. Почти наверняка можно сказать, что функции для реализации сети, написанные в ходе выполнения работы с использование библиотеки NumPy и при помощи манипуляций с тензорами будут менее эффективны и менее надежны, нежели чем функции библиотеки Keras. 

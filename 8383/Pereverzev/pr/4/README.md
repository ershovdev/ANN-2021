# 8383 Pereverzev Dmitriy pr4 v2

Необходимо реализовать нейронную сеть вычисляющую результат заданной логической операции. Затем реализовать функции, которые будут симулировать работу построенной модели. Функции должны принимать тензор входных данных и список весов. Должно быть реализовано 2 функции:

Функция, в которой все операции реализованы как поэлементные операции над тензорами
Функция, в которой все операции реализованы с использованием операций над тензорами из NumPy
Для проверки корректности работы функций необходимо:

Инициализировать модель и получить из нее веса (Как получить веса слоя, Как получить список слоев модели)
Прогнать датасет через не обученную модель и реализованные 2 функции. Сравнить результат.
Обучить модель и получить веса после обучения
Прогнать датасет через обученную модель и реализованные 2 функции. Сравнить результат.

Примечание: так как множество всех наблюдений ограничен, то обучение проводить можно на всем датасете без контроля.

### Вариант 2

`(a or b) xor not(b and c)`

### Модель сети

```py

model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(3,)))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy'])

```

### Обучение

```py
resModelPr = model.predict(data)
resNative = nativeF(data, weights)
resNumpy = numpyF(data, weights)
parsedResModelPr = ("\n").join([f'{i}: {num}' for i, arr in enumerat(resModelPr) for num in arr])
parsedResNative = ("\n").join([f'{i}: {num}' for i, arr in enumerat(resNative) for num in arr])
parsedResNumpy = ("\n").join([f'{i}: {num}' for i, arr in enumerat(resNumpy) for num in arr])
f.write(f"\nmodel.predict\n{parsedResModelPr}")
f.write(f"\nnative\n{parsedResNative}")
f.write(f"\nnumpy\n{parsedResNumpy}")

```

### Результат

```py

model.predict
    0: 0.9331332445144653
    1: 0.9900527596473694
    2: 0.07459771633148193
    3: 0.9901602268218994
    4: 0.007873862981796265
    5: 0.05624300241470337
    6: 0.013570576906204224
    7: 0.9383985996246338
numpy
    0: 0.933133232755255
    1: 0.9900527638316506
    2: 0.07459776902630622
    3: 0.9901601783233541
    4: 0.007873931748353187
    5: 0.05624300947765564
    6: 0.013570576782730354
    7: 0.9383986116121481
native
    0: 0.933133232755255
    1: 0.9900527638316506
    2: 0.07459776902630617
    3: 0.9901601783233541
    4: 0.007873931748353187
    5: 0.05624300947765567
    6: 0.013570576782730354
    7: 0.9383986116121481
```

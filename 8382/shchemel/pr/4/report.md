## Вариант 1

## Задание

Необходимо реализовать нейронную сеть вычисляющую результат заданной логической операции. 
Затем реализовать функции, которые будут симулировать работу построенной модели. Функции должны принимать тензор входных данных и список весов. Должно быть реализовано 2 функции: Функция, в которой все операции реализованы как поэлементные операции над тензорами 
Функция, в которой все операции реализованы с использованием операций над тензорами из NumPy

Для проверки корректности работы функций необходимо:

Инициализировать модель и получить из нее веса (Как получить веса слоя, Как получить список слоев модели)
Прогнать датасет через не обученную модель и реализованные 2 функции. Сравнить результат.
Обучить модель и получить веса после обучения
Прогнать датасет через обученную модель и реализованные 2 функции. Сравнить результат.

## Результаты:

```
trained keras:

[[0.09092057]
 [0.0867072 ]
 [0.08187154]
 [0.11949211]
 [0.30077296]
 [0.8452872 ]
 [0.85067487]
 [0.9248086 ]]
=======================================

trained naive: 

[[0.09092059]
 [0.08670722]
 [0.08187154]
 [0.1194921 ]
 [0.30077294]
 [0.84528715]
 [0.8506748 ]
 [0.92480856]]
=======================================

trained numpy:
 
[[0.09092059]
 [0.08670722]
 [0.08187154]
 [0.1194921 ]
 [0.30077294]
 [0.84528715]
 [0.8506748 ]
 [0.92480856]]
=======================================)
```

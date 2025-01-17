# Практика №3, вариант 8

## Задание

Написать функцию, выделяющую часть матрицы фиксированного размера с центром в данном элементе (дополненное значением fill если необходимо).

## Выполнение работы

Была написана следующая функция.

```python
def pr3(matrix: np.ndarray, y, x, width, height):
    assert width > 0
    assert height > 0
    shape = matrix.shape
    col_start = y - width // 2
    col_end = y + width // 2 + width % 2
    row_start = x - height // 2
    row_end = x + height // 2 + height % 2
    assert (col_start >= 0)
    assert (row_start >= 0)
    assert (col_end <= shape[1])
    assert (row_end <= shape[0])
    return matrix[row_start:row_end, col_start:col_end]
```

На вход подается исходная матрица, координаты центра и размеры выходной таблицы.
В случае некорректных координат или размеров выбрасывается исключение.
В случае четной размерности желаемой матрицы центр смещается вправо или вниз, то есть центральный элемент по координатам `(x, y)` будет расположен правее или ниже центра на одну ячейку.

## Тестирование

Исходная матрица:

|.|0|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|---|---|
|**0**|1| 2| 3| 4| 5| 1| 23| 45| 1|
|**1**|5| 4| 3| 2| 1| 1| 23| 45| 2|
|**2**|6| 7| 8| 9| 0| 1| 23| 45| 3|
|**3**|1| 2| 3| 4| 5| 1| 23| 45| 4|
|**4**|0| 1| 2| 5| 7| 1| 23| 45| 5|

Параметры (тест 1):

```
x = 0
y = 0
width = 1
height = 1
```

На выходе (тест 1):

|.|0|
|---|---|
|**0**|1|

Параметры (тест 2):

```
x = 8
y = 4
width = 1
height = 1
```

На выходе (тест 2):

|.|0|
|---|---|
|**0**|5|

Параметры (тест 3):

```
x = 2
y = 3
width = 3
height = 2
```

На выходе (тест 3):

|.|0|1|2|
|---|---|---|---|
|**0**|7|8|9|
|**1**|2|3|4|

Параметры (тест 4):

```
x = 5
y = 30
width = 1
height = 1
```

На выходе (тест 4):

```
Traceback (most recent call last):
    ...
    assert (row_end <= shape[0])
AssertionError
```

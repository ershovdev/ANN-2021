# 8383 Pereverzev Dmitriy pr3 v8

Написать функцию, выделяющую часть матрицы фиксированного размера с центром в данном элементе (дополненное значением fill если необходимо)

### Пример входных данных

|11 |12 |13   |14   |15   |16   |17   |18 |19 |10 |
|---|---|-----|-----|-----|-----|-----|---|---|---|
|21 |22 |23   |24   |25   |26   |27   |28 |29 |20 |
|31 |32 |33   |34   |35   |36   |37   |38 |39 |30 |
|41 |42 |43   |44   |45   |46   |47   |48 |49 |40 |
|51 |52 |53   |54   |55   |56   |57   |58 |59 |50 |
|61 |62 |63   |64   |65   |66   |67   |68 |69 |60 |
|71 |72 |73   |74   |75   |76   |77   |78 |79 |70 |
|81 |82 |83   |84   |85   |86   |87   |88 |89 |80 |
|91 |92 |93   |94   |95   |96   |97   |98 |99 |90 |


### Пример вывода:

1. func(arr, 0, 0, 4, 0)

|0  |0  |0    |0    |
|---|---|-----|-----|
|0  | 0 | 0   | 0   |
|0  | 0 | 11.0| 12.0|
|0  | 0 | 21.0| 22.0|

2. func(arr, 0, 0, 4, 0)

|-599|-599|-599 |-599 |-599 |
|----|----|-----|-----|-----|
|-599| 11.0| 12.0| 13.0| 14.0|
|-599| 21.0| 22.0| 23.0| 24.0|
|-599| 31.0| 32.0| 33.0| 34.0|
|-599| 41.0| 42.0| 43.0| 44.0|
3. func(arr, 3, 4, 1, 'a')

|54|

4. func(arr, 8, 8, 10, 3)

|44.0|45.0|46.0 |47.0 |48.0 |49.0 |40.0 |3  |3  |3  |
|----|----|-----|-----|-----|-----|-----|---|---|---|
|54.0| 55.0| 56.0| 57.0| 58.0| 59.0| 50.0| 3 | 3 | 3 |
|64.0| 65.0| 66.0| 67.0| 68.0| 69.0| 60.0| 3 | 3 | 3 |
|74.0| 75.0| 76.0| 77.0| 78.0| 79.0| 70.0| 3 | 3 | 3 |
|84.0| 85.0| 86.0| 87.0| 88.0| 89.0| 80.0| 3 | 3 | 3 |
|94.0| 95.0| 96.0| 97.0| 98.0| 99.0| 90.0| 3 | 3 | 3 |
|3   | 3  | 3   | 3   | 3   | 3   | 3   | 3 | 3 | 3 |
|3   | 3  | 3   | 3   | 3   | 3   | 3   | 3 | 3 | 3 |
|3   | 3  | 3   | 3   | 3   | 3   | 3   | 3 | 3 | 3 |
|3   | 3  | 3   | 3   | 3   | 3   | 3   | 3 | 3 | 3 |

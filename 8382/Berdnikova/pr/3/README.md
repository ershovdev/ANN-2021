# Практика №3, вариант 1
## Задание:
Дано множество из p матриц (n,n) и множество из p векторов (n,1). Написать функцию для рассчета суммы p произведений матриц (результат имеет размерность (n,1))

# Решение
В функции make_dot производится:
* Проверка соответствия размерностей матриц и векторов
* Создание матрицы с помощью zeros
* Запись в матрицу результата произведения, произведение осуществляется методом dot

Также в программе предусмотрена проверка входных данных.
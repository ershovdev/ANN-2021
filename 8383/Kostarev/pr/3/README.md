# Костарев Кирилл, группа 8383
## Практическая работа № 3, вариант 1
Дано множество из p матриц (n,n) и множество из p векторов (n,1). Написать функцию для рассчета суммы p произведений матриц (результат имеет размерность (n,1)).

## Решение
Входные данные считываются с помощью функции genfromtxt(), алгоритм решения задачи выполняется в функции get_dot_sum(): сначала происходит проверка на соответствие размерностей матрицы и вектора, далее создается нулевой вектор, и в цикле по векторам и матрицам из входных данных происходит суммирование их произведений к этому вектору. Потом происходит проверка на размерность данного вектора и возвращается результат, который записывается в файл с помощью функции savetext(). Программа поддерживает обработку ошибок в случае некорректно заданных входных данных.
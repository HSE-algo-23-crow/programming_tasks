# Алгоритм Дейкстры

## Описание алгоритма

Алгоритм Дейкстры используется для поиска кратчайших путей от одной стартовой вершины до всех других вершин в графе с невзвешенными или неотрицательно взвешенными ребрами. Алгоритм гарантирует нахождение кратчайшего пути до всех вершин графа, если такие пути существуют.

### Шаги алгоритма:
1. **Инициализация:**
    - Задается стартовая вершина.
    - Создается массив расстояний, где для стартовой вершины расстояние равно нулю, а для всех остальных вершин — бесконечности.
    - Создается приоритетная очередь для обработки вершин, в которую добавляется стартовая вершина с нулевым расстоянием.

2. **Основной цикл:**
    - Извлекается вершина с минимальным расстоянием из приоритетной очереди.
    - Для каждой соседней вершины проверяется возможность улучшить расстояние до нее через текущую вершину. Если расстояние до соседней вершины можно уменьшить, оно обновляется, и соседняя вершина добавляется в очередь.

3. **Завершение:**
    - Когда очередь пуста, все кратчайшие расстояния от стартовой вершины до всех остальных вершин вычислены.

### Входные данные:
- Граф, представленный в виде списка смежности или матрицы смежности.
- Начальная вершина, от которой нужно найти кратчайшие пути.

### Выходные данные:
- Массив кратчайших расстояний от начальной вершины до всех других вершин.
- При необходимости, массив предков для восстановления путей.

### Области допустимых значений:
- Граф должен быть связным.
- Ребра графа должны иметь неотрицательные веса.

## Пример выполнения алгоритма

Рассмотрим граф, представленный в виде списка смежности:

Граф:
  0 --(4)--> 1
  0 --(1)--> 2
  1 --(1)--> 3
  2 --(2)--> 1
  2 --(5)--> 3
  3 --(3)--> 4

Здесь 0 — стартовая вершина.

### Пошаговый пример:
1. **Инициализация:**
    - Расстояния: [0, ∞, ∞, ∞, ∞]
    - Очередь: [(0, 0)] (начальная вершина 0 с расстоянием 0)

2. **Итерация 1:**
    - Извлекаем вершину 0 с расстоянием 0.
    - Обновляем расстояния для соседей:
        - Для вершины 1: новое расстояние = 0 + 4 = 4, обновляем.
        - Для вершины 2: новое расстояние = 0 + 1 = 1, обновляем.
    - Очередь: [(1, 2), (4, 1)]

3. **Итерация 2:**
    - Извлекаем вершину 2 с расстоянием 1.
    - Обновляем расстояния для соседей:
        - Для вершины 1: новое расстояние = 1 + 2 = 3, обновляем (так как 3 < 4).
        - Для вершины 3: новое расстояние = 1 + 5 = 6, обновляем.
    - Очередь: [(3, 1), (4, 1), (6, 3)]

4. **Итерация 3:**
    - Извлекаем вершину 1 с расстоянием 3.
    - Обновляем расстояния для соседей:
        - Для вершины 3: новое расстояние = 3 + 1 = 4, обновляем (так как 4 < 6).
    - Очередь: [(4, 1), (4, 3), (6, 3)]

5. **Итерация 4:**
    - Извлекаем вершину 1 с расстоянием 4. (повторное извлечение, расстояние не обновляется)

6. **Итерация 5:**
    - Извлекаем вершину 3 с расстоянием 4.
    - Обновляем расстояния для соседей:
        - Для вершины 4: новое расстояние = 4 + 3 = 7, обновляем.
    - Очередь: [(6, 3), (7, 4)]

7. **Итерация 6:**
    - Извлекаем вершину 3 с расстоянием 6. (повторное извлечение, расстояние не обновляется)

8. **Итерация 7:**
    - Извлекаем вершину 4 с расстоянием 7.

### Завершение:
- Очередь пуста.
- Конечные расстояния: [0, 3, 1, 4, 7].

Таким образом, кратчайшие расстояния от стартовой вершины 0 до всех остальных вершин составляют [0, 3, 1, 4, 7].

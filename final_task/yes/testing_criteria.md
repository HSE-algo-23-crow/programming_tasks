# Критерии тестирования


| №   | Критерий                      | Т1 | Т2 | Т3 | Т4 | Т5 | Т6 | Т7 | Т8 | T9 | T10 | T11 | T12 |
|-----|-------------------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|----|-----|-----|-----|
| 1   | **Входные данные**            |    |    |    |    |    |    |    |    |    |     |     |     |
| 1.1 | Массив путей                  | -  | -  | -  | -  | -  | -  | -  | -  | -  | +   | +   | +   |
| 1.2 | Массив феромонов              | -  | -  | -  | -  | -  | -  | -  | -  | -  | +   | +   | +   |
| 1.3 | Коээффициенты                 | +  | +  | +  | +  | +  | +  | +  | +  | +  | +   | +   | +   |
| 2   | **Выходные данные**           | -  | -  | -  | -  | -  | -  | -  | -  | -  | -   | +   | +   |
| 2.1 | Лучший найденный путь         | -  | -  | -  | -  | -  | -  | -  | -  | -  | -   | -   | -   |
| 2.2 | Длина лучшего найденного пути | -  | -  | -  | -  | -  | -  | -  | -  | -  | -   | +   | +   |
| 3   | **Сообщения об ошибках**      | +  | +  | +  | +  | +  | +  | +  | +  | +  | +   | -   | -   |
| 3.1 | ALPHA_VALUE_ERROR             | +  | -  | -  | -  | -  | -  | -  | -  | -  | -   | -   | -   |
| 3.2 | BETA_VALUE_ERROR              | -  | +  | -  | -  | -  | -  | -  | -  | -  | -   | -   | -   |
| 3.3 | ALPHA_BETA_ZERO_ERROR         | -  | -  | +  | -  | -  | -  | -  | -  | -  | -   | -   | -   |
| 3.4 | VAPORIZE_VALUE_ERROR          | -  | -  | -  | +  | +  | -  | -  | -  | -  | -   | -   | -   |
| 3.5 | Q_VALUE_ERROR                 | -  | -  | -  | -  | -  | +  | -  | -  | -  | -   | -   | -   |
| 3.6 | CITIES_NUMBER_ERROR           | -  | -  | -  | -  | -  | -  | +  | -  | -  | -   | -   | -   |
| 3.7 | ITERATIONS_NUMBER_ERROR       | -  | -  | -  | -  | -  | -  | -  | +  | -  | -   | -   | -   |
| 3.8 | DISTANCE_NEGATIVE_ERROR       | -  | -  | -  | -  | -  | -  | -  | -  | +  | -   | -   | -   |
| 3.9 | PATH_NOT_FOUND_ERROR          | -  | -  | -  | -  | -  | -  | -  | -  | -  | +   | -   | -   |
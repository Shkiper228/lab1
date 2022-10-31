# Звіт до роботи
## Тема: _Тестування програм_
### Мета роботи: _ознайомлення із функціоналом в python, який забезпечує роботу із тестами_
---
### Виконання роботи
- Результати виконання завдання *1...N*;
## Перевірка assert
    1. Ввів наданий приклад, який пояснює роботу assert
    ![alt text](https://github.com/Shkiper228/labs/blob/master/7_lw/screenshots/2022-10-31%2021%2021%2004.png?raw=true "assert")
    1. Те саме тільки із input
    ![alt text](https://github.com/Shkiper228/labs/blob/master/7_lw/screenshots/2022-10-31%2021%2022%2013.png?raw=true "assert")
    1. Те саме засобами ООП
    ![alt text](https://github.com/Shkiper228/labs/blob/master/7_lw/screenshots/2022-10-31%2021%2026%2051.png?raw=true "assert")
    1. За допомоги if
    ![alt text](https://github.com/Shkiper228/labs/blob/master/7_lw/screenshots/2022-10-31%2021%2027%2057.png?raw=true "assert")


## Юніт тести
    1. Ввів наведений код
    ![alt text](https://github.com/Shkiper228/labs/blob/master/7_lw/screenshots/2022-10-31%2021%2046%2026.png?raw=true "assert")
    1. Створимо юніт тести та спробуємо перевірити тестовий клас щоб все працювало правильно
    ![alt text](https://github.com/Shkiper228/labs/blob/master/7_lw/screenshots/2022-10-31%2022%2008%2001.png?raw=true "assert")


## Юніт тести з використання бібліотеки PyTest
    1. Добавив до app.py простий тест:

```python
    def test_app_triangle():
    """Test if we create triangle figure.
    """
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.type == fig, f"Фігура має бути {fig}"
```
    1. Запускаємо тести за допомогою pytest
    ![alt text](https://github.com/Shkiper228/labs/blob/master/7_lw/screenshots/2022-10-31%2022%2019%2005.png?raw=true "assert")

    
- результати виконання індивідуального завдання (якщо такі є);

### Висновок: 
> у висновку потрібно відповісти на запитання:
- :question: Все готово сер!;
- :question: Мета досягнута сер!;
- :question: Все засвоєно сер!;
- :question: Жодного питання без відповіді сер!;
- :question: Всі завдання виконані!;
- :question: Жодних складнощів сер!;
---
# Звіт до роботи
## Тема: _Віртуальні середовища_
### Мета роботи: _Ознайомитись із організацією віртуальних середовищ в Python_
---
### Виконання роботи
- Основи роботи з сторонніми бібліотеками
    1. Для роботи провірив наявність на моєму комп'ютері pip. Він був, але не працював за прямим викликом "pip", а лише "py -m pip". У мене коштувало трохи зусиль, аби це пофіксити:
    ![alt text](https://github.com/Shkiper228/labs/blob/master/4_lw/screenshots/2022-10-12%2012%2008%2026.png?raw=true "pip -V")
    1. Список бібліотек через команду pip list:
    ![alt text](https://github.com/Shkiper228/labs/blob/master/4_lw/screenshots/2022-10-12%2012%2008%2053.png?raw=true "pip list")
    1. Встановив біліотеку requests та використав її методи:
    ![alt text](https://github.com/Shkiper228/labs/blob/master/4_lw/screenshots/2022-10-12%2012%2010%2007.png?raw=true "requests methods example")
    ![alt text](https://github.com/Shkiper228/labs/blob/master/4_lw/screenshots/2022-10-12%2012%2010%2031.png?raw=true "requests methods example")
    1. Виконав команди:
    ![alt text](https://github.com/Shkiper228/labs/blob/master/4_lw/screenshots/2022-10-12%2012%2023%2037.png?raw=true "pip install/deistall")

- Робота у віртуальному середовищі
    1. Для створення _VENV_ виконав наступні команди:
    ![alt text](https://github.com/Shkiper228/labs/blob/master/4_lw/screenshots/2022-10-13%2010%2010%2053.png?raw=true "my_env")
    В кінці ми бачимо інший список бібліотек, бо ми вийшли з віртуального середовища

- Робота з Pipenv
    1. Виконав команди:
    ![alt text](https://github.com/Shkiper228/labs/blob/master/4_lw/screenshots/2022-10-13%2011%2005%2056.png?raw=true "pipenv install")
    Команди:
    ![alt text](https://github.com/Shkiper228/labs/blob/master/4_lw/screenshots/2022-10-12%2012%2024%2029.png?raw=true "pipenv commands")
    1. Створив файл index.py і ввів код:
    ```python
    import requests

    response = requests.get('https://httpbin.org/')
    for line in response.iter_lines():
        print(line)
    ```
    1. Запустив через VS Code:
    ![alt text](https://github.com/Shkiper228/labs/blob/master/4_lw/screenshots/2022-10-13%2011%2008%2005.png?raw=true "via VS Code run")
    Запустив через pipenv:
    ![alt text](https://github.com/Shkiper228/labs/blob/master/4_lw/screenshots/2022-10-13%2011%2011%2054.png?raw=true "via pipenv run")
    Виникла помилка, адже в віртуальному середовищі не було встановлено requests

- Робота зі змінними середовища
    1. Створив файл .env і добавив там HELLO=VOLODYMYR
    Запустив код:

    ```python
    import os
    os.environ['HELLO']
    ```

    Вийшло:
    ![alt text](https://github.com/Shkiper228/labs/blob/master/4_lw/screenshots/2022-10-13%2011%2032%2041.png?raw=true "via pipenv run")

- результати виконання індивідуального завдання (якщо такі є);

### Висновок: 
> у висновку потрібно відповісти на запитання:
- :male_sign:  В роботі зроблено :male_sign: `letherclub` :male_sign: із класом який представляє :male_sign: `name, email and count symbols of name` :male_sign:;
- :male_sign:  Так, мета досягнута, ми спустились на :male_sign: `two blocks down` :male_sign: ;
- :male_sign:  Я відновив свої :male_sign: `skills` :male_sign: ;
- :male_sign:  Жодних не вирішених завдань, :male_sign: `dungeon master` :male_sign:, не залишилось ;
- :male_sign:  :male_sign: `sir` :male_sign:, складнощів не виникло ;
- :male_sign:  :male_sign: `oh yes sir` :male_sign:!;
---
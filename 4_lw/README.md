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
    
    1. Відповіді на запитання:
        1) У конструкторі є умова, яка це забезпечує
        2. Це можна зробити, передавши який-небудь параметр методу say_hello. Адже якщо не передавати йому нічого, то він використає значення на умовчуванням
        2. Зробив метод, який підраховує кількість сиволів в імені:
    ```python
    def count_symbols_name(self):
        return f"In yours name is {len(self.name)}"
    ```
    ![alt text](https://github.com/Shkiper228/labs/blob/master/3_lw/screenshots/2022-09-23%2012%2033%2023.png?raw=true "код")

    2. 
- вставлені рисунки (скріншоти екрана або фотографії виконаного завдання у зошиті);
> якщо графічних файлів багато то краще помістити їх у окрему папку, наприклад у мене це папка `pictures`. Уважно дивіться коли вставляєте URL - файл має бути представленим як `raw`. 

![alt text](https://github.com/Shkiper228/labs/blob/master/3_lw/screenshots/2022-09-23%2012%2032%2034.png?raw=true "ІТ Коледж")
![alt text](https://github.com/Shkiper228/labs/blob/master/3_lw/screenshots/2022-09-23%2012%2015%2056.png?raw=true "ІТ Коледж")
![alt text](https://github.com/Shkiper228/labs/blob/master/3_lw/screenshots/2022-09-23%2012%2013%2058.png?raw=true "ІТ Коледж")

- вставлений код / текстовий або числовий результат / інші результати:
```python
class MyName:
    """Опис класу / Документація
    """
    total_names = 0 #Class Variable

    def __init__(self, name=None) -> None:
        self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
        MyName.total_names += 1 #modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self): 
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()
    
    def create_email(self) -> str:
        """Instance method
        """
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!"):
        """Static method
        """
        return f"You say: {message}"

    def count_symbols_name(self):
        return f"In yours name is {len(self.name)}"



print("Let's Start!")

names = ("Bohdan", "Marta", "Volodymyr", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is {type(me.count_symbols_name)} call: {me.count_symbols_name()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")
```


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
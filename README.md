# Домашние задания на курсе «Продвинутый Python»

## Профессиональная работа с Python.
1. [Import. Module. Package](https://github.com/520911/PY-advanced)  
2. [Iterators. Generators. Yield](https://github.com/520911/PY-advanced/tree/Iterators._Generators._Yield)    
3. [Decorators](https://github.com/520911/PY-advanced/tree/decorators)  

## Применение Python на практике.
4. [Tests](https://github.com/520911/PY-advanced/tree/unittests)  
5. [Selenium](https://github.com/520911/PY-advanced/tree/selenium_unittest)
6. [Regular expressions](https://github.com/520911/PY-advanced/tree/RegExp)  
7. [Web-scrapping](https://github.com/520911/PY-advanced/tree/scraping)
8. [Подготовка к собеседованию](https://github.com/520911/PY-advanced/tree/interview)  



# Import. Module. Package

1. Разработать **структуру** программы "Бухгалтерия". 
- main.py;  
- директория application:  
-- salary.py;  
-- директория db:  
\--- people.py;  
main.py - основной модуль для запуска программы.  
В модуле salary.py функция calculate_salary.  
В модуле people.py функция get_employees.  

2. Импортировать функции в модуль main.py и вызывать эти функции в конструкции.
```
if __name__ == '__main__':
```

\*3. Создать рядом с файлом main.py модуль dirty_main.py и импортировать все функции с помощью
конструкции (необязательное задание)
```
from package import *
``` 

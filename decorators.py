from datetime import datetime
import json
import hashlib
import os


class WikiIter:
    WIKI_LINK = 'https://en.wikipedia.org/wiki/'

    def __init__(self):
        self._links = []

    def __iter__(self):
        self.get_counrties_list()
        return self

    def __next__(self):
        if not self._links:
            raise StopIteration
        links = self._links.pop(0)
        return links

    def get_counrties_list(self):
        with open('countries.json') as f:
            data = json.load(f)
            for i in data:
                links = (i['name']['official'] + ' - ' + (self.WIKI_LINK + i['name']['official']).replace(' ', '_'))
                self._links.append(links)


with open('country_link.txt', 'w', encoding='UTF-8') as f:
    for i in WikiIter():
        f.write(f'{i}\n')


def logger(func):
    def wrap_func(*args, **kwargs):
        with open('log.txt', 'w', encoding='UTF-8') as f:
            f.write(f'Время вызова функции - {datetime.now()}\n'
                    f'Имя функции - {func.__name__}\n'
                    f'Аргументы функции - {args, kwargs}\n'
                    f'Результат функции - {func(*args, **kwargs)}')

    return wrap_func


def logger_path(path):
    def logger1(func):
        def wrap_func(*args, **kwargs):
            with open(path, 'w', encoding='UTF-8') as f:
                f.write(f'Время вызова функции - {datetime.now()}\n'
                        f'Имя функции - {func.__name__}\n'
                        f'Аргументы функции - {args, kwargs}\n'
                        f'Результат функции - {func(*args, **kwargs)}\n'
                        f'Путь до логов - {os.path.abspath(path)}')

        return wrap_func

    return logger1


#  @logger
@logger_path('log.txt')
def hash_generator(file):
    with open(file, encoding='UTF-8') as f:
        for line in f:
            yield hashlib.md5(line.strip().encode()).hexdigest()


hash_generator('countries.json')

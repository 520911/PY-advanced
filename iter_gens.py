import json
import hashlib


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


def hash_generator(file):
    with open(file, encoding='UTF-8') as f:
        for line in f:
            yield hashlib.md5(line.strip().encode()).hexdigest()


a = hash_generator('country_link.txt')
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

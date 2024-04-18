from collections import OrderedDict


class Wordplay:
    def __init__(self, words=[]):
        self.words = words[:]

    def add_word(self, word):
        """метод, принимающий в качестве аргумента слово и добавляющий его в набор. Если слово уже есть в наборе, метод ничего не должен делать"""
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        """метод, принимающий в качестве аргумента натуральное число n и возвращающий список слов из набора, длина которых равна n"""
        return [i for i in self.words if len(i) == n]


    def only(self, *args):
        """ метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из набора, которые включают в себя только переданные буквы"""
        return [i for i in self.words if set(i).issubset(''.join(args))]


    def avoid(self, *args):
        """метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из списка words, которые не содержат ни одну из этих букв"""
        return [i for i in self.words if set(i).isdisjoint(''.join(args))]


wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.words)
wordplay.add_word('stepik')
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)
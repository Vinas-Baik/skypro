class BasicWord():

    def __init__(self, word, subwords=None):
        self.word = word
        if subwords:
            self.subwords = subwords
        else:
            self.subwords = []
        # 2 вариант
        # self.subwords = subwords if subwords else []



    def __str__(self):
        return f'{self.word}: ' \
               f'{", ".join(sub_word for sub_word in self.subwords)}'

    def __repr__(self):
        return f"BasicWord('{self.word}', {self.subwords})"


    def check_word(self, word):
        """
        провера введенного слова в списке допустимых подслов (вернет bool),
        """
        return word.lower() in [subword.lower() for subword in self.subwords]

    def count_subword(self):
        """
        подсчет количества подслов (вернет int).
        """
        return len(self.subwords)

    def min_len_subwords(self):
        """
        выводит минимальную длину подслова в списке подслов
        """
        return min([len(subword) for subword in self.subwords])

class Player:

    def __init__(self, name):
        self.name = name
        self.words = []

    def __str__(self):
        return f'Пользователь {self.name.title()} использовал следующие ' \
               f'слова {", ".join(word for word in self.words)} '

    def __repr__(self):
        return f"Player('{self.name}', {self.words})"

    def title_name(self):
        """
        выводи имя пользователя с заглавной буквы
        :return:
        """
        return self.name.title()

    def count_user_words(self):
        """
        получение количества использованных слов (возвращает int);
        """
        return len(self.words)

    def add_word(self, word):
        """
        добавление слова в словарь пользователя
        """
        self.words.append(word)

    def check_word(self, word):
        """
        проверка слова word в списке слов пользователя
        :param word:
        :return:
        """
        return word.lower() in [word.lower() for word in self.words]

    def join_str(self, words):
        """
        вывод строки слов из words с подстветкой отгаданных пользователем слов
        :param words: слова для вывода
        """
        result_str = ''
        for t_key, t_value in enumerate(words):
            result_str += '\033[33m'+t_value+'\033[39m' if t_value.lower() in self.words else '\033[35m'+t_value+'\033[39m'
            result_str += '\n\t' if ((t_key+1) == len(words)) or ((t_key+1) % 12 == 0) else ', '

        return result_str
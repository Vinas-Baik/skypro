import data.utils as myutils
import data.myclass as myclass

URL_JSON = 'https://jsonkeeper.com/b/WJY3'
FILE_JSON = 'data\words.json'


def main():

    # Делаем красиво и просим имя пользователя
    print('\n{0:^60}\n'.format('-=== \033[32m ДОБРЫЙ ДЕНЬ \033[39m ===-'))

    user_player = myclass.Player(myutils.check_line_entry('Введи свое имя'))

    print(f'Привет \033[32m{user_player.title_name()}\033[39m')
    print('\n{0:^60}\n'.format('-=== \033[33m ДАВАЙ ПОИГРАЕМ В ИГРУ \033[39m ===-'))

    # грузим слово
    word = myutils.load_random_word(url_data=URL_JSON, file_data=FILE_JSON)

    print(f'Составь {myutils.end_count_word_str(word.count_subword())} из слова \033[32m{word.word.upper()}\033[39m')
    print(f'Слова должны быть не короче {word.min_len_subwords()} букв')

    count_words = 0

    while True:
        if count_words == word.count_subword():
            break
        print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
        user_input = myutils.check_line_entry(f'{count_words + 1}-е слово')
        if user_input in ['stop', 'стоп']:
            break
        elif len(user_input) < word.min_len_subwords():
            print(myutils.text_error(
                'Cлишком короткое слово, минимальная длина слова ' + str(word.min_len_subwords()) + ' букв'))
        elif not word.check_word(user_input):
            print(myutils.text_error('Неверно'))
            count_words += 1
        elif user_player.check_word(user_input):
            print(myutils.text_error('Уже использовалось'))
        elif not user_player.check_word(user_input) and word.check_word(user_input):
            count_words += 1
            user_player.add_word(user_input)
            print('\n{0:^40}\n'.format('-==== \033[32mВерно\033[39m ====-'))

    # Выводим статистику по игре
    print(f'\nИгра завершена \033[32m{user_player.title_name()}\033[39m, '
          f'вы угадали \033[32m{myutils.end_count_word_str(user_player.count_user_words())}\033[39m: '
          f'{", ".join(word.upper() for word in user_player.words)}!\n\n'
          f'из слова \033[32m{word.word.upper()}\033[39m можно составить следующие слова:\n'
          f'\t{user_player.join_str(word.subwords)}')


# 01. НАЧАЛО программы
# 02. НАЧАЛО программы
# 03. НАЧАЛО программы
# 04. НАЧАЛО программы
# 05. НАЧАЛО программы
# 06. НАЧАЛО программы

main()

# 01. КОНЕЦ программы
# 02. КОНЕЦ программы
# 03. КОНЕЦ программы
# 04. КОНЕЦ программы
# 05. КОНЕЦ программы
# 06. КОНЕЦ программы

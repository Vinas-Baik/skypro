import os
import json
import random
import requests
from data.myclass import BasicWord


def load_json_url(url_name):
    """
    Загрузка JSON словаря с Интернета
    :param url_name: ссылка на JSON словарь в Интернете
    :return: загруженный JSON словарь или None (если страница не доступна)
    """
    result = requests.get(url_name, verify=False)
    # print(result.status_code)
    if result.status_code != 200:
        print(text_error('Ссылка ' + url_name + ' не существует, проверьте правильность'))
        return None
    return result.json()


def text_error(text=''):
    """
    Формирование сообщения об ошибку с выделением красным цветом вызов функции без параметра выдает просто сообщение ОШИБКА
    """
    return '\033[31m' + '>> ОШИБКА - ' + text + ' << ' + '\033[39m'
    # return text


def load_json_file(name_file):
    """
    Загрузка JSON словаря с файла
    name_file:  имя файла c JSON словарем
    :return: список JSON
    """
    json_list = None  # словарь
    # формируем полный путь до файла
    # name_file = os.getcwd() + '/' + name_file
    name_file = os.path.join(*name_file.replace('\\','/').split('/'))
    # print(name_file)

    try:
        if os.path.exists(name_file):
            with open(name_file, 'r', encoding='UTF-8') as file:
                json_list = json.load(file)
        else:                                       # если файла нет, то ошибка
            print(text_error('Файл ' + name_file + ' не существует, проверьте наличие файла по указанному пути'))
    except json.JSONDecodeError:                    # если ошибка чтения JSON словаря, то выводим ошибку
        print(text_error('Файл ' + name_file + ' не является JSON файлом'))

    return json_list


def check_line_entry(text='', allowed_сhars='', error_string=''):
    """
    Функция проверяет введенную пользователем строку на пустой ввод и разрешенные символы
    :param text: строка для пользователя
    :param allowed_сhars: разрешенные символы, если список пустой, то разрешены любые символы
    :param error_string: строка с ошибкой, если строка содержит запрещенные символы
    :return: возвращаем введенную строку от пользователя
    """
    allowed_сhars = allowed_сhars.strip()
    while True:
        input_string = input(f'{text}: ').strip().lower()
        if input_string == '':
            print(text_error('Пустой ввод'))
        elif allowed_сhars == '':
            break
        else:
            is_chars_allowed = True
            for i_s in input_string:
                if i_s not in allowed_сhars:
                    is_chars_allowed = False
                    break
            if is_chars_allowed:
                break
            else:
                print(text_error(error_string))

    return input_string


def load_random_word(url_data=None, file_data=None):
    """
    загрузка случайного слова из словаря:
    1. из Интернета если указан адрес сайта
    2. из файла - если указан путь до файла
    3. если словарь не прогружен из Интернета и файла, то берется временный
    словарь для проверки 

    :param url_data - ссылка на сайт со JSON словарем
    :param file_data - путь до файла с JSON словарем
    :return - случайное слово из словаря как объект класса BasicWord
    """
    # временный словарь слов, если не доступен сайт и нет файла
    TEMP_JSON_LIST = [ {"word":"строка",
                        "subwords": ["акр","акт","кот","рак","орк","оса"]
                        },
                       {"word":"байкальск",
                        "subwords":["лайка","ласка", "сайка", "салка",
                                    "скала",  "байкал","баскак",  "калька",
                                    "сабаль", "скалка","слабак"]
                        }
                     ]
    json_list = None
    # Сначала грузим JSON словарь с Интернета, если указан путь
    if url_data != None:
        json_list = load_json_url(url_data)
        # print('из Интернета - ', url_data)
    # Если указано имя файла и JSON словарь пустой, то грузим JSON словарь c файла
    if json_list == None and file_data != None:
        json_list = load_json_file(file_data)
        # print('из файла - ', file_data)
    # Если JSON словарь пустой, то грузим JSON словарь из временной константы
    if json_list == None:
        json_list = TEMP_JSON_LIST
        # print('из константы - ')

    random_index = random.randint(0, len(json_list)-1)

    return BasicWord(json_list[random_index]['word'],
                     json_list[random_index]['subwords'])

    # 2 вариант
    #
    # random_element = random.choice(json_list)
    #
    # return BasicWord(random_element['word'], random_element['subwords'])


def end_count_word_str(count_word):
    """
    :param count_word: количество слов
    :return: Возвращает строку с окончанием (слов, слова, слово)
    """
    result_str = 'слов'
    if count_word % 100 in range(5, 21):
        result_str = 'слов'
    elif count_word % 10 == 0:
        result_str = 'слов'
    elif count_word % 10 == 1:
        result_str = 'слово'
    elif count_word % 10 in range(2, 5):
        result_str = 'слова'
    return f'{count_word} {result_str}'

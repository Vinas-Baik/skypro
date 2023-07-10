from myclass import Player, BasicWord


# str_ = 'абак алас баас байк бакс баск кайл каса ккал ласа ласк скак ' \
#             'скал слаб альба байка балка баска кабак кайла кайса каска клака лайба лайка ласка сайка салка скала байкал баскак калька сабаль скалка слабак'
#
# print(str_.split())

temp_player = Player('ааа')
temp_player.add_word('пппп')
temp_player.add_word('3222')
temp_word = BasicWord('ааа', ['fff', 'nnn'])

print(temp_player)
print(temp_word)

print(f'{temp_player!r}')
print(f'{temp_word!r}')

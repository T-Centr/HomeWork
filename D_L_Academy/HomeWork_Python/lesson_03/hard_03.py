# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


room = int(input('Введите номер комнаты: '))
block = 1
stage = 1
last_room_on_stage = 1

while room > last_room_on_stage:
    stage = stage + block
    block += 1
    last_room_on_stage = block ** 2 + last_room_on_stage

rooms_in_block = []
for i in range(block ** 2):
    rooms_in_block.append(last_room_on_stage - i)

rooms_in_block.reverse()

part_of_block_index = 0
part_of_block = []

offset = 0
for i in range(block, block ** 2 + block, block):
    if room in rooms_in_block[offset:i]:
        part_of_block_index = int(i / block)
        part_of_block = rooms_in_block[offset:i]
        break
    offset += block

stage = part_of_block_index + stage - 1
position = part_of_block.index(room) + 1

print(stage, position)

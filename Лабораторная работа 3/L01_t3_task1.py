src = not False and True or False and not True

# TODO расписать упрощение выражения
# 1 этап: избавляемся от отрицаний:
# 'not False = True' и 'not True = False'
# получаем: (True and True) or (False and False)
    # *сразу проставим скобки для следующего этапа

#2 этап: избавляемся от лонического "И":
# 'True and True = True' и 'False and False = False'
#получаем: True or False

#3 этап: избавляемся от лонического "ИЛИ"
#получаем: 'True or False = True'

result = True # TODO подставить результат выражения

print(src == result)

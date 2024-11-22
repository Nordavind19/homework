immutable_var = (5, 6, 20, 'word')
print(immutable_var)
immutable_var[1] = 15
print(immutable_var) #кортеж не изменяем, вышла ошибка
mutable_list = [8, 12, 'music', 'book', True]
print(mutable_list)
mutable_list[0] = 33
print(mutable_list)
mutable_list[2] = 'winter'
print(mutable_list)

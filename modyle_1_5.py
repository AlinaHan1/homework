immutable_var = (['a', 'b', 'c', 'd'], 1, 2, 3, 'Alina', 'Anna')
print(immutable_var)
# immutable_var[3]=[100]# являнтся не изменяемой коллекцией. Нельзя заменить/изменить элемент, есть только права на чтение.
mutable_list = ['a', 'b', 'c', 'd']
mutable_list[2] = 'W'
print(mutable_list)

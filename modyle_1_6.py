#СЛОВАРЬ
my_dict = {'Alina': 1989,
           'Olga': 1978,
           'lera': 1978,
           'Dania': 1993}
print(my_dict)
print(my_dict['Olga'])
print(my_dict.get('Anastasia'))
my_dict.update({'Max': 1999,
                'Andrey': 1956})
a = my_dict.pop('Alina')
print(a)
print(my_dict)
# МНОЖЕСТВА
my_set = {89, 99, 89, 78, 99, 'Alina', 'Anna', 'Alina', (1, 4, 8, 12)}
print(my_set)
print(my_set.update({18,'Max'}))
print(my_set)
print(my_set.remove(99))
print(my_set)


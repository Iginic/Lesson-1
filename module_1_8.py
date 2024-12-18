my_dict = {'name1':2000,'name2':1990,'name3':1970,'name4':1995,'name5':1992}
print('Соварь начальный',my_dict)
print(my_dict['name4'])
print(my_dict.get('name6','Нет такого имени'))
my_dict.update({'name50':2010,'name8':1999})
print(my_dict)  # дополнительно вывел обновленный словарь
nam = my_dict.pop('name50')
print(nam)
print('Измененный словарь',my_dict)
#
# МНОЖЕСТВО
my_set ={1,3,45,67,'IVAN', 3,4,45,6,7,67,'DENIS','IVAN'}
print('Начальное множество',my_set)
my_set.add(111)
my_set.add('ROMA')
print(my_set.discard(45))
print('Измененное множество',my_set)


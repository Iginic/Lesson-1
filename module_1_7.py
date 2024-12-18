immutable_var = 1,2, 'a', 'b'
print('Immutable tuple',immutable_var)
print(type(immutable_var))
#immutable_var[3] = 55  // кортежи не поддерживают изменение элементов
#но можно изменять элементы внутри СПИСКА в кортеже
mutable_list = [1, 2, 'a', 'b', 'XXX']
print(type(mutable_list))
print('Mutable_list',mutable_list)
mutable_list.remove('XXX') #// замена в списке XXX на Modifid
mutable_list.insert(5,'Modifid')
print('Mutable LiST',mutable_list)




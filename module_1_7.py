immutable_var = 1,2, 'a', 'b'
print('Immutable tuple',immutable_var)
#immutable_var[3] = 55  // кортежи не поддерживают изменение элементов
#но можно изменять элементы внутри СПИСКА в кортеже
mutable_list = 0,[1,2, 'a','b', 'XXX']
mutable_list[1][4] = 'Modifed' #// замена в списке XXX на Modifid
print('Mutable LiST',mutable_list[1:])




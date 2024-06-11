# Максимум в списке
# Подсчёт четных чисел в списке
# Уникальный список


def find_max(list_):
    '''
    Возвращает максимум, поиск перебором.
    :param list_:
    исходный список на входе
    :return:
    максимальное значение в списке
    '''
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_

# print(find_max([1, 2, 1, 5, 0]))
print(find_max.__doc__)
#или:
print(help(find_max))

def count_even(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter

# print(count_even([2, 2, 3, 4, 2, 1, 0]))

def unique1(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list

def unique2(list_):
    '''
    Делает список из списка, сохраняя только уникальные элементы.
    :param list_:
    исходный список на входе
    :return:
    список-результат, содержащий уникальные значения (без учета типа, то есть True и 1, или "" и False -- не различаются!)
    '''
    set_ = set(list_)
    return list(set_)

print(unique1([None, '', 1, 2, 3, 4, 5, 6, 0, 'a', False, True, -3.1416, 7, 8, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8]))
print(unique2([None, '', 1, 2, 3, 4, 5, 6, 0, 'a', False, True, -3.1416, 7, 8, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8]))

print(help(unique2))

str_ = unique2.__doc__
print('Помощь по функции:', str_)

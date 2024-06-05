def info(txt, *types, name_author='Alexey A.Tsukanoff', **values):
    print('Пояснение:', txt)
    print('Аргументы:', values)
    for key, value in values.items():
        print(key, '>>', value)
    print(types, '\n', name_author)

#аргументы: позиционные, *списки, именованные, **словари

info('Пример использования параметров разных типов',
     1, 2, 3, "Ч",
     name_author='Tsukanov',
     name='Alexey',
     middle=' A.',
     course='Python++')

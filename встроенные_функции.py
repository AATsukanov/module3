# int()  --> int(input())
# float()
# bool()
# str()
# list()
# tuple()
# dict()
# set()

#len(), sum(), min(), max(), round(), zip()

#isinstance(), any(), all()

#type(), id()

salary = [2300, 1800.801234, 5000, 1234.583434, 7500.122323]
print(round(sum(salary)/len(salary), 2), '- средняя зарплата в компании')
print(round(max(salary), 2), '- максимальная зарплата в компании')
print(round(min(salary), 2), '- минимальная зарплата в компании')

names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
zipped = zip(names, salary)
#print('list:', list(zipped))
#print('tuple:', tuple(zipped))
#print('dict:', dict(zipped))
#print('set:', set(zipped))

zipped = dict(zipped)
print(zipped['Денис'], '- зарплата Дениса')
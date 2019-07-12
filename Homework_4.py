

# Задание-1:
chisla = [ x for x in range(10)]
kvadrati = [y**2 for y in chisla]
print(chisla)
print(kvadrati)

# Задание-2:
fruits = ['apple', 'banana', 'citrus', 'orange']
frukti = ['kiwi', 'apple', 'cherry', 'orange']
fr = [a for a in fruits for i in fruits if a == frukti[fruits.index(i)]]
print(fr)

# Задание-3:
from random import randint
list_1 = [randint(0,100) for i in range(10)]
list_2 = [g for g in list_1 if g % 3 == 0 and g >= 0 and g % 4 != 0]
print(list_2)

# Задача - 1
import re
user = {'name': input('введите имя '), 'surname': input('введите фамилию '), 'email': input('введите email ')}
while re.match('([A-Z]+[a-z]+)', user['name']) == None:
    user['name'] = input('неверно указано имя ')
while re.match('([A-Z]+[a-z]+)', user['surname']) == None:
    user['surname'] = input('неверно указано фамилия ')
while re.match('([a-z]+@[a-z]+\.(ru|com|net)', user['email']) == None:
    user['email'] = input('неверно указан email ')
# Козловцев Сергей

# Задание - 1
def prtinfo(name, age, city):
    a = name + ', ' + str(age) + 'год(а), проживает в городе ' + city
    return a

t = prtinfo('Ana', 23, 'Moscov')
print(t)

# Задание - 2
def chisla(a, b, c ):
    return max(a, b, c)

a = chisla(23, 40, 12)
print(a)

# Задание - 3
def stroki(*args):
    return max(args, key = len)

print(stroki('Sergey', 'Alex', 'Ivan', 'Kiril', 'Vasiliy'))

# Задание - 1
names = ['Ana', 'Vlad', 'Alex', 'Vasya']
salaris = [520000, 410000, 230000, 190000]
slr = {}
for i in names:
    slr[i] = salaris[names.index(i)]
    if salaris[names.index(i)] >= 500000:
        slr.popitem()
    else:
        file = open('salary.txt','a',encoding = 'utf-8')
        file.write('{} = {}\n'.format(i,slr[i]))
        file.close
print(slr)

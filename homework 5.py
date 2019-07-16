import os

# Задача-1:
def zadacha11():
    a = os.getcwd()
    for i in range(9):
        os.mkdir('dir_',i)

def zadacha12()
    for i in range(9):
        os.remove('dir_',i)

# Задача-2:
def zadacha2():
    for i in os.listdir():
        print(i)

# Задача-3:
def zadacha3():
    a = os.getcwd()
    open((a,'.copy'),'w')
'''
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.


'''
s=0
a=float(1)
b=int(input('Количество элементов (n) :'))\

cicle=range(b)
for f in cicle:
    a=a/2
    print (a)
    s = s + a

print('сумма n элементов:',s)

a, b, c = map(int, input().split())
lista=[a, b, c]
lista.sort()
#1 caso sejam iguais
if a==b or a==c or b==c:
    print("S")
#2 caso haja soma
elif lista[2]==(lista[0]+lista[1]):
    print("S")
#3 caso haja subtração
elif lista[0]==(lista[2]-lista[1]):
    print("S")
#4 não consegue
else:
    print("N")
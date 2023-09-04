n=int(input())
casas=set()
lista=[]
for i in range(n):
    casa=int(input())
    casas.add(casa)
soma=int(input())
for i in casas:
  for j in casas:
    if i+j==soma:
      lista.append(i)
      lista.append(j)
print(lista[0], lista[1])
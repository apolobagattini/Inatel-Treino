nomes, escolhido=map(int, input().split())
chamada=[]
for i in range(nomes):
    aluno=input()
    chamada.append(aluno)
ordem=sorted(chamada)
print(ordem[escolhido-1])
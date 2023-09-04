n=int(input())
numeros=list(map(float, input().split()))
raizes=[]
for i in numeros:
  raizes.append((i)**(1/2))
for i in raizes:
  print(f'{i:.4f}')
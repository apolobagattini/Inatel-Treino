def liis(): return list(map(int, input().split()))
count = 0
N, C, M = map(int, input().split())
carimbadas = set(liis())
compradas = set(liis())
total = carimbadas.intersection(compradas)
print(C-len(total))

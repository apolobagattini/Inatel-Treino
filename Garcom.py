bandejas=int(input())
quebrados=0
for i in range(bandejas):
  latas, copos=map(int, input().split())
  if latas>copos:
    quebrados+=copos
print(quebrados)
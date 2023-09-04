disponivel=int(input())
p1=int(input())
p2=int(input())
p3=int(input())
pokemon=[p1, p2, p3]
pokemon.sort()
consumidos=0
count=0
while consumidos<=disponivel:
    for i in pokemon:
        consumidos+=i
        count+=1
print(count)
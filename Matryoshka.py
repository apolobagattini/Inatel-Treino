n=int(input())
bagunca=list(map(int, input().split()))
ordem=sorted(bagunca)
count=0
mexidos=[]
for i in range(n):
    if ordem[i]!=bagunca[i]:
        count+=1
        mexidos.append(bagunca[i])
mexidos.sort()
print(count)
print(" ".join(map(str, mexidos)))
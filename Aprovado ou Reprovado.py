m1, m2 = map(float, input().split())
media=(m1+m2)/2
if media>=7:
    print("Aprovado")
elif media>=4:
    print("Recuperacao")
else:
    print("Reprovado")
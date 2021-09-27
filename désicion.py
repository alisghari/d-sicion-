nc=float(input("saisir la nôte de controle: "))
ns=float(input("saisir la nôte de sythése : "))
my=(nc+(ns*2))/3
print("votre moyenne = ",my)
if my>=17:
    print("admis, mention trés bien")
    print("mabrouk")
elif 15<=my<17:
    print("admis, mention bien")
    print("mabrouk")
elif 12<=my<15:
    print("admis, mention assez bien")
    print("mabrouk")
elif 10<=my<12:
    print("admis, passable")
    print("mabrouk")
else:
    print("refusé, aucune mention")

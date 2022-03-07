nivel_agua=int(input("digite el nivel del agua: "))
if(nivel_agua<200):
    print("nivel del agua bajo")
elif(nivel_agua>=200 and nivel_agua<=450):
    print("nivel del agua estable")
elif(nivel_agua>=450):
    print("nivel del agua exidel el limite")
else:
    print("numero invalido")

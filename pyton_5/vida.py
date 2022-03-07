vida=float(input("digite su edad: "))
if(vida>=0 and vida<=14):
    print("niño")
elif(vida>14 and vida<=28):
    print("joven")
elif(vida>28 and vida<=60):
    print("adulto")
elif(vida>=60):
    print("adulto mayor")
else:
    print("digito no valido")

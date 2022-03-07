mes=input("digite un mes:").lower()
input(mes)
if(mes=='diciembre' or mes=='enero' or mes=='febrero' or mes=='marzo'):
    print("invierno")
elif(mes=='abril' or mes=='mayo' or mes=='junio'):
    print("verano")
elif(mes=='julio' or mes=='agosto' or mes=='septiembre'):
    print("otoño")
elif(mes=='octubre' or mes=='nobiembre' or mes=='diciembre'):
    print("primavera")
else:
    print("mes no valido")
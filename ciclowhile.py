centinela=100

#ciclo while
print("***MENU***")
print("1.saludar")
print("2.despedir")
print("0.salir")
while(centinela!=0):
    centinela=int(input("Digita una opcion"))
    if(centinela==1): print("Hellowda")
    elif(centinela==2): print("Chinga Tu Madre")
    elif(centinela==0): break #Break sirve para parar el programa ignorando el resto del codigo, como un freno de mano
    else: print ("Digite una opcion valida")
else:
    print("termine")
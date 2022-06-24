#Espressioni booleane

#ugualianza
print(5==5)

#disugualianza
print("casa"!="gatto")

#maggioranza
print(6>9)
print(6>=6) # ugalianza

#minoranza
print(6<9)
print(6<=9) #o ugalianza

#Operatori logici
print("Operatori Logici")
print(1==1 and 2==2)
print(1==1 or 2==1)
print(not 1==1)

#Istruzioni condizionali
n=int(input("Inserisci un numero positivo: "))

if(n<0):
    print("%d non è un numero positivo"%n)
elif(n%2==0):
    print("%d è un numero pari"%n)
else:
    print("%d è un numero dispari"%n)
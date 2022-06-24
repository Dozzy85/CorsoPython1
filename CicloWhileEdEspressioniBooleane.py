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

#Ciclo while
n=int(input("Fino a che numero vuoi contare? "))
i=0

while i<n:
    if(i%3==0):
        i+=2
        continue
    print(i)
    i+=1
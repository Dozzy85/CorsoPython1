cat="Eleon"
age=2
peso=5.678

print("Il mio gatto si chiama "+cat+" ed ha "+str(age)+" anni")

#formattazione (old school)
print("Il mio gatto si chiama %s ed ha %d anni e pesa %.2f kg"%(cat,age,peso))

#Formattazione (new school)
print("Il mio gatto si chiama {nome} e ha {age} anni e pesa {peso} kg".format(nome=cat,age=age,peso=peso))

#Formattazione Python 3.6 o superiore
print(f"Il mio gatto si chiama {cat} e ha {age} anni e pesa {peso} kg")
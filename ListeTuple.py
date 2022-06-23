#Liste
my_list=[10,5,8,3,11,2]
print(type(my_list))

#indexing
print(my_list[0])
print(my_list[1])
print(my_list[-1])

#slicing
print(my_list[0:3]) #Prende i valori dalla posizione 0 alla posizione 2
print(my_list[:5]) #Prende i valori dalla posizione 0 alla posizione 4
print(my_list[2:]) #Prende i valori dalla posizione 2 alla posizione fino alla fine
print(my_list[:]) #Prende tutti i valori
print(my_list[::-1]) #inverte gli elementi della lista

#modifica
my_list[0]=0 #modifica il valore in posizione 0
print(my_list)
my_list[-2:]=[7,1] #modifica gli ultimi 2 valori della lista
print(my_list)

#verifica se valore è presente nella lista
animals=["cane","gatto","topo"]
print(animals)
print("uomo" in animals)
print("gatto" in animals)

#rimuovere elementi dalla lista
#per valore
animals.remove("gatto")
print(animals)
#per indice (estrazione)
animals=animals.pop(1)
print(animals)

#aggiungere elementi alla lista
animali=["cane","gatto","topo"]
print(animali)
animali.append("bestia demoniaca")
print(animali)

#inserimento in una posizione stabilita
animali.insert(1,"topolino")
print(animali)

#Tuple a differenza delle liste una volta definite non possono essere modificate
my_tupla=(10,5.5,"ciao","ciao")
print(my_tupla)

#ottenere l'indice di un elemento
print(my_tupla.index("ciao"))

#conta degli elementi
print(my_tupla.count("ciao"))

#metodo per la lunghezza lista e tupla e anche per le stringhe
print(len(my_list))
print(len(my_tupla))

hello="hello python"
print(hello)
print(len(hello))
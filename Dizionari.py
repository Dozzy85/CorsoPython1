items={"latte":3,"riso":2,"tofu":5}
print(items)

#accesso al singolo elemento
print(items["latte"])

#modificare un elemento
items["latte"]=2
print(items)

#creazione nuovo elemento
items["cereali"]=1
print(items)

#aggiungere un dizionario dentro un'altro dizionario
items["yogurt"]={"fragola":2,"bianco":3}
print(items)

#ottenere il numero associato all'elemento
print(items["yogurt"]["fragola"])

#per ottenere solo le chiavi del dizionario
print(items.keys())
keys=list(items.keys()) #conversione dizionario in lista

#per ottenere solo i valori
values=list(items.values())
print(values)

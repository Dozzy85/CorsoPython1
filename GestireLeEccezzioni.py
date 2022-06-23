num=input("inserisci un numero: ")
try:
    print(type(num))
    num = int(num)
    print("il numero che hai inserito è: ", num)
except ValueError:
    print("Il dato che hai inserito non è un numero")
#Funzioni

b=5
h=3

def compute_area(b,h):
    return b*h/2

area=compute_area(b,h)
print(area)

shopping_list = ["tofu","latte di soia","riso basmanti","yogurt greco"]

def print_shopping_list(shopping_list, owner = "Andrea"):
    print("La lista della spesa di %s"%owner)
    for i, entry in enumerate(shopping_list):
        print("%d) %s"%(i+1,entry))

print_shopping_list(shopping_list, owner="Chicco") #se non si specifica l'owner viene usato
                                                   # quello inserito di default nella funzione
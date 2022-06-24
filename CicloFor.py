#Ciclo for
n=int(input("Fino a che numero vuoi stampare? "))

#per tutti i numeri i che vanno da 0 a n dove n viene inserito da tastiera esegue una certa operazione
for i in range(0,n):
    print(i)

#Swapping (old school)
a="cane"
b="gatto"
print(a,b)
temp=a
a=b
b=temp
print(a,b)

#Swapping (new school)
a="cane"
b="gatto"
print(a,b)
a,b=b,a
print(a,b)

#ciclo for per il calcolo della successione di Fibonacci
n=int(input("Quanti numeri di Fibonacci vuoi stampare? "))

fib_num=0
next_fib_num=1

for i in range(n):
    fib_num,next_fib_num=next_fib_num,next_fib_num+fib_num
    print("%d° numero di Fibonacci = %d"%(i+1,fib_num))

#ciclo for con la lista
shopping_list=["tofu","latte di soia","riso basmanti","yogurt greco"]

for i,entry in enumerate(shopping_list):
    print("%d) %s"%(i+1,entry))
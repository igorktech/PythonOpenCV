## fibonachi
import math
from re import M
from tkinter import N


# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     print(fibonacci(n - 1) + fibonacci(n - 2))
#     return fibonacci(n - 1) + fibonacci(n - 2)
 
 
#print(fibonacci(10))

fib1 = 0
fib2 = 1
 
n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)
 
i = 0
while i < n:
    fib_sum = 0
    
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
    print("Значение этого элемента:", fib_sum)
    
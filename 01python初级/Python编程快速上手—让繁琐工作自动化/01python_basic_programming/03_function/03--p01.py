def hello(m,n):
    try:
        s = m/n
        print(s)
    except ZeroDivisionError:
        print("Stupid!!!")
    else:
        print("666")

m = int(input("First Number:"))
n = int(input("Second Number:"))
hello(m, n)
print("hahaha")

import random
s = random.randint(1, 3)
print(s)
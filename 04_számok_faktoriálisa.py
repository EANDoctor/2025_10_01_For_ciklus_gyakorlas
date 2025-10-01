"""
4. Számok faktoriálisa
Számold ki egy adott szám faktoriálisát! A számot a felhasználótól kérd be!
"""
#Easier mode:
    # import math
    # x = int(input("Kérek egy számot!"))
    # print(math.factorial(x))

x = int(input("Kérek egy számot!"))
y = 1

for i in range(1, x + 1):
    y *= i

print(f"A szám faktoriálisa: {y}")
"""
2. Két szám közötti számok
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
2.1. Ha b nagyobb, mint a, akkor csökkenő sorrendben írasd ki őket.
"""

a = int(input("Írd be az első számot!"))
b = int(input("Írd be a második számot!"))

if a < b:
    for i in range (a + 1,b):
        print(i)
else:
    for i in range(a - 1, b, -1):
        print(i)
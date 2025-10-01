"""
1. Összegszámítás
Kérj be egy egész számot (pl. 10; 13;  20…), és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.
"""

x = int(input("Kérek egy egész számot!"))
y = 0

for i in range(1, x):
    y += i

print(f"A számok 1 től való összege {y}")
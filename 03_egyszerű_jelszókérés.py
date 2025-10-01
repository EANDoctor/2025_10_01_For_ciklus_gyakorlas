"""
3. Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják.
Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""
#helyes jelszó "1234"

user_jelszo = int(input("Kérem a jelszót!"))

while user_jelszo != 1234:
    user_jelszo = int(input("Kérem a jelszót!"))
else:
    print("Sikeres belépés!")
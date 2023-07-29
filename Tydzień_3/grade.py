# -*- coding: utf-8 -*-
def wynik(punkty): 
    procent = punkty/50*100
    if procent > 90:
        return "bdb"
    elif procent > 70:
        return "db"
    elif procent >50:
        return "dost"
    elif procent > 30:
        return "dop"
    else:
        return "ndst"

students = int(input("Podaj liczbę studentów: "))
for student in range(students):
    punkty = int(input ('Podaj liczbę punktów'))
    grade = wynik(punkty)
    procent = punkty/50*100
    print('Wynik tego studenta to ', procent , '%')
    print("Twoja ocena to ", {grade} )










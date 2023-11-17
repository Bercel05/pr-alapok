# feladat_014
"""
Kérjük be a vezeték és keresztnevünket 
Irassuk ki eljárás segítségével nevünket
pl:
Be: "Kérem a vezetékneved: Márkus"
Be: "Kérem a keresztneved: Bercel"
Ki: "A nevem: Márkus Bercel"

"""

vezeteknev = input (f"Kérem a vezetéknevedet:")
keresztnev = input (f"Kérem a keresztnevedet:")

def nev(vnev, knev):
    print(f"A nevem: {vnev} {knev}")

nev(vezeteknev, keresztnev)
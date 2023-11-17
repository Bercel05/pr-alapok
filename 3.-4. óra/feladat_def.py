#feladat_015
"""
Kérjük be a vezeték és keresztnevünket 
Irassuk ki függvény segítségével nevünket
pl:
Be: "Kérem a vezetékneved: Márkus"
Be: "Kérem a keresztneved: Bercel"
Ki: "A nevem: Márkus Bercel"

"""

vezeteknev = input (f"Kérem a vezetéknevedet:")
keresztnev = input (f"Kérem a keresztnevedet:")

def nevf(vnev, knev):
    nevem = vnev + '' + knev
    return nevem

print(f"A nevem: {nevf(vezeteknev, keresztnev)}")
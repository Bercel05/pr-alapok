# feladat_009
"""

Kérjünk be két egész számot, szám1 és szám2.
Hasonlítsuk össze a két számot, és írassuk ki, hogy a szam1 kisebb mint a szam2,
vagy a szam2 kisebb mint a szam1, 
vagy a szam1 egyenlő szam2-vel.
"""

szám1=input("Írj be egy számot /szám1/ :")
szám2=input("Írj be mégeegy számot /stám2/ :")
szám1=int(szám1)
szám2=int(szám2)

"""
if szám1 <szám2:
    print(f"A szám1 kisebb mint a szám2")
elif szám2 < szám1:
    print(f"A szám2 kisebb mint a szám1")
else:
    print(f"A szám1 egyenlő a szám2-vel)
    """
    #--------------

"""
if szám1 <szám2:
    print(f"A szám1 kisebb mint a szám2")
if szám2 < szám1:
    print(f"A szám2 kisebb mint a szám1")
if szám1 == szám2:
print(f"A szám1 egyenlő a szám2-vel") 
"""  
#-----------------

if szám1 < szám2:
    print(f"A szám1 kisebb mint a szám2")
elif szám2 < szám1:
    print(f"A szám2 kisebb mint a szám1")
elif szám1 == szám2:
     print(f"A szám1 egyenlő a szám2-vel")
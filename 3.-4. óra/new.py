
honapok = ['január', 'február','március', 'április', 'május', 'június']

for honap in honapok:
    honap = honap.upper()	
    print(honap)
print(honapok)
for index in range(len(honapok)):
        # az eredeti listaelem módosul!
        honapok[index] = honapok[index].upper()
print(honapok)



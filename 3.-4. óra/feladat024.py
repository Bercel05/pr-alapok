# üres listát hoz létre
 # üres listát hoz létre
gyumolcsok = []

# kezdőérték nélküli változót hoz létre
gyumolcs = None
while gyumolcs != '':
 gyumolcs = input('Adj meg egy gyümölcsöt! ')
 if gyumolcs != '':
  # hozzáfűzi a listahoz
  gyumolcsok.append(gyumolcs)
print(gyumolcsok)  
print(f"A gyumolcsok lista elemeinek száma: {len(gyumolcsok)}")

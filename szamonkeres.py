#Márkus Bercel 10.c 1. csoport 2023 10. 13.
jegy = input("Kérek egy jegyet 1-5:")
jegy = int(jegy)

if jegy == 5: 
  print(f"A jegyed {jegy} jeles")
elif jegy == 4:
  print(f"A jegyed {jegy} jó")
elif jegy == 3:
  print(f"A jegyed {jegy} közepes")
elif jegy == 2:
  print(f"A jegyed {jegy} elégséges")
elif jegy == 1:
 print(f"A jegyed elégtelen")
else:
    print(f"A jegyed {jegy},  nem megfelelő")
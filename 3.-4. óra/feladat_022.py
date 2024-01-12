#feladat 22
szam = int(input(f"Kérek egy páros számot"))
szam_fele = int(szam/2)

darab_karakter = 1
sor = 1
while sor <= szam_fele:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0', end='')
        oszlop = oszlop + 1
    print('') 
    darab_karakter = darab_karakter + 1
    sor = sor + 1   








darab_karakter = 4
sor = 1
while sor <= szam_fele:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0', end='')
        oszlop = oszlop + 1
    print('') 
    darab_karakter = darab_karakter - 1
    sor = sor + 1   
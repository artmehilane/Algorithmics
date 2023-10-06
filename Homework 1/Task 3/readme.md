*Art Mehilane & Raido Priske*
# Task 3: Rekursiivne Fibonacci funktsioon

Fibonacci jada on arvujada, kus iga järgnev number on kahe eelmise numbri summa. Esimesed kaks numbrit on tavaliselt 0 ja 1. See tähendab, et jada näeb välja selline: 0,1,1,2,3,5,8,13,21,34,…


1. Kui n = 0, siis funktsioon tagastab 0, sest see on esimene number Fibonacci jadas.

2. Kui n = 1, siis funktsioon tagastab 1, sest see on teine number Fibonacci jadas.

3. Kui n > 1, siis funktsioon leiab n-nda numbri, liites(n-1) numbri ja (n-2) numbri. Selleks kutsub funktsioon ennast kaks korda: esimesel korral n-1 ja teisel korral n-2.

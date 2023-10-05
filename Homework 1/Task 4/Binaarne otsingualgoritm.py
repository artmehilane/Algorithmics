def binaarne_otsing(loend, otsitav):

    # Loendi algus ja lopppunkt
    algus = 0
    lopp = len(loend) - 1

    # Otsingu jätkamine, kuni loendi alguspunkt on väiksem või võrdne lõpppunktiga
    while algus <= lopp:
        kesk = (algus + lopp) // 2

        # Kui leidsime otsitava, siis tagastame täisarvu indeksi
        if loend[kesk] == otsitav:
            return kesk

        # Otsib parema poole pealt
        elif loend[kesk] < otsitav:
            algus = kesk + 1

        # Otsib vasaku poole pealt
        else:
            lopp = kesk - 1

    return "Täisarvu loendis pole"


sorteeritud_loend = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

otsitav_element = int(input("Sisesta otsitav täisarv: "))

tulemus = binaarne_otsing(sorteeritud_loend, otsitav_element)

print("Tulemus:", tulemus)
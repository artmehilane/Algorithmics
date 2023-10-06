

def fibonacci(n):

    # Kui n on 0, tagasta 0
    if n == 0:
        return 0

    # Kui n on 1, tagasta 1
    elif n == 1:
        return 1

    # Kui n on suurem kui 1, arvutab n-nda Fibonacci numbri
    else:
        # Tagasta n-1 ja n-2 Fibonacci numbrite summa
        return fibonacci(n-1) + fibonacci(n-2)

# Küsi kasutajalt sisendit

sisend = input("Palun sisesta arvu positsioon Fibonacci jadas: ")

n = int(sisend)

tulemus = fibonacci(n)

print(f"{n}-ndas positsioonis olev Fibonacci number on: {tulemus}")
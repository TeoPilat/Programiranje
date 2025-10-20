# 1. Traženje unosa
n_unos = input("Unesite pozitivan cijeli broj (n): ")

# 2. Pretvorba stringa u integer
try:
    n = int(n_unos)
    if n <= 0:
        print("Molimo unesite pozitivan cijeli broj.")
        n = 0 # Postavljanje na 0 kako petlja neće raditi
except ValueError:
    print("Pogrešan unos! Molimo unesite cijeli broj.")
    n = 0

if n > 0:
    print(f"\nBrojevi od 1 do {n}:")

    # 3. Korištenje for petlje s range()
    # range(1, n + 1) ide od 1 do n (uključivo)
    for broj in range(1, n + 1):
        # 4. Ispis unutar petlje
        print(broj)
#Traženje unosa (rezultat je string)
godine_unos = input("Unesite svoje godine: ")

# 2. Pretvorba stringa u integer (cijeli broj)
# Važno: Ovdje je pretpostavljeno da korisnik unosi valjan broj
try:
    godine = int(godine_unos)
except ValueError:
    print("Pogrešan unos! Molimo unesite cijeli broj.")
    # Zaustavljanje programa u slučaju pogrešnog unosa
    # Ovdje ćemo samo preskočiti daljnju provjeru radi jednostavnosti
    # U stvarnom programu bi se tražio ponovni unos
    godine = -1 # Postavljanje na vrijednost koja ne prolazi provjeru punoljetnosti


# 3. Grananje i 4. Ispis
if godine >= 18:
    print("Punoljetni ste.")
elif godine >= 0: # Provjera ako je unos bio ispravan broj (pozitivan ili nula)
    print("Maloljetni ste.")
# Inače, ako je godine = -1 zbog greške, ništa se ne ispisuje
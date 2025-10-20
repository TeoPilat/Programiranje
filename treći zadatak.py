# 1. i 2. Definiranje funkcije s return naredbom
def kreiraj_pozdrav(ime):
    """
    Prima ime kao string i vraća formatiranu pozdravnu poruku.
    """
    # Kreiranje pozdravnog stringa pomoću f-stringa
    pozdravna_poruka = f"Pozdrav, {ime}!"
    
    # Vraćanje kreiranog stringa
    return pozdravna_poruka

# -- Glavni dio programa --

# 3. Pozivanje funkcije i spremanje povratne vrijednosti
pozdrav_za_ivanu = kreiraj_pozdrav("Ivana")
pozdrav_za_filipa = kreiraj_pozdrav("Filip")

# 4. Ispis rezultata
print(pozdrav_za_ivanu)
print(pozdrav_za_filipa)

# Možete pozvati funkciju i direktno u print
print(kreiraj_pozdrav("Gost"))
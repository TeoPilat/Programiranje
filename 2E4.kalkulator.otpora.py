#izbornik za kalkulator
print("----------------------")
print("izbornik za kalkulator")
print("----------------------")
print("izaberite operaciju:")
print("1.izračun napona struje")
print("2. izračun otpora tsruje")
print("3.izračun jakosti struje")
opcija=int(input("izaberite operaciju (1 / 2 / 3 / 4 / 5):"))
#struktura grananja
if opcija == 1:
    print("izračun napona struje")
    jakost=int(input("upiši jakost struje: "))
    otpor=int(input("upiši otpor: "))
    napon=jakost*otpor
    print(f"napon struje je: {napon} V")
elif opcija ==2:
    print("izračun otpora struje")
    napon=int(input("upiši napon: "))
    jakost=int(input("unesite jakost struje: "))
    otpor=napon/jakost
    print(f"otporje: {otpor} Ohm")
elif opcija ==3:
    print("izračun jakosti struje")
    napon=int(input("upiši napon: "))
    otpor=int(input("unesite otpor struje: "))
    jakost=napon/otpor
    print(f"jakost struje je: {jakost} A")
elif opcija ==4:
    print("izračun otpor serijskih otpornika")
    R1=int(input("upiši otpor prvog otpornika: "))
    R2=int(input("unesite otpor drugog otpornika: "))
    Rs=R1+R2
    print(f"ukupni otpor serijskih otpornika  je: {Rs} Ohm")
elif opcija ==5:
    print("izračun otpor paralelnih otpornika")
    R1=int(input("upiši otpor prvog otpornika: "))
    R2=int(input("unesite otpor drugog otpornika: "))
    Rp=(R1*R2)/(R1*R2)
    print(f"ukupni otpor serijskih otpornika  je: {Rp} Ohm")
else:
    print("pogrešan unos")

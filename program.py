#izbornik za kalkulator pretvorbe mjernih jedinica
print("izbornik za kalkulator pretvorbe mjernih jedinica")
print("----------------------")
print("izaberite opciju:")
print("0.izlaz")
print("1.pretvaranje volti")
print("2. pretvaranje ampera")
print("3.pretvaranje ohma")
print("----------------------")
while True:
    opcija=float(input("izaberite opciju (0 / 1 / 2 / 3):"))
    #struktura grananja
    if opcija == 1:
       Napon=float(input("upiši napon u voltima: "))

       U=Napon*1000
       print(f"napon u milivoltima je: {U} mV")
    #pretvorba ampera
    elif opcija == 2:  
        Jakost=float(input("upiši jakost struje u amperima: "))
        I=Jakost*1000
        print(f"jakost struje u miliamperima je: {I} mA")
    #pretvorba ohma
    elif opcija == 3:
        Otpor=float(input("upiši otpor u ohmima: "))
        R=Otpor*1000
        print(f"otpor u kiloohmima je: {R} kOhm")
    elif opcija ==0:
        print("izlaz iz programa")
        break
    else:
        print("pogrešan unos, pokušaj ponovno")
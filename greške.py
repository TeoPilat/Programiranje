#izbornik za kalkulator pretvorbe mjernih jedinica
print("izbornik za kalkulator pretvorbe mjernih jedinica")
print("----------------------")
def ispisi_izbornik():
    print("izaberite opciju:")
    print("0.izlaz")
    print("1.pretvaranje volti")
    print("2. pretvaranje ampera")
    print("3.pretvaranje ohma")
   
    print("----------------------")
def V_u_mV():
    Napon=float(input("upiši napon u voltima: "))

    U=Napon*1000
    print(f"napon u milivoltima je: {U} mV")
def A_u_mA():
    Jakost=float(input("upiši jakost struje u amperima: "))
    
    I=Jakost*1000
    print(f"jakost struje u miliamperima je: {I} mA")
def ohm_u_Kohm():
    Otpor=float(input("upiši otpor u ohmima: "))
    
    R=Otpor/1000
    print(f"otpor u kiloohmima je: {R} kOhm")
while True:
    ispisi_izbornik()
    try:
        opcija=float(input("izaberite opciju (0 / 1 / 2 / 3):"))
    except Exception as greska:
        print(f"pogrešan unos..{greska}")
        continue
#struktura grananja
    if opcija == 1:
      V_u_mV()
    #pretvorba ampera
    elif opcija == 2: 
        A_u_mA()
    #pretvorba ohma
    elif opcija == 3:
       ohm_u_Kohm()
    elif opcija ==0:
        print("izlaz iz programa")
        break#
    else:
        print("pogrešan unos, pokušaj ponovno")
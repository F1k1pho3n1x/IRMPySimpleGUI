from PySimpleGUI import * 
from datetime import datetime
from playsound import playsound

def dodaj_nulu(jedinica_vremena):
    if jedinica_vremena < 10:
        return "0" + str(jedinica_vremena)
    return str(jedinica_vremena)

def daj_trenutno_vreme():
    trenutno_vreme = datetime.now()
    casovi = dodaj_nulu(trenutno_vreme.hour)
    minuti = dodaj_nulu(trenutno_vreme.minute)
    sekunde = dodaj_nulu(trenutno_vreme.second)
    return casovi + ":" + minuti + ":" + sekunde

def pusti_alarm():
    global je_pusteno, brojac
    if not je_pusteno:
        playsound("alarm.mp3", block=False)
        je_pusteno = True
    brojac += 1
    if brojac == 20:
        je_pusteno = False
        brojac = 0

def formiraj_listu_dd(granica):
    lista = []
    for i in range(granica):
        if i < 10:
            lista.append("0" + str(i))
        else:
            lista.append(str(i))
    return lista

sadrzaj = [
    [Text(daj_trenutno_vreme(), key="SAT", font=("Digital-7", 60), size=(10, 0), justification="center")],
    [
        Combo(formiraj_listu_dd(24), default_value="00", size=(5, 5), key="A_SAT"),
        Text(":", font=("", 20)),
        Combo(formiraj_listu_dd(60), default_value="00", size=(5, 5), key="A_MIN"),
        Button("Setuj", size=(5, 1)),
        Button("Odloži", size=(5, 1)),
        Button("Poništi", size=(5, 1)),
     ],
]

sacuvan_alarm = "00:03"
prozor = Window("Digitalni sat", sadrzaj)
je_pusteno = False
brojac = 0
broj_odlaganja = 0

while True:
    dogadjaj, vrednosti = prozor.read(timeout=450)
    if dogadjaj == WIN_CLOSED:
        break

    trenutno_vreme = daj_trenutno_vreme()
    if trenutno_vreme == sacuvan_alarm:
        pusti_alarm()

    if dogadjaj == "Poništi":
        sacuvan_alarm = ""
        broj_odlaganja = 0
        popup("Alarm je uspešno poništen.")
        
    if dogadjaj == "Odloži":
        if sacuvan_alarm != "":
            if broj_odlaganja < 3:
                vreme = sacuvan_alarm.split(":")
                sa_hh = int(vreme[0])
                sa_mm = int(vreme[1])
                uk_min = sa_hh * 60 + sa_mm + 5
                sa_cas = (uk_min // 60) % 24
                sa_min = uk_min % 60
                sa_hh = dodaj_nulu(sa_cas)
                sa_mm = dodaj_nulu(sa_min)
                sacuvan_alarm = sa_hh + ":" + sa_mm + ":00"
                broj_odlaganja += 1
                popup("Alarm je uspešno odložen:", sacuvan_alarm)
            else:
                popup("Alarm ne možete odložiti.")
        else:
            popup("Alarm nije prethodno podešen.")

    if dogadjaj == "Setuj":
        a_hh = prozor["A_SAT"].get()
        a_mm = prozor["A_MIN"].get()
        sacuvan_alarm = a_hh + ":" + a_mm + ":00"
        popup("Alarm je uspešno setovan na:", sacuvan_alarm)


    prozor["SAT"].Update(trenutno_vreme)
    prozor.refresh()

prozor.close()

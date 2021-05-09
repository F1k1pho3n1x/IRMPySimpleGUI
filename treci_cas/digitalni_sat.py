import PySimpleGUI as sg
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
    [sg.Text(daj_trenutno_vreme(), key="SAT", font=("Digital-7", 60), size=(10, 0), justification="center")],
    [
        sg.Combo(formiraj_listu_dd(24), default_value="00", size=(5, 5), key="A_SAT"),
        sg.Text(":", font=("", 20)),
        sg.Combo(formiraj_listu_dd(60), default_value="00", size=(5, 5), key="A_MIN"),
        sg.Button("Setuj", size=(5, 1)),
        sg.Button("Odloži", size=(5, 1)),
        sg.Button("Poništi", size=(5, 1)),
     ],
]

sacuvan_alarm = ""
prozor = sg.Window("Digitalni sat", sadrzaj)
je_pusteno = False
brojac = 0

while True:
    dogadjaj, vrednosti = prozor.read(timeout=450)
    if dogadjaj == sg.WIN_CLOSED:
        break

    trenutno_vreme = daj_trenutno_vreme()
    if trenutno_vreme == sacuvan_alarm:
        pusti_alarm()

    if dogadjaj == "Poništi":
        sacuvan_alarm = ""

    if dogadjaj == "Odloži":
        # Dopuniti
        pass

    if dogadjaj == "Setuj":
        a_hh = prozor["A_SAT"].get()
        a_mm = prozor["A_MIN"].get()
        sacuvan_alarm = a_hh + ":" + a_mm + ":00"
        sg.popup("Alarm je uspešno setovan na:\n", sacuvan_alarm)

    prozor["SAT"].Update(trenutno_vreme)
    prozor.refresh()

prozor.close()
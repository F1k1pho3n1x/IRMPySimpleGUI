import PySimpleGUI as sg
from datetime import datetime
from playsound import playsound

def formiraj_listu_dd(granica):
    lista = []
    for i in range(granica):
        if i < 10:
            lista.append("0" + str(i))
        else:
            lista.append(str(i))
    return lista

def play_alarm():
    global is_playing, alarm_end
    if not is_playing:
        is_playing = True
        playsound("alarm.mp3", block=False)
    print(alarm_end)
    if alarm_end == 20:
        alarm_end = 0
        is_playing = False
    alarm_end += 1



def dodaj_cifru(vreme):
    if vreme < 10:
        return "0" + str(vreme)
    return vreme

sadrzaj = [
    [sg.Text("00:00:00", font=("Digital-7", 55), size=(9, 0), key="EKRAN", justification="center")],
    [
        sg.Listbox(formiraj_listu_dd(24), size=(5, 5), enable_events=False, key='CASOVI'),
        sg.Text(":", font=("Digital-7", 50)),
        sg.Listbox(formiraj_listu_dd(60), size=(5, 5), enable_events=False, key='MINUTI'),
        sg.Text("", size=(1, 0)),
        sg.Button("Setuj alarm", size=(6, 3)),
        sg.Button("Zaustavi", size=(6, 3))
    ],
]

prethodno = datetime.now()
trenutno = datetime.now()
prozor = sg.Window("Alarm", sadrzaj)
sacuvan_alarm = ""
is_playing = False
alarm_end = 0

while True:
    dogadjaj, vrednosti = prozor.read(timeout=500)
    if dogadjaj == sg.WIN_CLOSED:
        break

    trenutno = datetime.now()

    hh = dodaj_cifru(trenutno.hour)
    mm = dodaj_cifru(trenutno.minute)
    ss = dodaj_cifru(trenutno.second)

    if str(hh) + ":" + str(mm) == sacuvan_alarm:
        play_alarm()

    vreme = f"{hh}:{mm}:{ss}"
    prozor["EKRAN"].Update(vreme)

    if dogadjaj == "Setuj alarm":
        a_hh = prozor["CASOVI"].get()
        a_mm = prozor["MINUTI"].get()
        if len(a_hh) != 0 and len(a_mm) != 0:
            a_hh = a_hh[0]
            a_mm = a_mm[0]
            sacuvan_alarm = a_hh + ":" + a_mm
            sg.popup("Podešen je alarm za\n" + sacuvan_alarm)

    if dogadjaj == "Zaustavi":
        sacuvan_alarm = ""

    prozor.refresh()


prozor.close()
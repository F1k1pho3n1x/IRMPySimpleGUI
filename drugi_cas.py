import PySimpleGUI as sg
from math import sqrt

def osvezi_ekran(ispis):
    prozor["EKRAN"].Update(ispis)
    prozor.refresh()

def izracunaj():
    global operator, unos
    if dogadjaj == "=":
        drugi_broj = float(unos)
        if operator == "+":
            unos = prvi_broj + drugi_broj
        elif operator == "-":
            unos = prvi_broj - drugi_broj
        elif operator == "*":
            unos = prvi_broj * drugi_broj
        elif operator == "/":
            unos = prvi_broj / drugi_broj
        if unos - int(unos) == 0:
            unos = str(int(unos))
        operator = "X"

def obrisi():
    global prvi_broj, drugi_broj, operator, unos
    if dogadjaj == "C":
        prvi_broj = 0
        drugi_broj = 0
        operator = "X"
        unos = "0"

def unesi():
    global unos
    if dogadjaj == "." and "." not in unos:
        unos += "."
    if dogadjaj in "1234567890":
        if unos[0] == "0" and "." not in unos:
            unos = dogadjaj
        else:
            unos += dogadjaj

def sacuvaj_binarne_operacije():
    global prvi_broj, unos, operator
    if dogadjaj in "+-*/":
        prvi_broj = float(unos)
        operator = dogadjaj
        unos = "0"

def stepenuj():
    global unos, operator
    if dogadjaj in "²√":
        if dogadjaj == "²":
            unos = float(unos) ** 2
        else:
            unos = sqrt(float(unos))
        if unos - int(unos) == 0:
            unos = int(unos)
        operator = "X"

sadrzaj = [
    [sg.InputText("0", key="EKRAN", size=(14, 0), font=("Digital-7", 25))],
    [
        sg.Button("7", size=(4, 2)),
        sg.Button("8", size=(4, 2)),
        sg.Button("9", size=(4, 2)),
        sg.Button("/", size=(4, 2)),
        sg.Button("²", size=(4, 2)),
    ],
    [
        sg.Button("4", size=(4, 2)),
        sg.Button("5", size=(4, 2)),
        sg.Button("6", size=(4, 2)),
        sg.Button("*", size=(4, 2)),
        sg.Button("√", size=(4, 2)),
    ],
    [
        sg.Button("1", size=(4, 2)),
        sg.Button("2", size=(4, 2)),
        sg.Button("3", size=(4, 2)),
        sg.Button("-", size=(4, 2)),
        sg.Button("C", size=(4, 2))
    ],
    [
        sg.Button(".", size=(4, 2)),
        sg.Button("0", size=(4, 2)),
        sg.Button("=", size=(4, 2)),
        sg.Button("+", size=(4, 2)),
    ],
]

prozor = sg.Window("Digitron", sadrzaj)
prozor["EKRAN"].Disabled = True

prvi_broj = 0
drugi_broj = 0
operator = "X"
unos = "0"
je_sacuvan = False
sacuvan = "0"

while True:
    dogadjaj, vrednosti = prozor.read()
    if dogadjaj == sg.WIN_CLOSED:
        break

    unesi()
    sacuvaj_binarne_operacije()
    stepenuj()
    izracunaj()
    obrisi()
    osvezi_ekran(unos)

prozor.close()

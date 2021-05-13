from PySimpleGUI import *
from datetime import datetime


def izgenerisi_dugmice():
    matrica = []
    indeks = 0
    for i in range(6):
        red = []
        for j in range(7):
            naziv = "Dugme" + str(indeks)
            red.append(
                Button(
                    "",
                    font=("Arial", 20),
                    key=naziv,
                    button_color=("black","white"),
                    border_width=0
                ))
            indeks += 1
        matrica.append(red)
    return matrica




sadrzaj = izgenerisi_dugmice()

prozor = Window("Kalendar", sadrzaj, background_color="#FFFFFF")

def osvezi_matricu():
    global sadrzaj, prozor
    for i in range(6):
        for j in range(7):
            indeks = i * 7 + j
            prozor["Dugme" + str(indeks)].Update(str(indeks))

#print(datetime(year=2021, month=5, day=9).weekday())


izgenerisi_dugmice()


while True:
    dogadjaji, vrednosti = prozor.read(timeout=500)
    if dogadjaji == WIN_CLOSED:
        break

    osvezi_matricu()
    prozor.refresh()

    if dogadjaji == "Klikni":
        print(prozor["KALENDAR"].get_text())

prozor.close()

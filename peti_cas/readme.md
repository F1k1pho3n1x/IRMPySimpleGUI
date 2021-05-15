# Zadaci
1) ~~Napisati funkciju **date_to_str()** koja pomoću **datetime.now()** formira i vraća string današnjeg dana u formatu **"DD/MM/GGGG"**.~~  
```python
# LJUBICA
def date_to_str():
    datum = datetime.now()
    dan = datum.day
    mesec = datum.month
    godina = datum.year

    if dan < 10:
        DD = "0" + str(dan)
    else:
        DD = str(dan)

    if mesec < 10:
        MM = "0" + str(mesec)
    else:
        MM = str(mesec)

    if godina < 10:
        GGGG = "0" + str(godina)
    else:
        GGGG = str(godina)

    return DD + "/" + MM + "/" + GGGG
```
3) Napisati funkciju **date_to_int()** koja pomoću **datetime.now()** formira i vraća listu celih brojeva, kojim se određuje današnji dan u formatu **[dan, mesec, godina]**.  
4) ~~Napisati funkciju **timef_to_str()** koja pomoću **datetime.now()** formira i vraća string trenutnog vremena u formatu **"ČČ:MM:SS"**.~~  
```python
# DARKO
def timef_to_str():
  trenutno_vreme = datetime.now().hour, datetime.now().minute, datetime.now().second
  
  if trenutno_vreme[0] < 10:
    trenutno_vreme[0] = "0" + str(trenutno_vreme[0])

  if trenutno_vreme[1] < 10:
    trenutno_vreme[1] = "0" + str(trenutno_vreme[1])

  if trenutno_vreme[2] < 10:
    trenutno_vreme[2] = "0" + str(trenutno_vreme[2])

  vreme_u_formatu = str(trenutno_vreme[0]) + ":" + str(trenutno_vreme[1]) + ":" + str(trenutno_vreme[2])

  return vreme_u_formatu
```
5) ~~Napisati funkciju **times_to_str()** koja pomoću **datetime.now()** formira i vraća string trenutnog vremena u formatu **"ČČ:MM"**.~~  
```python
# DARKO
def times_to_str():
    trenutno_vreme = datetime.now().hour, datetime.now().minute

    if trenutno_vreme[0] < 10:
        trenutno_vreme[0] = "0" + str(trenutno_vreme[0])

    if trenutno_vreme[1] < 10:
        trenutno_vreme[1] = "0" + str(trenutno_vreme[1])

    vreme_u_formatu = str(trenutno_vreme[0]) + ":" + str(trenutno_vreme[1])

    return vreme_u_formatu
```
6) Napisati funkciju **popuni_vrednosti(lista_dana_u_mesecu, dan_u_nedelji)** koja menja prikaz u matrici dugmića, tako da se prikazuju redom datumi počev od 1 do poslednjeg dana u mesecu (uključujući). **Nepopunjena polja, moraju ostati prazna.** 
7) ~~Napisati funkciju **dohvati_indeks_meseca(mesec)** koja za prosleđeno ime meseca, napisano nezavisno kojim slovima ("januar", "JANUAR", "JaNUAr", ...), vraća celobrojnu vrednost indeksa meseca tog dana.~~  
```python
# TEODOR
def dohvati_indeks_meseca(mesec):
  mesec = mesec.lower()
  if "jan" in mesec:
    return 0
  if "feb" in mesec:
    return 1
  if "mar" in mesec:
    return 2
  if "apr" in mesec:
    return 3
  if "maj" in mesec:
    return 4
  if "jun" in mesec:
    return 5
  if "jul" in mesec:
    return 6
  if "avg" in mesec:
    return 7
  if "sep" in mesec:
    return 8
  if "okt" in mesec:
    return 9
  if "nov" in mesec:
    return 10
  if "dec" in mesec:
    return 11
 ```
9) ~~Napisati funkciju **dohvati_broj_dana(indeks, godina)** koja za prosleđen broj indeksa meseca i godine, određuje koliko taj mesec ima dana.~~  
```python
# TEODOR
def dohvati_broj_dana(indeks, godina):
  broj_dana=31
  if indeks==1:
    if je_prestupna(godina):
      broj_dana-=2
    else:
      broj_dana-=3
  if indeks==3 or indeks==5 or indeks==8 or indeks==10:
    broj_dana-=1
  return broj_dana
```  
9) ~~Napisati funkciju **je_prestupna(godina)** koja za prosleđenu godinu vraća **True** ili **False** u zavisnosti od toga da li je godina prestupna ili ne.~~   
```python
# TEODOR
def je_prestupna(godina):
  if godina%4==0:
    if godina%100==0:
      if godina%400==0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
```
10) Napisati funkciju **dodaj_nulu()**  

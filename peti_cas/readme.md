# Zadaci
1) Napisati funkciju **date_to_str()** koja pomoću **datetime.now()** formira i vraća string današnjeg dana u formatu **"DD-MM-GGGG"**.  
2) Napisati funkciju **date_to_int()** koja pomoću **datetime.now()** formira i vraća listu celih brojeva, kojim se određuje današnji dan u formatu **[dan, mesec, godina]**.  
3) Napisati funkciju **timef_to_str()** koja pomoću **datetime.now()** formira i vraća string trenutnog vremena u formatu **"ČČ:MM:SS"**.  
4) Napisati funkciju **times_to_str()** koja pomoću **datetime.now()** formira i vraća string trenutnog vremena u formatu **"ČČ:MM"**.  
5) Napisati funkciju **popuni_vrednosti(lista_dana_u_mesecu, dan_u_nedelji)** koja menja prikaz u matrici dugmića, tako da se prikazuju redom datumi počev od 1 do poslednjeg dana u mesecu (uključujući). **Nepopunjena polja, moraju ostati prazna.** 
6) Napisati funkciju **dohvati_indeks_meseca(mesec)** koja za prosleđeno ime meseca, napisano nezavisno kojim slovima ("januar", "JANUAR", "JaNUAr", ...), vraća celobrojnu vrednost indeksa meseca tog dana.  
7) Napisati funkciju **dohvati_broj_dana(indeks, godina)** koja za prosleđen broj indeksa meseca i godine, određuje koliko taj mesec ima dana.  
8) Napisati funkciju **je_prestupna(godina)** koja za prosleđenu godinu vraća **True** ili **False** u zavisnosti od toga da li je godina prestupna ili ne.  
```python
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

# Treći čas

## Domaći zadatak 
**Rok za predaju:** 11.05.2021. (19:59) \
**Fajl:** *digitalni_sat.py*
1) Otkloniti pass ključnu reč u 67. liniji 
2) Definisati funkcionalnost dugmeta *Odloži* pomoćnom funkcijom ili unutar uslova u 66. liniji
3) Poslednja sačuvana vrednost različita od praznog stringa u promenljivoj *sacuvan_alarm* treba biti povećana za 5 minuta od trenutka klika na dugme (Primer: "23:58:00")
4) Razdvojiti sacuvan_alarm u časove, minute i sekunde (Primer: "23", "58", "00")
5) Uvećati vrednost minuta za 5, vodeći računa o tome da se na pravi način ažuriraju minuti i časovi (Primer: ne 24h 3m nego 0h 3m)
6) Formatirati string alarma na odgovarajući način (Primer: HH:MM:SS, odnosno "00:03:00")
7) Sačuvati novi alarm u promenljivoj *sacuvan_alarm*

## Puštanje audio fajla
1) Uključiti modul playsound

```python 
from playsound import playsound
```

2) Pozvati funkciju playsound i proslediti .mp3/.wav fajl

```python 
playsound("alarm.mp3")
```

3) Postavljanjem Block na False onemogućava da zvuk zablokira ostatak aplikacije

```python 
playsound("alarm.mp3", block=False)
```

# Treći čas

## Puštanje audio fajla
1) Uključiti modul playsound
`from playsound import playsound`
2) Pozvati funkciju playsound i proslediti .mp3/.wav fajl
`playsound("alarm.mp3")`
3) Postavljanjem Block na False onemogućava da zvuk zablokira ostatak aplikacije
`playsound("alarm.mp3", block=False)`

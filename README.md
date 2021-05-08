# IRMPySimpleGUI

## Instalacija u lokalu
1) Pokrenuti Command Prompt ili Windows Powershell
2) Instalirati pip
3) Pokrenuti komandu:
`pip install PySimpleGUI`

## Instalacija u replit okruženju:
1) Prijaviti se za nalog na Repl.it platformi
2) Napraviti sopstvenu granu proizvoljnog naziva
3) Nalepiti naredbu:
`import PySimpleGUI`

## Skelet svake forme

```
import PySimpleGUI as sg

sadrzaj = [
	[],
]

prozor = sg.Window("Naziv aplikacije", sadrzaj)

while True:
	dogadjaj, vrednosti = prozor.read()
	if dogadjaj == sg.WIN_CLOSED:
		break
		
prozor.close()
```

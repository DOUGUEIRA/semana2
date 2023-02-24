segundosInput = int(input("Por favor, entre com o numero de segundos que deseja converter:"))

dias = segundosInput // 86400
diasRest = segundosInput % 86400
horas = diasRest // 3600
horasRest = diasRest % 3600
minutos = horasRest // 60
segundos = horasRest % 60

diaTexto = ""
horaTexto = ""
minutoTexto = ""
segundoTexto = ""

if(dias > 1):
    diaTexto = "dias,"
else:
    diaTexto = "dia,"

if(horas > 1):
    horaTexto = "horas,"
else:
    horaTexto = "hora,"

if(minutos > 1):
    minutoTexto = "minutos,"
else:
    minutoTexto = "minuto,"

if(segundos > 1):
    segundoTexto = "segundos."
else:
    segundoTexto = "segundo."

print(dias, diaTexto, horas, horaTexto, minutos, minutoTexto, segundos, segundoTexto)
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

minutos = hour * 60 + mins
minutos2 = minutos + dura

minutosF = minutos2 % 60
hora = minutos2 // 60 % 24
print(hora, ":", minutosF, sep="")

print(2 // 4)
x = 1
y = 2
print(1 // 2 * 3)
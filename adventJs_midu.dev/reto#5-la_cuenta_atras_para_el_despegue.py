# import these modules if you need them:
# from datetime import datetime, timezone
import math
from datetime import datetime
import re
from typing import List


def time_until_take_off(from_time: str, take_off_time: str) -> int:
    def separar_fecha_hora(fecha_hora: str) -> List[int]:
        fecha_y_hora = re.split(r'\*|@|\|| ', fecha_hora)
        for i, parte in enumerate(fecha_y_hora):
            if parte == 'NP':
                break
            else:
                fecha_y_hora[i] = int(parte)
        return fecha_y_hora 
    
    hora_dada = separar_fecha_hora(from_time)
    hora_despegue = separar_fecha_hora(take_off_time)
    dt_dada = datetime(hora_dada[0], hora_dada[1], hora_dada[2], hora_dada[3], hora_dada[4],hora_dada[5])
    dt_despegue = datetime(hora_despegue[0], hora_despegue[1], hora_despegue[2], hora_despegue[3], hora_despegue[4],hora_despegue[5])
    diferencia = dt_despegue - dt_dada
    segundos = math.floor(diferencia.total_seconds())
    return segundos


takeoff = '2025*12*25@00|00|00 NP'
# desde el 24 diciembre 2025, 23:59:30, 30 segundos antes del despegue
print(time_until_take_off('2025*12*24@23|59|30 NP', takeoff))
# 30

# justo en el momento exacto
print(time_until_take_off('2025*12*25@00|00|00 NP', takeoff))
# 0

# 12 segundos después del despegue
print(time_until_take_off('2025*12*25@00|00|12 NP', takeoff))
# -12
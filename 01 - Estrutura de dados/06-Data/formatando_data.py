#converter e formatar datas e horas. Usando o metodos:
# 'strftime" (string format time)
# 'strptime' (strinf parse time).
from datetime import date, datetime, time, timedelta


data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = '%d/%m/%Y %H:%M'
mascara_en = '%Y-%m-%d %H:%M'
print(data_hora_atual)
print(data_hora_str)
print("-" * 50)

print(data_hora_atual.strftime(mascara_ptbr))

print("-" * 50)
d = datetime.now()
#formato data e hora
print(d.strftime("%d/%m/%Y %a %H:%M"))
print(type(data_hora_str))
#convertendo string para datetime

data_convertida = datetime.strptime(data_hora_str, mascara_en)

print(type(data_convertida))
#timedelta
from datetime import date, datetime, time, timedelta
#           ano, mes, dia
tipo_carro = 'G' # 'P' 'M' 'G'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()


if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou as ; {data_atual} e ficara pronto ás : {data_estimada}")
    
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou as ; {data_atual} e ficara pronto ás : {data_estimada}")
    
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou as ; {data_atual} e ficara pronto ás : {data_estimada}")
    
print(date.today() - timedelta(days=1))


#para trabalhar com hora precisa trabalhar com datetime junto
#monta data e hora e depois extrai so a parte da hora

resultado = datetime(2023, 7, 25, 10 ,19, 20) - timedelta(hours=1)
print(resultado.time())
print("-" * 50)

print(datetime.now().date())
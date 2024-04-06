# datetime(ano, mes, dia)
# datetime(ano, mes, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz type-pytz
from datetime import datetime

# from pytz import timezone

# data = datetime.now(timezone('America/Fortaleza'))
data = datetime.now()
print(data.timestamp()) # Isso está na base de dadsos
print(datetime.fromtimestamp(1712367478))
# data_str_data = '2024-04-05 21:55:24'
# data_str_data = '05/04/2024'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2024, 4, 5, 21, 55, 24, tzinfo=timezone('Asia/Tokyo'))
# print(data)
# data = datetime.strptime(data_str_data, data_str_fmt)
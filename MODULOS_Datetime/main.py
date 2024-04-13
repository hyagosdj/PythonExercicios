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
# from datetime import datetime

# from pytz import timezone

# data = datetime.now(timezone('America/Fortaleza'))
# data = datetime.now()
# print(data.timestamp()) # Isso está na base de dadsos
# print(datetime.fromtimestamp(1712367478))
# data_str_data = '2024-04-05 21:55:24'
# data_str_data = '05/04/2024'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2024, 4, 5, 21, 55, 24, tzinfo=timezone('Asia/Tokyo'))
# print(data)
# data = datetime.strptime(data_str_data, data_str_fmt)

# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2024 08:20:20', fmt)

# delta = timedelta(days=10, hours=2)
delta = relativedelta(data_fim, data_inicio)
print(delta.days, delta.years)

# print(data_fim + delta)
# print(data_fim - delta)
# print(data_fim)
# print(data_fim + relativedelta(seconds=60, minutes=10))


# print(data_fim - data_inicio)
# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())

# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)
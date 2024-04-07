"""
Formatando datas do datetime
datetime.strftime('DATA', 'FORMATO')
https://docs.python.org/3/library/datetime.html
"""
from datetime import datetime

# fmt = '%d/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'), data.day, data.month, data.year)
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%Y'))
print()
print(data.strftime('%Y'), type(data.strftime('%Y')), data.year, type(data.year))
print(data.strftime('%d'), type(data.strftime('%d')), data.day, type(data.day))
print(data.strftime('%m'), type(data.strftime('%m')), data.month, type(data.month))
print()
print(data.strftime('%H'), type(data.strftime('%H')), data.month, type(data.hour))
print(data.strftime('%M'), type(data.strftime('%M')), data.month, type(data.minute))
print(data.strftime('%S'), type(data.strftime('%S')), data.month, type(data.second))
print()
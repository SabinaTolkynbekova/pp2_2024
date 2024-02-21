
import datetime

today = datetime.datetime.now()
subtractfivedays = today - datetime.timedelta(days = 5)
subtractfivedays = subtractfivedays.replace(microsecond=0)

print(subtractfivedays)



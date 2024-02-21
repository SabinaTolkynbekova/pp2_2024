import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)

diff = today - yesterday
print(diff)


import datetime
x = datetime.datetime.now()
print(f"Yesterday: {x.day - 1}-{x.month}-{x.year}")
print(f"Today: {x.day}-{x.month}-{x.year}")
print(f"Tomorrow: {x.day + 1}-{x.month}-{x.year}")
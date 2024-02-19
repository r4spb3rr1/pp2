import datetime
x = datetime.datetime.now()
subtracted_day = x.day - 5
subtracted_year = x.year
subtracted_month = x.month

print(f"Subtracted date: {subtracted_day}-{subtracted_month}-{subtracted_year}")
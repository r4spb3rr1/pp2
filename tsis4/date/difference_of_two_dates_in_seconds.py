import datetime
first = input("Input first date in format day month year: ").split()
second = input("Input second date in format day month year: ").split()
first_date = datetime.datetime(int(first[2]), int(first[1]), int(first[0]))
second_date = datetime.datetime(int(second[2]), int(second[1]), int(second[0]))

print("the differnce betweem two dates in seconds =",  (second_date - first_date).days * 3600)
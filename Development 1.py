hours = int(input("Enter number of hours: "))
mins = int(input("Enter number of minutes: "))
seconds = int(input("Enter number of seconds: "))
hours_total = (hours * 60) * 60
mins_total = mins * 60
total = hours_total + mins_total + seconds
print("The total number of seconds is {0}.".format(total))


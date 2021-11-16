import time
sec = int(input("Enter the number fo seconds: "))
days = sec // 86400
print ("Days is ", days)
reminder_afterdays = sec % 86400
print ("Seconds left: ", reminder_afterdays)
hours = reminder_afterdays // 3600
print ("Hours is: ", hours)
reminder_afterhours = reminder_afterdays % 3600
print("Seconds left: ", reminder_afterhours)
min = reminder_afterhours // 60
print ("Minutes is: ", min)
reminder_aftermin = reminder_afterhours % 60
print ("Seconds is: ", reminder_aftermin )
print ("days: %02d hours: %02d minutes:%02d seconds %02d" % (days,hours,min,reminder_aftermin))
print (days,hours,min,reminder_aftermin)

t = time.localtime()
print ("time.asctime(t): %s" % time.asctime(t))
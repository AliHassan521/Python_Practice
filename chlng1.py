import time
a = time.strftime('%H:%M:%S')
print("Current time in H/M/S = ", a)
h = int(time.strftime('%H'))
if h>=1 and h<=12:
   print("good morning")
elif h>12 and h<=16:
   print("good afternoon")
else:
   print("good evening")
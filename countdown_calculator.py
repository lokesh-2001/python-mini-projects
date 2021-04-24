import time as t

#----------------METHOD 1 -----------------------------
"""seconds=int(input("how many seconds to wait: "))
for i in range(seconds):
    print(str(seconds-i)+" seconds remaining")
    t.sleep(1)
print("TIMES UP!!!!")"""


#----------------METHOD 2 -----------------------------
"""#Import time library
import time as t
## Countdown function starts here
def stopwatch(sec):
while sec:
minn, secc = divmod(sec, 60)
timeformat = '{:02d}:{:02d}'.format(minn, secc)
print(timeformat, end='\r')
t.sleep(1)
sec -= 1
print('Goodbye!\n')
## calling stopwatch function
stopwatch(15)"""

#----------------METHOD 3 -----------------------------
def countdown(tme):
    print(f"this window will remain open for {tme} more seconds")
    while (tme>=0):
        print(tme,end='. . . ')
        t.sleep(1)
        tme-=1
    print("Goodbye!!")
tme=100
countdown(tme)
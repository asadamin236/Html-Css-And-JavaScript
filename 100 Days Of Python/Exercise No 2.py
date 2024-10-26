import time
t = time.strftime('%H:%M:%S')
h = int(time.strftime("%H"))

if h >= 0 and h <= 12:
    print("Good Morning")
elif h > 12 and h <= 17:
    print("Good Evening")
elif h > 17 and h < 12:
    print("Good Night")
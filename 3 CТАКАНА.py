import random
a = random.randint(0,1)
b = random.randint(0,1)
c = random.randint(0,1)
d = int(input())
#e = input("натыкал угадал")
#f = input("верно")
#g = input("правильно")

if a == 1:
    b = 0
    c = 0
elif b == 1:
    c = 0
    a = 0
elif c == 1:
    a = 0
    c = 0
if d == 1:
    if a == 1:
        print("натыкал угадал")
    else:
        ("в молоко")
if d == 2:
    if b == 1:
        print("натыкал угадал")
    else:
        ("в молоко")
if d == 3:
    if c == 1:
        print("натыкал угадал")
    else:
        ("в молоко")
if d == 4:
    if a == 0 and b == 0 and c == 0:
        print("натыкал угадал")
    else:
        ("в молоко")
        

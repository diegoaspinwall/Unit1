#Diego Aspinwall
#9-8-17
#isItATriangle.py

a = float(input('Enter Side A: '))
b = float(input('Enter Side B: '))
c = float(input('Enter Side C: '))
maximum = max(a,b,c)
minimum = min(a,b,c)
middle = (a+b+c)-(maximum+minimum)
print((minimum+middle)> maximum)

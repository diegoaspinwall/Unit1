#Diego Aspinwall
#9-6-17
#change.py

centtotal = int(input('Input number of cents: '))
quarters = centtotal//25
dimes = (centtotal - centtotal//25*25)//10
nickles = centtotal - (((centtotal - centtotal//25*25)//10*10) + (centtotal - centtotal//25*25)//5)

print(quarters, dimes, nickles)
#Diego Aspinwall
#9-8-17
#binary.py

base10test = int(input('Input base 10 number: '))
print(bin(base10test))

digfull = int(input('Enter an 8-digit binary number: '))
dig8 = (digfull%10)*2**0
dig7 = ((digfull//10)%10)*2**1
dig6 = ((digfull//100)%10)*2**2
dig5 = ((digfull//1000)%10)*2**3
dig4 = ((digfull//10000)%10)*2**4
dig3 = ((digfull//100000)%10)*2**5
dig2 = ((digfull//1000000)%10)*2**6
dig1 = ((digfull//10000000)%10)*2**7
print(dig8+dig7+dig6+dig5+dig4+dig3+dig2+dig1)

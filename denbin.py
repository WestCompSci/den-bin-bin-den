bin = input("Input a number in bin:")
den = 0
for digit in bin:
  den = den*2 + int(digit)
print("Your den number is: " + str(den))
den = int(input("Input a den number:"))
bin=""
while den>0:
  bin = str(den%2) + bin
  den = den//2
print("Your bin number is: " + bin)

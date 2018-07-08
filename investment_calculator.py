import math
print('Investment Calculator:')

p = float(input('Principle:'))
i = float(input('Rate of Interest as percentage, 7 = 0.07:'))
i = i/100
years= int(input('Duration in years:'))
a = int(input('Contributions:'))

#total = (amount *pow(1 + (roi/100), years))
total = (p+(a/i)*(math.pow((1+i),years)) - a/i) 
#interest = total - amount
print ("Total: ${:,.2f}".format(total))

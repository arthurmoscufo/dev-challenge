# Exercises for chapter 2:

# Name: Arthur C. Moscufo
print 'Exercise 2.1 (Disclaimer: I did view the hint article on Wikipedia)'
#Python is reading the zip code and translating using the octal system.
#02132 = 1114 because:
print(0*8**4+2*8**3+1*8**2+3*8**1+2*8**0)
#02492 does produce a number using the above mathematical application, 
#but 9 is outside of the acceptable 0 through 7 range (again-used hint)
print'below-not an acceptable octal representation'
print(0*8**4+2*8**3+4*8**2+9*8**1+2*8**0)

print 'Exercise 2.2'
#The below are expressions and ae legal, but there is nothing to execute so no output
5
x = 5
x + 1
#Once put into a script, the statements execute at once. "print 5" simply returns "5", x = 5 assigns a value and does not return anything, and "print x+1"
#returns the sum of the value assigned to x + 1
print 5
x = 5
print x + 1
#If each expression is modified to be a print statement we receive an error as "print x+1" is bad syntax

print 'Exercise 2.3'
width = 17
height = 12.0
delimiter = '.'
print(width/2)
print type(width/2)
print(width/2.0)
print type(width/2.0)
print(height/3)
print type(height/3)
print(1+2*5)
print type(1*2+5)
print(delimiter*5)
print type (delimiter*5)

print 'Exercise 2.4 Problem 1'
r = 5
p = 3.14159
print((4/3.0)*(p)*(r**3))

print 'Exercise 2.4 Problem 2'
cp = 24.95
print(cp*(1.00-.40)*60.00)+(3.00+(.75*59.00))

print 'Exercise 2.4 Problem 3'
print(((((6.0*60.0*60.0)+(52.00*60.0))+((8.0*60.0+15.0)*2.0)+((7.0*60.0+12.0)*3.0))/60.0)/60)
print(.50166666667*60.0)
print(.1000000002*60)
print'Answer 7:30.06'
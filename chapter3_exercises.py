# Exercises for chapter 3:

# Name: Arthur C. Moscufo

print 'Exercise 3.1'

def repeat_lyrics():
	print print_lyrics()
	print print_lyrics()

def print_lyrics():
	print "I'm a Lumberjack, and I'm okay"
	print "I sleep all night and I work all day"

print repeat_lyrics()

print "When the last line of the program 'print repeat_lyrics()' is placed at the top, the error received is:" 
print "Traceback (most recent call last)'repeat_lyrics' is not defined)"

print 'Exercise 3.2'

print "When 'print repeat_lyrics()' is placed back at the bottom and the definition of 'print_lyrics()' is moved after the definition of 'repeat_lyrics()' the output is the"
print "same as when it was when they were reversed"


print 'Exercise 3.3'

#Needed help on this solution...was ignorant to ' ' being equal to a space

print len('Allen')

def right_justify(s):
	print (' '*(70-len(s))+s)


print right_justify('allen')
	
def onehundred_space(trent):
	print (' '*100)+trent

print onehundred_space('cellar door')

print 'Exercise 3.4'

#Part 1

def do twice(f):
	print print_twice(f)
	print print_twice(f)

def print_spam(x):
	print 'spam'

#Part 2

print do_twice(print_spam,'word')

#Part 3

def print_twice(z):
	print z
	print z

print print_twice('hot dog')


def do_twice2(v):
	v()
	v()

def do_four(q):
	print do_twice(v)
	print do_twice(v)


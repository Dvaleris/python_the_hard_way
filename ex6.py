#Setting up the variables for the program below. I'm not sure why it's a
#d for the variable instead of s for string.
x = "There are %d types of people." % 10
#Showing the different ways to deal with " and '
binary = "binary"
do_not = "don't"
#Setting up a list of vars
y = "Those who know %s and those who %s." % (binary, do_not)

#Commands to prtscr the "joke"
print x
print y

#Because nothing makes a joke funnier than repetition
#I do like the use of the r here tho
print "I said: %r." % x
print "I also said: %s'." % y

#This is interesting. The var string calls a var
#But I'm not sure what the point of the % is
#Oh, it's formatting! s = string, d = signed decimal int
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Prints the joke as a complete string calling vars
print joke_evaluation % hilarious

#A different way to concat strings 
w = "This is the left side of..."
e = "a string with a right side."

print w + e

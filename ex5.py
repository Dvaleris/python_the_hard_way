name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74.0 #inches
height_in_cm = 74 * 2.54 #cm
weight = 180 #lbs
weight_in_kg = weight * 0.453592 #kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %d in centimeters" % height_in_cm
print "He's %d pounds heavy." % weight
print "That's %d in kilograms." % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d, I get %d." % (age, height, weight, age + height + weight)

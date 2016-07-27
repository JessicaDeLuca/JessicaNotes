# Learn Python The Hard Way
# http://learnpythonthehardway.org/book/

# Exercise 1
print "Begin Exercise 1" + "\n"
print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.' + "\n"

    # Hello World!
    # Hello Again
    # I like typing this.
    # This is fun.
    # Yay! Printing.
    # I'd much rather you 'not'.
    # I "said" do not touch this.

# Exercise 3
print "Begin Exercise 3"+"\n"
print "I will now count my chickens:"
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
print 25 * 3 % 4
print 25 * 3
print 75 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2, "\n"

    # I will now count my chickens:
    # Hens 30
    # Roosters 97
    # 3
    # 75
    # 3
    # Now I will count the eggs:
    # 7
    # Is it true that 3 + 2 < 5 - 7?
    # False
    # What is 3 + 2? 5
    # What is 5 - 7? -2
    # Oh, that's why it's False.
    # How about some more.
    # Is it greater? True
    # Is it greater or equal? True
    # Is it less or equal? False


# Exercise 4
print "Begin Exercise 4" + "\n"
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

    # There are 100 cars available.
    # There are only 30 drivers available.
    # There will be 70 empty cars today.
    # We can transport 120.0 people today.
    # We have 90 to carpool today.
    # We need to put about 3 in each car.

print "Hey %s there." % "you" + "\n"
    # Hey you there.

    # What do you mean by "read the file backward"?
        # Very simple. Imagine you have a file with 16 lines of code in it. Start at line 16,
        # and compare it to my file at line 16. Then do it again for 15,
        # and so on until you've read the whole file backward.

# Exercise 5
print "Begin Exercise 5" + "\n"

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "%s is really fat. He weighs %d pounds." % (my_name, my_weight)

    # Let's talk about Zed A. Shaw.
    # He's 74 inches tall.
    # He's 180 pounds heavy.
    # Actually that's not too heavy.
    # He's got Blue eyes and Brown hair.
    # His teeth are usually White depending on the coffee.
    # Zed A. Shaw is really fat. He weighs 180 pounds.
    # If I add 35, 74, and 180 I get 289.

# Format specifiers:  %s for string, %d for decimal
    # What are formatters?
    # They tell Python to take the variable on the right and put it in to replace the %s with its value.
    # I don't get it, what is a "formatter"? Huh? The problem with teaching you programming is that
    # to understand many of my descriptions you need to know how to do programming already.
    # The way I solve this is I make you do something, and then I explain it later.
    # When you run into these kinds of questions, write them down and see if I explain it later.

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight) + "\n"

# Begin Exercise 6


x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

    # There are 10 types of people.
    # Those who know binary and those who don't.

print "I said: %r." % x
    # I said: 'There are 10 types of people.'.

# Notice the stylistic choice of using single quotes and then the double quotes
# for a string with a string noted below
print "I also said: '%s'." % y
    # I also said: 'Those who know binary and those who don't.'.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
    # Isn't that joke so funny?! False

w = "This is the left side of..."
e = "a string with a right side."

    # This is the left side of...a string with a right side.

print w + e

    # What is the difference between %r and %s?
        # Use the %r for debugging, since it displays the "raw" data of the variable,
        # but the others are used for displaying to users.

    # What's the point of %s and %d when you can just use %r?
        # The %r is best for debugging, and the other formats are for actually displaying variables to users.

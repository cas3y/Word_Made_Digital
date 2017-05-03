print "Whoever leads a solitary life and yet now and then \nwants to attach himself somewhere..."  
 
## in python, strings can be single or double-quoted
print 'Does this describe you?'
 
## raw_input gets input from the user
## Here, we take the input, and *assign* it to a variable called 'ans'
ans = raw_input("'yes' or 'no'")
 
## conditionals
## see if the user's answer is interesting or not
if ans=="yes":
    print "Then the horses below will draw you down \ninto their train of wagons and tumult, \nand so at last into the human harmony!"
## elif means "else-if"
elif ans == "no":
    print "If you are in the mood of not desiring anything \nand only go to your window sill a tired man, \nwith eyes turning from the public to heaven and back again, \nnot wanting to look out and having thrown his head up a little..."
## else is a 'catch-all' for "any condition not all ready covered"
else:
    print "With changes in the time of day, the weather, the state of your business, \nand the like, you may suddenly wish to see any arm at all to which you \nmight cling - you will not be able to manage for long without a window \nlooking on to the street."
 
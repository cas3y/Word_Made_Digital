text_file = open("you_kafka.txt", "w")
text_file.write(raw_input("Hello, what is your name? "))
print "Whoever leads a solitary life and yet now and then \nwants to attach himself somewhere..."
text_file.write(" leads a solitary life and yet now and then \nwants to attach themselves somewhere...\n")
print 'Does this describe you?'
## raw_input gets input from the user
## Here, we take the input, and *assign* it to a variable called 'ans'
ans = raw_input("yes or no ")
## conditionals
## see if the user's answer is interesting or not
if ans=="yes":
    text_file.write("The horses below would draw them down \ninto their train of wagons and tumult, \nand so at last into the human harmony!")
## elif means "else-if"
elif ans == "no":
    text_file.write("They are in the mood of not desiring anything \nand only go to the window sill a tired man, \nwith eyes turning from the public to heaven and back again, \nnot wanting to look out and having thrown their head up a little...")
## else is a 'catch-all' for "any condition not all ready covered"
else:
    text_file.write("Changes in the time of day, the weather, \nthe state of business, and the like, \nthey may suddenly wish to see any arm \nat all to which they might cling - \nthey will not be able to manage for long \nwithout a window looking on to the street.")
 
text_file.close() 
print " "
print " "
print " "
text_file = open("you_kafka.txt", "r")
print text_file.read()
text_file.close()

raw_input("\n\nview file you_kafka.txt ")

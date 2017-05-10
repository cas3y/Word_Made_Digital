import random

print "You come across a wooded area. "

cc = 0

while cc < 20:
    wander_opt = ['You wander a while. ', 'You observe a vast expanse. ', 'You see something. ',  'You come across something. ', 'You come to a place. ']
    search_opt = ['You find nothing! ', 'There\'s nothing here! ', 'You think you may be walking in circles. ']
    leave_opt = ['You come across a path. ', 'Are you sure you want to leave? ', 'You try to leave. ', 'You return the way you came. ', 'You are on your way. ']
    
    x = raw_input("Do you wander, search, or leave?\n").lower()
    
    if x == "wander":
        print(random.choice(wander_opt))
        cc = cc + 2 
        
    elif x == "search":
        print(random.choice(search_opt))
        cc = cc - 2
        
    elif x == "leave":
        print(random.choice(leave_opt))
        cc = cc + 1
    else:
        print "You can wander, search, or leave. " 

print "You transcend!"

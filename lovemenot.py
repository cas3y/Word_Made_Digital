import sys

for line in sys.stdin:
    line = line.strip()
    if "you" in line:
        print "he loves me"
    else:
        print "he loves me not"
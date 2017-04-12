w = raw_input("Hello, what is your name?")
max_letter = w[0]
min_letter = w[0]
max = w.count(w[0])
min = w.count(w[0])
for c in w:
    if c is not " ":
        if w.count(c) > max:
            max_letter = c
            max = w.count(c)
        if w.count(c) < min:
            min_letter = c
            min = w.count(c)

print "He" + max_letter.lower() + "lo, Bi" + max_letter.lower() + "ches!"
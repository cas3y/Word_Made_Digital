import sys

# create an integer variable to accumulate
# word count
word_count = 0

for line in sys.stdin:
    line = line.strip()
    words = line.split(" ")
    line_word_count = len(words)
    word_count = word_count + line_word_count

# print the total number of words
print "you have", word_count, "lamborghinis in your lamborghini account"
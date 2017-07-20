# http://web.archive.org/web/20170620012442/https://learnpythonthehardway.org/book/ex49.html
#
# We need 4 tools
# 1. A way to loop through the list of scanned words. That's easy.
# 2. A way to "match" different types of tuples that we expect in our Subject Verb Object setup.
# 3. A way to "peek" at a potential tuple so we can make some decisions.
# 4. A way to "skip" things we do not care about, like stop words.
# 5. A Sentence object to put the results in.


# take in the tuple and make into a sentence

# Sentence object with 3 sub classes/ attributes - subject, verb, and object

# what can be subject - none = player (assumption) most of the time
# what can be verb - verbs + stop (generally don't care about stop)
# what can be object - nouns, directions
# TODO: how to deal with numbers?

# Our parser then has to use the functions we described and given a scanned
# sentence, convert it into a List of Sentence objects to match the input.

list in and then loop through
def parser(listoftuples):

scannedwords = [listoftuples]

for t in scannedwords:

    #start with matching and test this.

    if t has
        subject == player

    if t has
        verbs and stop == verb

    if t has
        noun and directions == object

    if t has stop
        drop it, skip



# results go in here
class Sentence(object):
    subject

    verb

    object

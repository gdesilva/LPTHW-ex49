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


# class ParserError(Exception):
#     pass
#
# class Sentence(object):
#
#     def __init__(self, subject, verb, objects):
#         self.subject
#         self.verb
#         self.objects


def parser(word_list):

    for wordtype, word in word_list:

        # if 'subject' in wordtype:
        #     drop player, append new subject

        if 'verb' in wordtype:
            print 'it\'s a verb! the word is %s' % word

        if 'noun' in wordtype:
            print 'it\'s an object! the word is %s' % word

        if 'directions' in wordtype:
            print 'it\'s a direction! the word is %s' % word

        if 'stop' in wordtype:
            pass

        # number handling

parser([('verb', 'run'), ('directions', 'north')])


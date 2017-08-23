# http://web.archive.org/web/20170620012442/https://learnpythonthehardway.org/book/ex49.html
#
# We need 4 tools
# 1. A way to loop through the list of scanned words. That's easy.
# 2. A way to "match" different types of tuples that we expect in our Subject Verb Object setup.
# 3. A way to "peek" at a potential tuple so we can make some decisions.
# 4. A way to "skip" things we do not care about, like stop words.
# 5. A Sentence object to put the results in.


# Sentence object with 3 sub classes/ attributes - subject, verb, and object

# what can be subject - none = player (assumption) most of the time
# what can be verb - verbs + stop (generally don't care about stop)
# what can be object - nouns, directions

# TODO: how to deal with numbers?

# Our parser then has to use the functions we described and given a scanned
# sentence, convert it into a List of Sentence objects to match the input.


class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, objects):
        self.subject = subject[1]
        self.verb = verb[1]
        self.objects = objects[1]



def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return none

    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")


def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)

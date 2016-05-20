"""This is the entry point of the program."""

from .languages import LANGUAGES

def score_text(list_of_words, language):
    counter = 0
    # go one at a time through each word in text
        # if that word is in the most common word list, gets +1
    for word in list_of_words:
        # if that word is in the most common word list, gets +1
        if word in language['common_words']:
            counter += 1
    return counter
    

def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""

    scores = []
    
    #Make sure inbound text is lowercase
    text = text.lower()
    #for each language appends a tuple of (score, language name)
    #Calls score_text to determine score
    for language in languages:
        scores.append((score_text(text.split(), language), language['name']))
        
    
    scores.sort()
    #return the highest sorted score-tuple at position -1, and return language name -- the 2nd tuple item
    return scores[-1][1]
      

#==================================

#def detect_language(text, languages=LANGUAGES):
#   """Returns the detected language of given text."""
    # implement your solution here
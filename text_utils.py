def count_chars(text):
    return len(text) 
    """
    Count the number of characters in a text
    """

def count_words(text): 
    return len (text.split())
    """
    Count the number of words in a text
    """

def count_sentences(text):
    return text.count('!') + text.count(".") + text.count('?')
    """
    Count the number of sentences in a text
    """

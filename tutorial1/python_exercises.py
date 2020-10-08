"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    
    """
    if (x % 2 == 0):
        return False
    else:
        return True




def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """

   
    for i in range(len(word)):
        if(word[i] == word[-1-i]):
            i+=1
        else:
            return False
        
    return True


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    oddlist = list()
    for i in range(len(numlist)):
        if(numlist[i] % 2 != 0):
            oddlist.append(numlist[i])
        i+=1
    
    return oddlist


def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    newDict = dict()
    newText = text.lower()
    words = newText.split()
    for word in words:
        if word in newDict:
            newDict[word] += 1
        else:
            newDict[word] = 1

    return newDict
    
    
    
    
    
    
    
    

    
    
  







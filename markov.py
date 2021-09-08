"""Generate Markov text from text files."""

import sys

import random as r


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_file = open(file_path).read()

    return text_file



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    words_list = text_string.split() #len42
    
    # for i in range(len(words_list) -1):
    #     loop_tup = (words_list[i], words_list[i+1])
    #     list_of_tuples.append(loop_tup)

    chains = {}

    # for i in range(len(list_of_tuples) - 2):
    #     chains[(words_list[i], words_list[i+1])] = chains.get((words_list[i], words_list[i+1]), [f"words[i+2]"]).append(words_list[i+2]) 
    
    
    for i in range(len(words_list) -2):
        loop_tup = (words_list[i], words_list[i+1])
        if chains.get(loop_tup, 0) == 0:
            chains[loop_tup] = [f"{words_list[i+2]}"]
        else:
            chains[loop_tup].append(words_list[i+2])

      

    return chains


def make_text(chains):
    """Return text from chains."""
    
    init_link = chains[("Would", "you")]
    
    words = ["Would", "you"]
    print(words)

    while True:
        try: 
            pos_1 = chains[init_link[1]] #defines first position for next link
            pos_2 = r.choice(chains[init_link]) #defines second position for next link w/ random word from initial link dictionary value
            words.append(pos_2) # Adds new word of tuple/dictionary key to words list
            next_link = chains[(pos_1, pos_2)] #sets next link to be equal to the new values
            init_link = next_link

        except KeyError:
            break

    # init_link = ("Would", "you") I FIXED IT!!!!!!
    # words = ["Would", "you"]

    # while True:
    #     try:
    #         pos_1 = init_link[1] #defines first position for next link
    #         pos_2 = r.choice(chains[init_link]) #defines second position for next link w/ random word from initial link dictionary value
    #         words.append(pos_2) # Adds new word of tuple/dictionary key to words list
    #         next_link = (pos_1, pos_2) #sets next link to be equal to the new values
    #         init_link = next_link
    #     except:
    #         break
        

    # your code goes here
    # initial link is a key(2 words) and a random word from the value
    #list [keyword1, keyword2, value_word]
    #need to find the key that is equal to (keyword2, value_word1)
    # need to add a random value word from the (kw2, vw1)

    return ' '.join(words)


input_path = f'{sys.argv[1]}'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

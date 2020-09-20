'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # TBC
    # Base case. If the length of word is 1 or 0, return 0
    if len(word) == 1 or len(word) == 0:
        return 0
    # If word starts with t and h
    if word[0] == "t" and word[1] == "h":
        # adds to the count and calls its self again
        return 1 + count_th(word[2:])
    else:
        # calls itself over the length of the array if no match found above
        return count_th(word[1:])

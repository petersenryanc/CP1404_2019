"""
CP1404 - Practical 5 - Word Occurrences
"""

word_dictionary = {}
text_input = str(input("Text: "))
words = text_input.split()

for word in words:
    num_occurrences = word_dictionary.get(word, 0)
    word_dictionary[word] = num_occurrences + 1

words = list(word_dictionary.keys())
words.sort()

max_occurrences = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_occurrences, word_dictionary[word]))

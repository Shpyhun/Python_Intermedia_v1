"""
Реализуйте модуль  word_utils.py, позволяющий:
- очистить предложение от знаков препинания;
- получить список слов из предложения;
- получить самое длинное слово в предложении;
"""


import word_utils as wu

# sentence = input("Enter a sentence: ")
sentence = 'I thought, the King had more! affected the Duke of Albany than <Cornwall>.'


print("\nA sentence without punctuation: ", wu.sentence_without_punctuation(sentence))


print("\nA list of words from a sentence: ", wu.word_list(sentence))


print("\nThe longest word in a sentence: ", wu.longest_word(sentence))

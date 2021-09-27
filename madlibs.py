#! python3
# This program is a mad libs that allows users to input their own
# entries for adjectives, nouns, verbs etc. It will print the result and then save
# that result to a text file


import os, re

# TODO Reads a text document containing a madlib
os.chdir('c:\\test')
madlib_unfilled = open('madlib.txt')
ml_str = '\n'.join(((madlib_unfilled.read()).splitlines()))
print('the madlib is:\n' + ml_str + '\n')
madlib_unfilled.close()


# TODO make a list of the occurences of adjectives, nouns, verbs, adverbs that
# appear in the madlib

word_regex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
mo_words = word_regex.findall(str(ml_str))

# TODO ask the user to input a word for each entry
i = 0
new_mo_words = []
for words in range(len(mo_words)):
    usr_input = input('please input a ' + mo_words[i] + ' for the madlib:\n\n')
    new_mo_words.append(usr_input)
    i += 1

# apply the words to the madlib 
split_sentence_list = (word_regex.sub('REPLACEME',ml_str)).split()
joined_sentence_list = str(' '.join(split_sentence_list))

items = 0
while items < len(new_mo_words):
    joined_sentence_list = joined_sentence_list.replace('REPLACEME',new_mo_words[items],1)
    items += 1

print('\nthe new madlib is:\n' + joined_sentence_list)

# TODO print madlib to new file
madlib_filled = open('madlib_filled.txt','w')
madlib_filled.write(joined_sentence_list)
madlib_filled.close()
print('Madlib file has been saved to txt file')

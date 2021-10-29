############### GET INPUT FILE ###############
infile = open("data/textin.txt","r")
textin = infile.read()
infile.close()
##############################################

corpus = textin
# corpus is just a string.

import random
ngram = {}
corpus = corpus.lower().replace('"','').replace("'",'').replace('\n','').replace(')','').replace('(','').replace('[','').replace(']','')
# .lower() is a string method that makes it all lowercase
# .replace() is a string method which replaces
     
for sentence in corpus.split('.'):
    # divide up corpus into sentences, splitting by period
    # each "sentence" is a string consisting of the corpus delimited by periods
    # this for loop iterates through the sentences in the array definded by corpus.split('.')
    for i in range(1, len(sentence.split(' '))):
        # sentence.split(' ') creates an array of words, made by splitting sentence up by space
        # this for loop iterates through the words, starting at the second word
        word_pair = (sentence.split(' ')[i - 2], sentence.split(' ')[i - 1])
        # round parenthesis define a tuple as opposed to a list, which means 
        # the values cannot be re-assigned
        # this tuple is as per its name a pair of words in sequence, which will get reassgined each time

        if '' in word_pair:
            #tests for one of the word pair to be empty
            continue

        if (word_pair) not in ngram:
            #tests to see if one of the two elements of the list word_pair
            ngram[word_pair] = []
        ngram[word_pair].append(sentence.split(' ')[i])
    
word_pair = random.choice(list(ngram.keys())) 
# convert ngram.keys() to a list. each list element is a tuple, choose one at random...

out = word_pair[0] + ' ' + word_pair[1] + ' '
# start making the output string by concatenating the two words in the first word pair

while True:
    if word_pair not in ngram.keys():
        break  # only do this as long as a word pair is in the corpus
    third = random.choice(list(ngram[word_pair]))
    # choose a third word at random from the list of third words found in the text
    out += third + ' '
    # add it to the output string
    word_pair = (word_pair[1], third)
    # make a new word pair out of the second word followed by the third word, which will be used on the 
    # next round of the while loop as long as the new pair exists in the dict ngram

    
#print ('output banter: \n', out)
textout = out

######### SAVE NGRAM FILE  ###### 
file = open("data/ngram.txt", "w")
file.write(str(ngram)) # conver dict to string with str()
file.close()

######### SAVE OUTPUT FILE  ###### 
file = open("data/textout.txt", "w")
file.write(textout)
file.close()


'''
structures.py

Simple functions performing operations on basic Python data structures.

The code here was completed by Kevin Li on October 24 2019.
'''
# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    return the_list[0] + the_list[-1]

#COMPLETED

# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
     if beginning<end:
         the_list = the_list[beginning+1:end]
         return the_list[::-1]
     else: 
         raise ValueError

    #the_list.reverse

# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
     the_list.insert(index,the_list[index])
     the_list.insert(index,the_list[index])
     print(the_list)

#COMPLETE 

# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    word = word.lower()
    wordreverse= word[::-1]
    if wordreverse==word:
         print("It's a palindrome.")
    else:
         print('It is not a palindrome')

     #COMPLETE

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    import string as str
    for i in range(len(str.punctuation)):
        punctuation = (str.punctuation[i])
        sentence = sentence.replace(punctuation,'')
    sentence = sentence.replace(' ','')
    sentence = sentence.lower()
    sentencereverse = sentence[::-1]
    if sentencereverse == sentence:
        print ("It's a palindrome.")
    else:
        print('It is not a palindrome')

#COMPLETED

     #import string as str
    #sentence=sentence.replace(' ','')
    #' ','') #used .strip initially. However, only removes trailing and end spaces.
    #sentence=sennce.replace(',','')
    #sentence=sentence.replace('?','')
    #sentence=sentence.replace('!','')
    #sentence=sentence.lower()
    #sentencereverse=sentence[::-1]
    

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 

#Main Function
def concatenate_sentences(sentence1, sentence2):
    if is_lowercase(sentence1)==True:
        if is_lowercase(sentence2)==True:
            print (sentence1 + ' '+ sentence2)
        else: 
            return
    else:
        return


def is_lowercase(sentence):
     punctuation={'.','!','?'}
     if not sentence[0].isupper() and sentence[-1] not in punctuation:
         print('One of your sentence does not begin with a capital letter and has no punctuation at the end.')
     elif not sentence[0].isupper() and sentence[-1] in punctuation:
         print('One of your sentence does not start with a capital letter.')
     elif sentence[0].isupper() and sentence[-1] not in punctuation: 
         print('One of your sentence does not end with any punctuation.')
     else:
         return True

#COMPLETED



# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary.keys():
        return True
    else:
        return False

dictionary={'fun':'','happy':''}

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False

dictionary1={'fun':'2','happy':'4'}


# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    newdictionary= dict(**dictionary1,**dictionary2)
    return (newdictionary)

if __name__=='_main_':
     main()

def main():
     #list1=[0,1,2,3,4]
     #list2=[23,45,67,1,67,4,67,87]
     #print(first_and_last(list1))
     #concatenate_sentences('My name is Kevin.','i like to swim')
     # not verified part_reverse(list2, 0, 6)
     #repeat_at_index(list1, 1)
     #palindrome_word('WOW')
     #palindrome_sentence('      Hi, ! ?      My, Ym   , ih ')
     dict1={'Hello':1,'My Name':3}
     dict2={'Thank you':4}
     merge_dictionaries(dict1, dict2)



main()
#English to pig Latin
print('Enter the English message to translate into Pig Latin')
message = input()
VOWELS = ('a','e','i','o','u','y')
pigLatin= []# a list of the words in Pig Latin

for word in message.split(): #split() method is called on a string and returns a list
    #separate the non-letters at the start of this word
    prefixNonLetters = ''

    while len(word) > 0 and not word[0].isalpha(): #isalpha() method returns true if only letters and not blank
        prefixNonLetters += word[0] #makes the prefixNonLetters into the first letter of word
        word = word[1:] # Changes the word from the word into the word except for the first letter

    if len(word) == 0:
        pigLatin.append(prefixNonLetters) #appends the first letter to the end of the word
        continue

    #Separate the non-letters at the end of this word
    suffixNonLetters = ''
    while not word[-1].isalpha(): #isalpha returns true if only letters and not blank
        suffixNonLetters += word[-1] # append the last letter of the word to the suffixNonLetters
        word = word[:-1] #word is now equal to the 0 to 1 minus letter not including last letter
    #Remember if the word was in uppercase or title case.
    wasUpper = word.isupper() 
    wasTitle = word.istitle()

    word = word.lower() # make hte word lowercase for translation
    #separate the consonatnts at the start of the word
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    #add the pig lating ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    #Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    #Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
#Join all the words back to gether into a single string
print(' '.join(pigLatin))
    
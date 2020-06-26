'''
Phone and Email Extractor
ABSWP CH 7
Racz 06/09/2020

Code should 
    1. Get the text off the clipboard
    2. Find all phone numbers and email addresses in the text.
    3. Paste onto the clipboard
'''
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? #Area code(if included because ?)
    (\s|-|\.)?         #Separator
    (\d{3})            #First 3 Digits
    (\s|-|\.)          #Separator
    (\d{4})            #Last 4 Digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #Extension
    )''', re.VERBOSE)


#TODO: Create Email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ #Username
    @                 #@ symbol
    [a-zA-Z0-9.-]+    #Domain Name
    (\.[a-zA-Z]{2,4}) #Dot-something
    )''',re.VERBOSE)


#TODO: Find matches in clipboard text.

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] !='':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groupa in emailRegex.findall(text):
    matches.append(groupa[0])

#TODO: Copy results to the clipboard.

if len(matches) >0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')
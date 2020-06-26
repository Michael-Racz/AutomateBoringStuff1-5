# Automate The Boring Stuff Chapter 1-5
This contains files that I was making or using to learn while reading Automate the Boring Stuff With Python: Second Edition. Files have simple headers with date and some description about the chapter and some simple comments. Below are some comments for each of the files for ease of access.

## Motivation 
These projects might be simple but were some of the first projects I have made in Python. 

## Features/Description
*Some of these may be listed out of alpha order because I feel that they are more significant or are worth seeing first.

#### birthdays.py
   A simple test of the use of a dictionary in Python. This program will prompt the user for an input and a birthday. If the name is in the dictionary(stored as a key) then the program will print out the name of the person entered and their birthday(stored as the key's value).
If the entered name is not in the dictionary, then it will ask for their birthday and store it.

#### chessDictionaryValidator.py


#### fantasyGameInventory.py
This is a use of a dictionary. There is no input required. The program will run and take the current inventory and then update after a set of items in a list is added.

#### mclip.py
This program works with the clipboard via pyperclip. It would be used in the case of someone responding to emails with the same message and hoping to shorten their tasks. It can be used to make a running script to run at the command line. Depending on the command used with the specific key's in the dictionary, it would find the value and copy to the clipboard.

#### phoneAndEmail.py
A test in regular expressions. This program first gets the text off of the clipboard, then scans all the text for emails and phone numbers. Once it has found any of these, it will copy the matches to the clipboard. It also will let the user know in the output on screen which numbers and emails have been found/copied.

#### pigLat.py
This program was a good use of methods of strings. It prompt's the user to enter a message in English for translation to Pig Latin. Once entered the program will separate words and add the appropriate suffixes. After translating, prints the message to screen.

#### zombieDice.py
A program to give a glimpse into AI and game theory. This program uses a class which is a zombie. Different instances of this zombie have different functions to simulate which actions a zombie will take on their turn. With the imported library 'zombiedice', the program opens a tab in a browser to simulate any number of games. Instances of zombies made have different strategies on each of their turns. Once finished running, the website opened will display the wins and ties from the simulation. The program will then output the tournament results to the screen.

#### board.py 
Test of printing and use of a dictionary in the form of a tic-tac-toe game. The program prompts the user for an input 9 times and places the user's choice(X or O) on the board.
Current issues: Game currently doesn't recognize when someone has won/lost game. Also doesn't recognize when there is already a space filled with a previous selection.

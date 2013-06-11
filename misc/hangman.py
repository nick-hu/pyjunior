#!/usr/bin/python

import random, string, wordbank

word = [l for l in random.choice(wordbank.words)]

print 'Welcome to Hangman!\n'
ch = int(raw_input('Enter number of chances: '))
display = ['-' for l in word]
guessed = []

while ch > 0:
    print '\n', ''.join(display), '\nChances left:', ch
    print 'Guessed:', ','.join(guessed)
    let = string.upper(raw_input('\nLetter to guess (type end to solve): '))

    if let == 'END':
        solve = string.upper(raw_input('Enter solution to guess: '))
        if solve == ''.join(word):
            display = word
            break
        print 'Incorrect guess!'
        ch = ch-1
    
    else: 
        if let not in string.ascii_uppercase:
            print 'Error: Guess must be one letter only!'
            continue     
        if let in guessed:
            print 'Error: That letter has already been guessed!'
            continue
        if let not in word:
            print 'That letter is not in the word!'
            guessed.append(let)
            ch = ch-1
        else:
            for l in range(len(word)):
                if word[l] == let: display[l] = let
            guessed.append(let)
            if '-' not in display: break

if '-' not in display:
    print '\n', ''.join(display), '\nCongratulations! You win!'
else: print '\nSorry, you lose! The word was:', ''.join(word)

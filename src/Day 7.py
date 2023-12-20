# Hangman
import random
CHANCES = 5
WORD = 'TRAINING'

def check_the_guess(guess:str, correct_guess, word):
    for w in word_guess:
        
        if guess == word[w] and w not in correct_guess:
            correct_guess.append(w)
            return True
    
    return False

while True:
    word = WORD
    chances = CHANCES
    chance_to_play = chances + 2
    words_to_guess = []
    for i in range(0, chances):
        guess = random.randint(0, len(word)-1)
        while guess in words_to_guess:
            guess = random.randint(0, len(word)-1)
        words_to_guess.append(guess)


    words_to_show = [i for i in range(0, len(word)) if i not in words_to_guess]


    word_guess = words_to_guess
    correct_guess = []
    score = 0
    for i in range(0,  chance_to_play):
        current_word = [word[a]  for a in range(len(word))]
        
        for j in words_to_guess:
            current_word[j] = "_" if j not in correct_guess else word[j]
        print(f"word: {current_word}")
        guess = str(input("Enter Your Guess:- "))
        result = check_the_guess(guess, correct_guess, word)
        if result :
            score += 1
            print(f"Successfully guessed, current Score: {score}")
            
        else:
            print(f"Incorrect guess, current Score: {score} chance Used: {i+1}")
    
        if score == chances:
            print(("Congratulations you have successfully guessed all the words"))
            break
    else:
        print((f"Sorry, you have failed to guess all the words, score: {score}.. Want to try again."))
        
    continu = input("Continue/ Exit: Enter E/C")
    
    if continu == 'E':
        break 
       
    
    
    
    
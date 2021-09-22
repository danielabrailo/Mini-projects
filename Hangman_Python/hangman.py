import json, random

with open('words.json', 'r') as file_obj:
    words = json.load(file_obj)

words = words['data']
word = random.choice(words)
stars_word = list("*" * len(word))
wrong_guess = 0

while wrong_guess < 5:
    print(f"Word to guess is: {''.join(stars_word)}")
    letter = input(f"Choose a letter (So far you have used {wrong_guess} chances): ")
    letter = letter.lower()
    index = word.find(letter)  # will return the index of the letter
    if index != -1:
        if stars_word[index] != "*":
            index = word[index + 1:].find(letter)
        stars_word[index] = letter
        print("Correct!")
        print(''.join(stars_word))
        if ''.join(stars_word) == word:
            print("You win!")
            break
    else:
        print("Wrong guess")
        wrong_guess += 1
else:
    print(f"You already used your 5 chances! You lose. The word was {word}")

print("Game over!")

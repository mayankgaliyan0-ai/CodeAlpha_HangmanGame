import random

word_list = ["apple", "mango", "banana", "grape", "orange"]
word = random.choice(word_list)

letters = []
chance = 6

print("====== HANGMAN GAME ======")

while chance > 0:

    show = ""

    for i in word:
        if i in letters:
            show += i + " "
        else:
            show += "_ "

    print("\nWord :", show)

    if "_" not in show:
        print("🎉 You guessed the word correctly!")
        break

    guess = input("Enter one letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in letters:
        print("You already entered this letter.")
        continue

    letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        chance -= 1
        print("Wrong Guess!")
        print("Remaining Chances:", chance)

if chance == 0:
    print("\nGame Over!")
    print("Correct Word was:", word)
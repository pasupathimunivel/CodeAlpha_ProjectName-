import random

word_list = ["apple", "pizza", "tiger", "house", "plant"]
secret_word = random.choice(word_list)
guessed_word = ["_"] * len(secret_word)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")


while incorrect_guesses < max_incorrect and "_" in guessed_word:
    print("Current word:", " ".join(guessed_word))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()


    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("❗ You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Incorrect! You have {max_incorrect - incorrect_guesses} tries left.\n")

if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Out of guesses! The word was:", secret_word)

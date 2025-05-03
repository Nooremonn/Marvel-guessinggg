import random

marvel_words = [
    "ironman", "thor", "loki", "avengers", "spiderman", "wakanda",
    "thanos", "hulk", "blackwidow", "shield", 
    "asgard", "xmen", "multiverse", "hydra", 
    "sokovia", "ravagers", "midgard"
]

secret_word = random.choice(marvel_words)
guessed_letters = []

# Reveal one random letter as a lil hint
hint_letter = random.choice(secret_word)
guessed_letters.append(hint_letter)

tries = 6  
lives_word = list("MARVEL")

print("DA *ULTIMATE* Marvel Guessing Game 💥")
print(f"You’ve got {tries} chances to slay this game. Don’t be lame.")

while tries > 0:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print("\n Word so far:", display_word)

    if display_word == secret_word:
        print(" YASSS kweeen you ate that up. The word was:", secret_word.upper())
        break

    print("❤️ Lives left:", "".join(lives_word))
    guess = input(" Drop a guess: ").lower()

    if guess in guessed_letters:
        print(" Ugh, you already said that one. Try harder.")
    elif guess in secret_word:
        guessed_letters.append(guess)
        print("💅 Periodt. That was a good one!")
    else:
        guessed_letters.append(guess)
        tries -= 1
        removed = lives_word.pop(0)
        print(f" Nope. '{removed}' yeeted. You have {tries} tries left. Be fr pls.")

if tries == 0:
    print(f"\nGame over, The word was: '{secret_word.upper()}'. Skill issue tbh.")

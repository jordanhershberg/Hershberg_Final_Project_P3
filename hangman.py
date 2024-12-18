def create_hangman(wrong_guesses):
  hangman_parts = [
    ["head", "neck", "torso", "left arm", "right arm", "left leg", "right leg", "left sonic screwdriver", "right sonic screwdriver"],
    ["head", "neck", "torso", "left arm", "right arm", "left leg", "right leg", "left sonic screwdriver"],
    ["head", "neck", "torso", "left arm", "right arm", "left leg", "right leg"],
    ["head", "neck", "torso", "left arm", "right arm", "left leg"],
    ["head", "neck", "torso", "left arm", "right arm"],
    ["head", "neck", "torso", "left arm"],
    ["head", "neck", "torso"],
    ["head", "neck"],
    ["head"]
  ]
  return hangman_parts[wrong_guesses]






def play_hangman():
  word = input("enter a word for the player to guess: \n ")
  print("\033[H\033[J", end="")
  word_letters = set(word)
  alphabet = set(chr(i) for i in range(97, 123))
  used_letters = set()
  lives = 9

  while len(word_letters) > 0 and lives > 0:
    print("you have " + str(lives) + " lives left.")
    print("you have used these letters: " + ",".join(used_letters))

    word_list = [letter if letter in used_letters else '_' for letter in word]
    print('current word: ', ' '.join(word_list))
    user_letter = input('guess a letter: \n ')
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
        print('')
      else:
        lives = lives-1
        print("Letter is not in word." + str(create_hangman(lives)))
    elif user_letter in used_letters:
      print("you already used that character, try again :/")
    else:
      print("invalid character, only use individual letters, lowercase, no spaces")

  if lives == 0:
    print('hangman got hanged :( the word was ' + word)
  else:
    print('you guessed right, the word was ' + word)
play_hangman()
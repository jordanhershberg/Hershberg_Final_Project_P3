def create_hangman(wrong_guesses):
  """
  Creates the hangman graphic based on wrong guesses.
  Args:
    wrong_guesses: Number of incorrect guesses.
  Returns:
    A list representing the hangman graphic.
  """
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
  """
  Plays the hangman game.
  """
  word = input("Enter a word for the player to guess: ")
  print("\033[H\033[J", end="")
  word_letters = set(word)
  alphabet = set(chr(i) for i in range(97, 123))
  used_letters = set()
  lives = 9
  # Get user input
  while len(word_letters) > 0 and lives > 0:
    print(f"You have {lives} lives left.")
    print(f"You have used these letters: {' '.join(used_letters)}")
    # Current word (ie W - R D)
    word_list = [letter if letter in used_letters else '_' for letter in word]
    print('Current word: ', ' '.join(word_list))
    user_letter = input('Guess a letter: ').lower()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
        print('')
      else:
        lives -= 1  # Takes away a life if wrong
        print(f'Letter is not in word. {create_hangman(lives)}')
    elif user_letter in used_letters:
      print('You have already used that character. Please try again.')
    else:
      print('Invalid character. Please try again.')
  # Gets here when len(word_letters) == 0 OR lives == 0
  if lives == 0:
    print(f'You died, sorry. The word was {word}')
  else:
    print(f'YAY! You guessed the word {word}!!')
play_hangman()
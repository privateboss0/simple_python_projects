secret_phrase = "Kindness Wealth"
guess = ""
guess_count = 0
guess_limit = 10
out_of_guesses = False

while guess != secret_phrase and not (out_of_guesses):
    if guess_count <= guess_limit:
        guess = input("Enter a Guess Phase: ")
        guess_count = guess_count + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print ("Out of Yin guessess... Yang Program!!")
else:
    print ("WINNER!!")
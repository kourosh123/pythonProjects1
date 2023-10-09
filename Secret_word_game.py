Secret_word = "Zebra"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != Secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("write your guess : ")
        guess_count += 1
    else:
        out_of_guesses = True

if guess_count >= guess_limit:
    print("You Lose! Out of guesses")
else:
    print("You win!")
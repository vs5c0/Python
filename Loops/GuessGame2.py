Secret_Word = "Ram"
guess = " "
guess_count = 0
guess_limit = 5
out_of_guess = False
while guess != Secret_Word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter the Guess Word: ")
        guess_count+=1
    else:
        out_of_guess = True

if out_of_guess:
    print("You Lose !")
else:
    print("You Win! ")

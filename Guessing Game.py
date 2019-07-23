secret_number=7
guess_limit=2
guess_count=0
while guess_count<=guess_limit:
    guess=int(input("What is the secret number: "))
    guess_count=guess_count+1
    if guess==secret_number:
        print("You have guessed it corrcet, You Won")
        break
else:
    print("Sorry You lost")
    
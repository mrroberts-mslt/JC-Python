arrived = False
km = 0
while arrived == False and count < 100:
    print("Are we there yet?")
    km +=1
print("You have arrived!")


password = "1234"
password_guess = ""

while password_guess != password:
    print("Please enter your password: ")
    password_guess = input()

print("What is capital of Canada ?" )
answer = "Ottawa"
guess = input()

while guess != answer:
    print("Incorrect answer")
    guess = input()
print("correct!!")


score = 0
print("What is capital of Canada ?" )
answer = "Ottawa"
guess = input("Answer: ")

while guess != answer:
    print("Incorrect answer")
    guess = input("Try again: ")
print("correct!!")
score +=1

print("What is capital of UK ?" )
answer = "London"
guess = input("Answer: ")

while guess != answer:
    print("Incorrect answer")
    guess = input("Try again: ")
print("correct!!")
score +=1

print("Your score: ", score)

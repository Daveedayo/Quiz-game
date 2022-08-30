print("Welcome to my computer quiz")

get_started = input("Do you wanna play my game? ")

if get_started != "yes":
    quit()

print("Okay let's play it!")

question1 = input("What does CPU stand for? ")

if question1 == "central processing unit":
    print("Correct")
else:
    print("Incorrect")
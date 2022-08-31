print("Welcome to my computer quiz")

get_started = input("Do you wanna play my game? ").lower()

if get_started != "yes":
    quit()

print("Okay let's play it!")
score = 0

question1 = input("What does CPU stand for? ").lower()

if question1 == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question2 = input("What does RAM stand for? ").lower()

if question2 == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")

question3 = input("What does ROM stand for? ").lower()

if question3 == "read only memory":
    print("Correct!")
else:
    print("Incorrect!")

question4 = input("What does GPU stand for? ").lower()

if question4 == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")

if score == 1:
    print("You got " + str(score) + " question correctly")
else:
    print("You got " + str(score) + " questions correctly")        
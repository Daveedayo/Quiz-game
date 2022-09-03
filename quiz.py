import json

questions_json = json.load(open("questions.json"))
questions = questions_json["questions"]


print("Welcome to my computer quiz")

get_started = input("Do you wanna play my game? ").lower()

if get_started != "yes":
    quit()

print("Okay let's play it!")
score = 0

for q in questions:
    question = input(q["question"]).lower()
    if question == q["ans"].lower():
        score +=1
        print('Correct')
    else:
        print("Incorect")

print(f"You have scored {score} marks out of {len(questions)} questions")

print(f"You got {(score/len(questions)) * 100}% ")
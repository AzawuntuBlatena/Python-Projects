
print("well come to my computer quiz")

playing = input("do you want to play")

if playing.lower() != "yes":
    quit()

print("oky lets play :)")
score = 0

answer = input("what does cpu stand for ").lower()
if answer == "central processing unit":
    print("correct")
    score += 1

else:
    print("incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

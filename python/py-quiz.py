print("welcome to my computer quiz!")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay! Let's play :)")
score = 0

answer = input("QUESTION 1 - what does CPU stands for? ANSWER - ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect!")
    
answer = input("QUESTION 2 - what does GPU stands for? ANSWER - ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect!")

answer = input("QUESTION 3 - what does ram stands for? ANSWER - ")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print("incorrect!")

answer = input("QUESTION 4 - what does PSU stands for? ANSWER - ")
if answer.lower() == "power supply unit":
    print('correct!')
    score += 1
else:
    print("incorrect!")

print("you got " + str(score) + " question correct!")

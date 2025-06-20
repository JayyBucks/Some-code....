import random

def getLevel():
    while True:
        try:
            gameLevel = int(input("Choose Level (1, 2, 3): "))
            if gameLevel not in [1, 2, 3]:
                print("Error: Invalid input!")
                continue
            else:
                break
        except:
            print("Error: Invalid input!")
            continue
    return gameLevel
        
def getQuestionNum():
    while True:
        try:
            questionAmount = int(input("How many questions? (3-10): "))
            if questionAmount not in [3,4,5,6,7,8,9,10]:
                print("Error: Invalid question amount!")
                continue
            else:
                break
        except:
            print("Error: Invalid question amount!")
            continue
    return questionAmount

def main():
    correctAnswers = 0
    userAttempts = 0
    gameLevel = getLevel()
    questionAmount = getQuestionNum()
    
    for _ in range(questionAmount):
        if gameLevel == 1:
            random1 = random.randint(0, 9)
            random2 = random.randint(0, 9)
        elif gameLevel == 2:
            random1 = random.randint(10, 99)
            random2 = random.randint(10, 99)
        elif gameLevel == 3:
            random1 = random.randint(100, 999)
            random2 = random.randint(100, 999)
        answer = random1 + random2

        userAttempts = 0
        while True:
            try:
                user_answer = int(input(f"\n{random1} + {random2} = "))
            except:
                print("INCORRECT!\n")
                userAttempts+=1
                if userAttempts == 3:
                    print(f"{random1} + {random2} = {answer}")
                    break
                continue
            
            if answer == user_answer:
                print("CORRECT!\n")
                correctAnswers+=1
                break
            else: 
                print("INCORRECT!\n")
                userAttempts+=1
                if userAttempts == 3:
                    print(f"{random1} + {random2} = {answer}")
                    break
                continue
    percentage = correctAnswers/questionAmount
    percentage = percentage * 100
    print(f"Questions Correct: {correctAnswers}/{questionAmount} or {percentage:.2f}%!")
    
main()
Score=0
Questions={"What's the capital of Frence?":{"Options":["Paris","Berlin","Madrid","Rome"],"correct":"Paris"},
           "Which planet is known as the Red Planet?":{"Options":["Mars","Venus","Jupiter","Saturn"],"correct":"Mars"},
           "What is the largest ocean on earth?":{"Options":["Pacific Ocean","Atlantic Ocean","Indian Ocean","Arctic Ocean"],"correct":"Pacific Ocean"},}
for i,j in Questions.items():
    print(i)
    Num=1
    for h in j["Options"]:
        print("{}.{}".format(Num,h))
        Num+=1
    while True:
        user_input=int(input("Answer: "))
        if user_input>0 and user_input<=len(j["Options"]):
            user_input = j["Options"][user_input - 1]
            break
        else:
            print("You entered an invalid number")
    if user_input == j["correct"]:
        print("You're answer is correct!")
        Score += 1
    else:
        print("You're answer is wrong!")
print("You got {} out of {} correct!".format(Score,len(Questions)))
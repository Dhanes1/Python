def Step_1():
    f=open("Believer.txt", "r")
    data=f.read()
    print(data)
    print()
    print("Information: ")
    print("Total characters: "+str(len(data)))
    w=data.split()
    print("Total words: "+str(len(w)))
    upper_case_words=[]
    lower_case_words=[]
    for i in w:
        if i[0].isupper():
            upper_case_words.append(i)
        else:
            lower_case_words.append(i)
    print("Upper case words: "+str(len(upper_case_words)))
    print("Lower case words: "+str(len(lower_case_words)))
    f.close()
def line_count():
    num=0
    f = open("Believer.txt", "r")
    column=f.readlines()
    for i in column:
        if i != "\n":
            num+=1
    print("Total lines: "+str(num))
    f.close()
def find_word():
    f = open("Believer.txt", "r")
    print()
    print("Choices: ")
    while True:
        print("""1. Find
2. Exit""")
        print()
        Choice=int(input("Choice: "))
        if Choice==2:
            break
        elif Choice==1:
            user_input=" "+input("What word do you want to find: ")+" "
            all_lines=f.readlines()

            for i in all_lines:
                if user_input in i:
                    print(i)
        else:
            print("You enter it wrong!")
            print("Program will end now!")

























Step_1()
line_count()
find_word()
text=input("Insert text: ")
text_length=len(text)
for i in range(text_length):
    print("  "*((text_length-1)-i),end="")
    for q in range(i+1):
        print(text[q],end=" ")
    print("")
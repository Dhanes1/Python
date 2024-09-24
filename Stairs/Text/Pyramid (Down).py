text=input("Insert text: ")
text_length=len(text)

for i in range(text_length):
    x=text[i]+" "
    print(x*(i+1))
import os
current_directory = os.getcwd()
print("""
Choices: 
1. Open file
2. Create new file
3. Delete file
4. Edit file
5. Quit""")
while True:
    print()
    print("Files: ")
    all_files=os.listdir(current_directory)
    txt_files=[]
    txt_files=[file for file in all_files if file.endswith('.txt')]
    num=1
    for file in txt_files:
        print(num,".",file)
        num+=1
    choice=int(input("Enter your choice (1-5): "))
    if choice == 5:
        print("Goodbye")
        break
    if choice == 1:
        file_num=int(input("Enter the number of the file to open: "))
        selected_file=txt_files[file_num - 1]
        txt_data=open(selected_file,"r")
        datatobeprint=txt_data.readlines()
        for i in datatobeprint:
            print(i)
    if choice == 2:
        new_file_name=input("Enter the name of the new file: ")
        f=open(new_file_name+".txt",'w')
        f.close()
        print("File", new_file_name,"created.")
        
    if choice == 3:
        file_num = int(input("Enter the number of the file to delete: "))
        if 1 <= file_num <= len(txt_files):
            selected_file = txt_files[file_num-1]
            os.remove(selected_file)
            print("File",selected_file,"is deleted.")

    if choice == 4:
        file_num = int(input("Enter the number of the file to edit: "))
        if 1 <= file_num <= len(txt_files):
            selected_file = txt_files[file_num-1]
            new_content = input("Enter new content for the file: ")

            f=open(selected_file, 'a')
            f.write(new_content)
            f.close()
            print("Content added to",selected_file,".")

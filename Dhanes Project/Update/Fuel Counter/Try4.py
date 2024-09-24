import os
from tkinter import *
from tkinter import ttk
folder_path = "C:\\Users\\Dhanes\\Documents\\App Data\\Visual Code\\Dhanes Project\\Fuel Counter\\Data"  
txt_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]
temp1=""
win = Tk()
win.title("Fuel Calculator")
win.geometry("600x400")
add=False
delete=False
count=False
avg=False
def add_car_btn_clk():
    global add, name_of_car_entry, car_name_lbl, fuel_type_lbl, fuel_type_cb,submit_btn
    
    
    car_name_lbl = Label(win, text="Car Name: ")
    car_name_lbl.place(x=150, y=20)
    name_of_car_entry = Entry(win, width=30)
    name_of_car_entry.place(x=280, y=20)

    fuel_type_lbl = Label(win, text="Fuel Type: ")
    fuel_type_lbl.place(x=150, y=60)
    fuel_type_clk = StringVar()
    fuel_type_cb = ttk.Combobox(win, textvariable=fuel_type_clk, values=['Electric', 'Gasoline'])
    fuel_type_cb.place(x=280, y=60)

    submit_btn = Button(win, text="Submit", command=lambda: submit_btn_car_clk(name_of_car_entry, fuel_type_clk))
    submit_btn.place(x=150, y=100)
    add_car_btn.config(state=DISABLED)
    delete_car_btn.config(state=NORMAL)
    counter_btn.config(state=NORMAL)
    average_btn.config(state=NORMAL)
    destroy_all()
    add=True
def submit_btn_car_clk(name_entry, fuel_type_clk):
    car_name = name_entry.get()
    fuel_type = fuel_type_clk.get()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_name = "Data"
    folder_path = os.path.join(current_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, car_name + ".txt")

    notification_lbl.config(text="")
    if os.path.exists(file_path):
        notification_lbl.config(text=f"Car {car_name} already exists!", fg="red")
        win.after(3000, clear_notification)
        return

    with open(file_path, 'w') as file:
        file.write(f"{fuel_type}")
def submit_btn_delete_clk():
    global file_num, txt_files, temp1
    file_num = num_car_cb.current()
    if 0 <= file_num < len(txt_files):
        selected_file = txt_files[file_num-1]
        os.remove(selected_file)
        print("File", selected_file, "is deleted.")
        
        # Update the list of files after deletion
        folder_path = "C:\\Users\\Dhanes\\Documents\\App Data\\Visual Code\\Dhanes Project\\Fuel Counter\\Data"
        txt_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]
        temp1=[]
        for i in txt_files:
            temp11 = i.replace("C:\\Users\\Dhanes\\Documents\\App Data\\Visual Code\\Dhanes Project\\Fuel Counter\\Data\\","")
            temp111 = temp11.replace(".txt","")
            temp1.append(temp111)
        
        # Update the ComboBox with the new list of files
        num_car_cb['values'] = temp1
        num_car_cb.current(0)  # Select the first item by default
    else:
        print("Invalid selection")
def clear_notification():
    notification_lbl.config(text="")
def delete_car_btn_clk():
    global delete,num_car_cb,num_car_cb,delete_car_lbl,submit_btn1
    delete_car_lbl=Label(win,text="Delete Car: ")
    delete_car_lbl.place(x=150,y=20)
    temp1=[]
    for i in txt_files:
        temp11 = i.replace("C:\\Users\\Dhanes\\Documents\\App Data\\Visual Code\\Dhanes Project\\Fuel Counter\\Data\\","")
        temp111 = temp11.replace(".txt","")
        temp1.append(temp111)
    num_car_clk=StringVar()
    num_car_cb=ttk.Combobox(win,textvariable=num_car_clk,values=temp1)
    num_car_cb.place(x=280,y=20)
    submit_btn1=Button(win,text="Submit",command=submit_btn_delete_clk)
    submit_btn1.place(x=150,y=60)
    add_car_btn.config(state=NORMAL)
    delete_car_btn.config(state=DISABLED)
    counter_btn.config(state=NORMAL)
    average_btn.config(state=NORMAL)
    destroy_all()
    delete=True
def counter_btn_clk():
    pass
def average_btn_clk():
    pass
def destroy_all():
    global add,delete,count,avg
    if add:
        car_name_lbl.destroy()
        name_of_car_entry.destroy()
        fuel_type_lbl.destroy()
        fuel_type_cb.destroy()
        submit_btn.destroy()
        add=False
    if delete:
        delete_car_lbl.destroy()
        num_car_cb.destroy()
        submit_btn1.destroy()
        delete=False


add_car_btn = Button(win, text="Add Car", command=add_car_btn_clk)
add_car_btn.place(x=20, y=20)

delete_car_btn = Button(win, text="Delete Car", command=delete_car_btn_clk)
delete_car_btn.place(x=20, y=60)

counter_btn = Button(win, text="Counter", command=counter_btn_clk)
counter_btn.place(x=20, y=100)

average_btn = Button(win, text="Average", command=average_btn_clk)
average_btn.place(x=20, y=140)

notification_lbl = Label(win, text="", fg="red")
notification_lbl.place(x=150, y=140)

win.mainloop()

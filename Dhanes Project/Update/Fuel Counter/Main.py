import os
from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Fuel Calculator")
win.geometry("600x400")
add = False
delete = False
counter = False
average = False
inf_data_lbl = None  # Define inf_data_lbl globally
inf_data = None  # Define inf_data globally

def add_car_btn_clk():
    global add, delete, inf_data_lbl, inf_data, name_of_car_entry
    add = True
    if delete:
        if inf_data_lbl:
            inf_data_lbl.destroy()
        if inf_data:
            inf_data.destroy()
    car_name_lbl = Label(win, text="Car Name: ")
    car_name_lbl.place(x=150, y=20)
    name_of_car_entry = Entry(win, width=30)
    name_of_car_entry.place(x=280, y=20)
    fuel_type_lbl = Label(win, text="Fuel Type: ")
    fuel_type_lbl.place(x=150, y=60)
    fuel_type_clk = StringVar()
    fuel_type_cb = ttk.Combobox(win, textvariable=fuel_type_clk, values=['Electric', 'Gasoline'])
    fuel_type_cb.place(x=280, y=60)

    submit_btn = Button(win, text="Submit", command=lambda: submit_btn_clk(name_of_car_entry, fuel_type_clk))
    submit_btn.place(x=150, y=100)

def submit_btn_clk(name_entry, fuel_type_clk):
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

def clear_notification():
    notification_lbl.config(text="")

def delete_car_btn_clk():
    global delete, inf_data_lbl, inf_data, add, name_of_car_entry
    delete = True
    if inf_data_lbl:
        inf_data_lbl.destroy()
    if inf_data:
        inf_data.destroy()
    inf_data_lbl = Label(win, text="Directory: ")
    inf_data_lbl.place(x=150, y=20)
    inf_data = Text(win, height=7, width=50, bg="light yellow")
    inf_data.place(x=150, y=40)

def counter_btn_clk():
    pass

def average_btn_clk():
    pass

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

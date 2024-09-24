import os
import tkinter as tk
from tkinter import ttk

# Function to add a car
def add_car():
    # Disable other buttons while adding a car
    disable_buttons()
    
    # Create labels and entry fields for car name and fuel type
    car_name_label = tk.Label(win, text="Car Name:")
    car_name_label.grid(row=0, column=0, padx=10, pady=5)
    car_name_entry = tk.Entry(win)
    car_name_entry.grid(row=0, column=1, padx=10, pady=5)
    
    fuel_type_label = tk.Label(win, text="Fuel Type:")
    fuel_type_label.grid(row=1, column=0, padx=10, pady=5)
    fuel_type_combo = ttk.Combobox(win, values=["Electric", "Gasoline"])
    fuel_type_combo.grid(row=1, column=1, padx=10, pady=5)
    
    # Function to handle submission of car details
    def submit_car():
        car_name = car_name_entry.get()
        fuel_type = fuel_type_combo.get()
        file_path = os.path.join(folder_path, car_name + ".txt")
        
        # Check if the file already exists
        if os.path.exists(file_path):
            notification_label.config(text=f"Car '{car_name}' already exists!", fg="red")
            win.after(3000, clear_notification)
        else:
            # Write car details to file
            with open(file_path, 'w') as file:
                file.write(fuel_type)
                
            # Notify user and clear entry fields
            notification_label.config(text=f"Car '{car_name}' added successfully!", fg="green")
            car_name_entry.delete(0, tk.END)
            fuel_type_combo.set("")
            
            # Update ComboBox with new car name
            update_combobox()
    
    # Button to submit car details
    submit_button = tk.Button(win, text="Submit", command=submit_car)
    submit_button.grid(row=2, column=1, padx=10, pady=5)

# Function to delete a car
def delete_car():
    selected_car = cars_combobox.get()
    if selected_car:
        file_path = os.path.join(folder_path, selected_car + ".txt")
        os.remove(file_path)
        notification_label.config(text=f"Car '{selected_car}' deleted successfully!", fg="green")
        update_combobox()
    else:
        notification_label.config(text="Please select a car to delete!", fg="red")
        win.after(3000, clear_notification)

# Function to disable buttons while adding a car
def disable_buttons():
    add_car_button.config(state=tk.DISABLED)
    delete_car_button.config(state=tk.DISABLED)
    counter_button.config(state=tk.DISABLED)
    average_button.config(state=tk.DISABLED)

# Function to enable buttons after adding a car
def enable_buttons():
    add_car_button.config(state=tk.NORMAL)
    delete_car_button.config(state=tk.NORMAL)
    counter_button.config(state=tk.NORMAL)
    average_button.config(state=tk.NORMAL)

# Function to clear notification after some time
def clear_notification():
    notification_label.config(text="")

# Function to update ComboBox with list of cars
def update_combobox():
    cars_combobox['values'] = [f.replace(".txt", "") for f in os.listdir(folder_path) if f.endswith('.txt')]

# Main Tkinter window
win = tk.Tk()
win.title("Fuel Calculator")
win.geometry("400x200")

# Folder path for car data files
folder_path = "C:\\Users\\Dhanes\\Documents\\App Data\\Visual Code\\Dhanes Project\\Fuel Counter\\Data"

# Add Car button
add_car_button = tk.Button(win, text="Add Car", command=add_car)
add_car_button.grid(row=0, column=0, padx=10, pady=5)

# Delete Car button
delete_car_button = tk.Button(win, text="Delete Car", command=delete_car)
delete_car_button.grid(row=0, column=1, padx=10, pady=5)

# Counter button (placeholder)
counter_button = tk.Button(win, text="Counter", state=tk.DISABLED)
counter_button.grid(row=1, column=0, padx=10, pady=5)

# Average button (placeholder)
average_button = tk.Button(win, text="Average", state=tk.DISABLED)
average_button.grid(row=1, column=1, padx=10, pady=5)

# Notification label
notification_label = tk.Label(win, text="", fg="green")
notification_label.grid(row=2, columnspan=2, padx=10, pady=5)

# ComboBox to display list of cars
cars_combobox = ttk.Combobox(win, width=30)
cars_combobox.grid(row=3, columnspan=2, padx=10, pady=5)
update_combobox()

# Enable buttons initially
enable_buttons()

win.mainloop()

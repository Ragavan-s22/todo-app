import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Define a list to store complaints
complaints = []

# Function to submit a complaint
def submit_complaint():
    title = title_entry.get()
    description = description_entry.get("1.0", tk.END)
    priority = priority_combobox.get()
    category = category_combobox.get()
    complaint_id = len(complaints) + 1
    status = "Open"
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = user_entry.get()

    complaint = {
        "complaint_id": complaint_id,
        "title": title,
        "description": description,
        "priority": priority,
        "category": category,
        "status": status,
        "date": date,
        "user": user,
    }

    complaints.append(complaint)
    status_label.config(text="Complaint submitted successfully.")
    save_to_file(complaint)  # Save the complaint to the text file

# Function to save the complaint to a text file
def save_to_file(complaint):
    with open("text.txt", "a") as file:
        file.write(f"Complaint ID: {complaint['complaint_id']}\n")
        file.write(f"Title: {complaint['title']}\n")
        file.write(f"Description: {complaint['description']}\n")
        file.write(f"Priority: {complaint['priority']}\n")
        file.write(f"Category: {complaint['category']}\n")
        file.write(f"Status: {complaint['status']}\n")
        file.write(f"Date: {complaint['date']}\n")
        file.write(f"User: {complaint['user']}\n")
        file.write("\n")

# Function to view complaints from the text file
def view_complaints():
    view_window = tk.Toplevel(root)
    view_window.title("View Complaints")
    view_window.geometry("600x400")

    complaints_text = tk.Text(view_window, width=60, height=20)
    complaints_text.pack(fill="both", expand=True)

    with open("text.txt", "r") as file:
        complaints_text.insert(tk.END, file.read())

# Create a Tkinter window
root = tk.Tk()
root.title("Complaint Management System")

# Create and configure labels, entry fields, and buttons
title_label = ttk.Label(root, text="Title:")
title_entry = ttk.Entry(root, width=40)
description_label = ttk.Label(root, text="Description:")
description_entry = tk.Text(root, width=40, height=5)
priority_label = ttk.Label(root, text="Priority:")
priority_combobox = ttk.Combobox(root, values=["Low", "Medium", "High"])
category_label = ttk.Label(root, text="Category:")
category_combobox = ttk.Combobox(root, values=["Technical", "Billing", "General"])
user_label = ttk.Label(root, text="Your Name:")
user_entry = ttk.Entry(root, width=40)
submit_button = ttk.Button(root, text="Submit Complaint", command=submit_complaint)
status_label = ttk.Label(root, text="")

# Place widgets in the grid
title_label.grid(row=0, column=0, sticky="w")
title_entry.grid(row=0, column=1, columnspan=2)
description_label.grid(row=1, column=0, sticky="w")
description_entry.grid(row=1, column=1, columnspan=2)
priority_label.grid(row=2, column=0, sticky="w")
priority_combobox.grid(row=2, column=1, columnspan=2)
category_label.grid(row=3, column=0, sticky="w")
category_combobox.grid(row=3, column=1, columnspan=2)
user_label.grid(row=4, column=0, sticky="w")
user_entry.grid(row=4, column=1, columnspan=2)
submit_button.grid(row=5, column=0, columnspan=3)
status_label.grid(row=6, column=0, columnspan=3)

# Add a "View Complaints" button
view_complaints_button = ttk.Button(root, text="View Complaints", command=view_complaints)
view_complaints_button.grid(row=7, column=0, columnspan=3)

# Start the Tkinter main loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox

def sort_names():
    names = name_entry.get()
    names = names.split(",")
    sorted_names = sorted(names)
    messagebox.showinfo("Sorted Names", ", ".join(sorted_names))
    libel2.config(text="The sorted names has been saved in sorted_names.txt")
    with open("sorted_names.txt","w") as file:
         for i in sorted_names:
             file.write(f"{i}\n")
root = tk.Tk()
root.title("Name Sorter")
root.geometry("650x600")

name_label = tk.Label(root, text="Enter names (separated by commas):", font=('Arial Bold',15))
name_label.pack()

name_entry = tk.Entry(root, width=40)
name_entry.pack()

sort_button = tk.Button(root, text="Sort", command=sort_names)
sort_button.pack()
libel2 = tk.Label(root, text="", font=('Arial Bold', 10), fg="red")
libel2.pack()
libel3 = tk.Label(root, text="Github: https://github.com/some-man1", font=('Arial Bold', 10), fg="red")
libel3.pack(side=tk.BOTTOM, anchor=tk.SW) 
libel4 = tk.Label(root, text="Telegram: @RD515Y", font=('Arial Bold', 10), fg="blue")
libel4.pack(side=tk.BOTTOM, anchor=tk.SW) 

root.mainloop()

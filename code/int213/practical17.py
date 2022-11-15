import tkinter as tk;


window = tk.Tk()
x = tk.IntVar()
window.title("Python GUI")
button = tk.Button(window, text="Button", width=30, command=window.destroy)
lb = tk.Listbox(window, height=20, bd=8, bg="PINK", font=("Times", 14))
r1 = tk.Radiobutton(text="Option 1", variable=x, value=1)
r1.pack()
r2 = tk.Radiobutton(text="Option 2", variable=x, value=2)
r2.pack()

for i in range(15):
    lb.insert(tk.END, i)

lb.pack()
button.pack()
window.mainloop()
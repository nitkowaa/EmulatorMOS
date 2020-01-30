import tkinter as tk
from tkinter import filedialog,Text
import gui
import os
programs_names = []
root = tk.Tk()

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        temp_programm_names = f.read()
        temp_programm_names = temp_programm_names.split(',')
        programs_names = [x for x in temp_programm_names if x.strip()]
def runcode():

    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes =(("text files","*.txt"),("all files","*.*")))
    programs_names.append(filename)
    print(filename)
    for program in programs_names:
        label = tk.Label(frame,text=program,bg="gray")
        label.pack()
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

def run6502():
    for program in programs_names:
        os.startfile(program)

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command = runcode)
openFile.pack()
runcode = tk.Button(root, text="Run Code", padx=10, pady=5, fg="white", bg="#263D42",command = run6502)
runcode.pack()


for program in programs_names:
    label = tk.Label(frame,text=program)
    label.pack()
root.mainloop()

with open('save.txt','w') as f:
    for program in programs_names:
        f.write(program +',')
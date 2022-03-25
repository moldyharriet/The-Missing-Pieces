import tkinter as tk
from tkinter import END, LEFT, RIGHT, Listbox, Toplevel

#main window information
window = tk.Tk()
lb1 = Listbox(window, width = "20", height = "4", highlightcolor = "yellow")
lb1.insert(1, "Bosses")
lb1.insert(2, "NPCs")
lb1.insert(3, "Sidequests")
lb1.insert(4, "Dungeons/Caves")

greeting = tk.Label(text = "Welcome to the Missing Pieces! \n v.01",  fg = "black")

def boss_window():
    nwindow = tk.Toplevel()
    path = r"C:\Users\Chase Gibbs\Desktop\desktop files\coding files\python files\The Missing Pieces\bossinfo.txt"
    tk.Label(nwindow, text = "Type down which bosses you've fought, and their rewards below.").pack(pady = 5)
    def submitaction():
        path = r"C:\Users\Chase Gibbs\Desktop\desktop files\coding files\python files\The Missing Pieces\bossinfo.txt"
        bossfile = open(path, "r+")
        bossfile.write(nwindow_text.get("1.0", END))
        bossfile.close()
    nwindow_text = tk.Text(nwindow)
    nwindow_text.pack(pady = 20, padx = 20) 
    nwindow.geometry("640x500")
    nwindow.title("Bosses")
    backbutton = tk.Button(nwindow, text = "Back", command = nwindow.destroy, fg = "blue")
    submitbutton = tk.Button(nwindow, text = "Submit", fg = "blue", command = submitaction)
    backbutton.pack(side = LEFT, padx = 15)
    submitbutton.pack(side = RIGHT, padx = 15)
    nwindow_text.insert("1.0", "string")
    #read the file contents, then .insert() them into the .Text() widget of boss_window()
#    class __enter__:
#        with open(path, "r") as firstfile, nwindow_text as secondfile:
#            for line in firstfile:
#                secondfile.insert(line)

selectlboption = tk.Button(text = "Select", fg = "blue", bg = "white", command = boss_window)


#geometry and window titles
greeting.pack()
window.geometry("500x400")
lb1.pack()
selectlboption.pack(pady = "5")
window.title("The Missing Pieces v0.1")



window.mainloop()
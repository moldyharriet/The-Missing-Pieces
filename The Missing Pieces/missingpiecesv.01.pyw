import tkinter as tk
from tkinter import ANCHOR, END, LEFT, RIGHT, Listbox, Toplevel, INSERT
import os

#main window information
window = tk.Tk()

greeting = tk.Label(text = "Welcome to the Missing Pieces! \n v.01",  fg = "black")

def boss_window():
    nwindow = tk.Toplevel()
    tk.Label(nwindow, text = "Type down which bosses you've fought, and their rewards below.").pack(pady = 5)
    def submitaction():
        cwd = os.getcwd()
        path = (cwd + r"\The Missing Pieces\bossinfo.txt")
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
    savewarning = tk.Label(nwindow, text = "You MUST press submit, or else changes will not be saved.")
    savewarning.pack(pady = 10)
    cwd = os.getcwd()
    path = (cwd + r"\The Missing Pieces\bossinfo.txt")
    with open(path, 'r') as i:
        nwindow_text.insert(INSERT, i.read())

def npc_window():
    nwindow = tk.Toplevel()
    tk.Label(nwindow, text = "Type down which NPCs you've spoken with, and what they've given you below.").pack(pady = 5)
    def submitaction():
        cwd = os.getcwd()
        path = (cwd + r"\The Missing Pieces\bossinfo.txt")
        npcfile = open(path, "r+")
        npcfile.write(nwindow_text.get("1.0", END))
        npcfile.close()
    nwindow_text = tk.Text(nwindow)
    nwindow_text.pack(pady = 20, padx = 20) 
    nwindow.geometry("640x500")
    nwindow.title("NPCs")
    backbutton = tk.Button(nwindow, text = "Back", command = nwindow.destroy, fg = "blue")
    submitbutton = tk.Button(nwindow, text = "Submit", fg = "blue", command = submitaction)
    backbutton.pack(side = LEFT, padx = 15)
    submitbutton.pack(side = RIGHT, padx = 15)
    savewarning = tk.Label(nwindow, text = "You MUST press submit, or else changes will not be saved.")
    savewarning.pack(pady = 10)
    cwd = os.getcwd()
    path = (cwd + r"\The Missing Pieces\bossinfo.txt")
    with open(path, 'r') as i:
        nwindow_text.insert(INSERT, i.read())
        
def sidequest_window():
    nwindow = tk.Toplevel()
    tk.Label(nwindow, text = "Type down which sidequests you've begun, and their information below.").pack(pady = 5)
    def submitaction():
        cwd = os.getcwd()
        path = (cwd + r"\The Missing Pieces\bossinfo.txt")
        sidequestfile = open(path, "r+")
        sidequestfile.write(nwindow_text.get("1.0", END))
        sidequestfile.close()
    nwindow_text = tk.Text(nwindow)
    nwindow_text.pack(pady = 20, padx = 20) 
    nwindow.geometry("640x500")
    nwindow.title("Sidequests")
    backbutton = tk.Button(nwindow, text = "Back", command = nwindow.destroy, fg = "blue")
    submitbutton = tk.Button(nwindow, text = "Submit", fg = "blue", command = submitaction)
    backbutton.pack(side = LEFT, padx = 15)
    submitbutton.pack(side = RIGHT, padx = 15)
    savewarning = tk.Label(nwindow, text = "You MUST press submit, or else changes will not be saved.")
    savewarning.pack(pady = 10)
    cwd = os.getcwd()
    path = (cwd + r"\The Missing Pieces\bossinfo.txt")
    with open(path, 'r') as i:
        nwindow_text.insert(INSERT, i.read())

def dungeon_window():
    nwindow = tk.Toplevel()
    tk.Label(nwindow, text = "Type down which Dungeons and Caves you've worked through, and what the rewards for them were below.").pack(pady = 5)
    def submitaction():
        cwd = os.getcwd()
        path = (cwd + r"\The Missing Pieces\bossinfo.txt")
        dungeonfile = open(path, "r+")
        dungeonfile.write(nwindow_text.get("1.0", END))
        dungeonfile.close()
    nwindow_text = tk.Text(nwindow)
    nwindow_text.pack(pady = 20, padx = 20) 
    nwindow.geometry("640x500")
    nwindow.title("Dungeons")
    backbutton = tk.Button(nwindow, text = "Back", command = nwindow.destroy, fg = "blue")
    submitbutton = tk.Button(nwindow, text = "Submit", fg = "blue", command = submitaction)
    backbutton.pack(side = LEFT, padx = 15)
    submitbutton.pack(side = RIGHT, padx = 15)
    savewarning = tk.Label(nwindow, text = "You MUST press submit, or else changes will not be saved.")
    savewarning.pack(pady = 10)
    cwd = os.getcwd()
    path = (cwd + r"\The Missing Pieces\bossinfo.txt")
    with open(path, 'r') as i:
        nwindow_text.insert(INSERT, i.read())


lb1 = Listbox(window, width = "20", height = "4", highlightcolor = "yellow")
ListOptions = ["Bosses", "NPCs", "Sidequests", "Dungeons/Caves", END]
for item in ListOptions:
    lb1.insert(END, item)

def lbSelected():
    selectedoption = lb1.get(ANCHOR)
    if selectedoption == "Bosses":
        boss_window()
    elif selectedoption == "NPCs":
        npc_window()
    elif selectedoption == "Sidequests":
        sidequest_window()
    elif selectedoption == "Dungeons/Caves":
        dungeon_window()

selectlboption = tk.Button(text = "Select", fg = "blue", bg = "white", command = lbSelected)

#geometry and window titles
greeting.pack()
window.geometry("500x400")
lb1.pack()
selectlboption.pack(pady = "5")
window.title("The Missing Pieces v0.1")



window.mainloop()
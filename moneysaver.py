import os, csv, datetime
from tkinter import *
from tkinter.ttk import *

currentDir = os.path.dirname(os.path.abspath(__file__))#current directory

# Data class to handle all data, saving files, etc.
# made to be a class to keep data 
class Data():
    def __init__(self): #initialize class with variables
        self.bank = 0
        self.income = 0
        self.spending = 0
        self.itemlist = []
        self.iselect = 1
        self.disablelist = []
        self.total = 0
    
    def __init__(self, filename): #initialize class with variables, using those from a file given
        file = csv.reader(open(currentDir + "\datafiles\\" + filename))
        lines = list(file)
        self.bank = lines[0][1]
        self.income = lines[1][1]
        self.spending = lines[2][1]
        self.itemlist = lines[4:]
        self.filename = filename
        self.iselect = len(self.itemlist)
        self.disablelist = []
        for i in self.itemlist:
            self.disablelist.append(True)
        self.total = 0
        self.calculate()

    def setfile(self, filename): #change values used by class by taking from specified file
        file = csv.reader(open(currentDir + "\datafiles\\" + filename))
        lines = list(file)
        self.bank = lines[0][1]
        self.income = lines[1][1]
        self.spending = lines[2][1]
        self.itemlist = lines[4:]
        self.filename = filename
        self.iselect = len(self.itemlist)
        self.disablelist = []
        for i in self.itemlist:
            self.disablelist.append(True)
        self.total = 0
        self.calculate()

    def writefile(self):
        mainframe.config(text="File Loaded:   " + data.filename + " Saving...")    
        file = csv.reader(open(currentDir + "\datafiles\\" + self.filename))
        lines = list(file)
        lines[0][1] = data.bank
        lines[1][1] = data.income
        lines[2][1] = data.spending
        lines[4:] = self.itemlist
        writer = csv.writer(open(currentDir + "\datafiles\\" + self.filename, "w", newline=''))
        writer.writerows(lines)
        mainframe.config(text="File Loaded:   " + data.filename)
        
    def calculate(self):
        self.total = 0
        for i in range (0, len(self.itemlist)):
            if(self.disablelist[i] == True):
                self.total += int((self.itemlist[i])[1])
        
    def getbank(self):
        return self.bank
    
    def getincome(self):
        return self.income

    def getspending(self):
        return self.spending
    


data = Data("file01.csv")

def update(): #update all visuals of data SEEN BY THE USER
    data.writefile()
    data.calculate()
    
    mainframe.config(text="File Loaded:   " + data.filename)
    
    bankentry.config(state=NORMAL)
    bankentry.delete("1.0", END)
    bankentry.insert(END, data.bank)
    bankentry.config(state=DISABLED)
    incomeentry.config(state=NORMAL)
    incomeentry.delete("1.0", END)
    incomeentry.insert(END, data.income)
    incomeentry.config(state=DISABLED)
    spendingentry.config(state=NORMAL)
    spendingentry.delete("1.0", END)
    spendingentry.insert(END, data.spending)
    spendingentry.config(state=DISABLED)

    itemtext.config(state=NORMAL)
    itemtext.delete("1.0", END)
    if(len(data.itemlist) > 0):
        for item in data.itemlist:
            itemtext.insert(END, ": $".join(item) + "\n")
        for i in range(0,len(data.disablelist)+1):
            if(data.disablelist[i-1] == False):
                    itemtext.tag_add("disabled", str(i)+".0", str(i+1)+".0")
                    itemtext.tag_config("disabled", foreground="grey")
            else:
                    itemtext.tag_remove("disabled", str(i)+".0", str(i+1)+".0")            
        itemtext.config(state=DISABLED)
    
        itemtext.tag_remove("start", str(data.iselect-1)+".0", str(data.iselect)+".0")
        itemtext.tag_add("start", str(data.iselect)+".0", str(data.iselect+1)+".0")
        itemtext.tag_config("start", background="light grey")
        
        if(data.disablelist[data.iselect-1] == True):
            disablebutton.config(text="Disable")
        else:
            disablebutton.config(text="Enable")
        
    totaltext.config(state=NORMAL)
    totaltext.delete("1.0", END)
    totaltext.insert(END, "$" + str(data.total))
    totaltext.config(state=DISABLED)
    
def bankedit():
    def savefunc():
        data.bank = (bankeditentry.get("1.0", END)).strip("\n")
        update()
        window.destroy()

    def cancelfunc():
        window.destroy()
    window = Toplevel(padx=10, pady=10)
    Label(window, text="Enter how much money you currently got on ya:").grid(column=0, row=0, columnspan=2)
    bankeditentry = Text(window, width=32, height=1)
    bankeditentry.grid(column=0, row=1, columnspan=2, pady=10)
    savebutton = Button(window, text="Save", command=savefunc).grid(column=0, row=2, sticky="e")
    cancelbutton = Button(window, text="Cancel", command=cancelfunc).grid(column=1, row=2, sticky="w")

def incomeedit():
    def savefunc():
        data.income = (incomeeditentry.get("1.0", END)).strip("\n")
        update()
        window.destroy()
    def cancelfunc():
        window.destroy()
    window = Toplevel(padx=10, pady=10)
    Label(window, text="Enter Monthly Income:").grid(column=0, row=0, columnspan=2)
    incomeeditentry = Text(window, width=32, height=1)
    incomeeditentry.grid(column=0, row=1, columnspan=2, pady=10)
    savebutton = Button(window, text="Save", command=savefunc).grid(column=0, row=2, sticky="e")
    cancelbutton = Button(window, text="Cancel", command=cancelfunc).grid(column=1, row=2, sticky="w")

def spendedit():
    def savefunc():
        data.spending = (spendeditentry.get("1.0", END)).strip("\n")
        update()
        window.destroy()
    def cancelfunc():
        window.destroy()
        
    window = Toplevel(padx=10, pady=10)
    Label(window, text="How much you spent:").grid(column=0, row=0, columnspan=2)
    spendeditentry = Text(window, width=32, height=1)
    spendeditentry.grid(column=0, row=1, columnspan=2, pady=10)
    savebutton = Button(window, text="Save", command=savefunc).grid(column=0, row=2, sticky="e")
    cancelbutton = Button(window, text="Cancel", command=cancelfunc).grid(column=1, row=2, sticky="w")

def loadfunc():
    def loadfunc():
        data.setfile(filename.get())
        update()
        window.destroy()
    def cancelfunc():
        window.destroy()
    templist = os.listdir(currentDir + "\\datafiles\\")
    filename = StringVar()
    initial = data.filename
    window = Toplevel(padx=25, pady=25)
    Label(window, text="Pick a file to load:").grid(column=0, row=0, padx=30, columnspan=2)
    dropdown = OptionMenu(window, filename, initial, *templist).grid(column=0, row=1, pady=20, sticky="w", columnspan=2)
    loadbutton = Button(window, text="Load", command=loadfunc).grid(column=0, row=2)
    cancelbutton = Button(window, text="Cancel", command=cancelfunc).grid(column=1, row=2)

def newfunc():
    currentdate = ("".join((list(str(datetime.datetime.now())))[:16])).replace(":", "h")
    file = open(currentDir + "\datafiles\\" + currentdate + ".csv", "w")
    writer = (open(currentDir + "\datafiles\\template.csv", "r"))
    for line in writer:
        file.write(line)
    file.close()
    writer.close()
    data.setfile(currentdate + ".csv")
    update()
    
def addfunc():
    def savefunc():
        temp = []
        temp.append(nameentry.get())
        temp.append(priceentry.get())
        data.itemlist.append(temp)
        data.disablelist.append(True)
        data.iselect = len(data.itemlist)
        update()
        window.destroy()

    def cancelfunc():
        window.destroy()

    window = Toplevel(padx=25, pady=10)
    Label(window, text="Enter item information:").grid(column=0, row=0, columnspan=2, pady=15)

    Label(window, text="Item name: ").grid(column=0, row=1, sticky="w")
    nameentry = Entry(window, width=20)
    nameentry.grid(column=1, row=1, pady=10)
    # nameentry.insert(END, data.itemlist)
    Label(window, text="Enter item price ($): ").grid(column=0, row=2, sticky="w")
    priceentry = Entry(window, width=20)
    priceentry.grid(column=1, row=2, pady=10)

    savebutton = Button(window, text="Add", command=savefunc).grid(column=0, row=3, sticky="e", pady=(10,0))
    cancelbutton = Button(window, text="Cancel", command=cancelfunc).grid(column=1, row=3, sticky="w", pady=(10,0))    
    
def upfunc():
    if(1 < data.iselect <= len(data.itemlist)):
        data.iselect -= 1
    update()
    
def downfunc():
    if(1 <= data.iselect < len(data.itemlist)):
        data.iselect += 1
    update()    

def editfunc():
    def savefunc():
        (data.itemlist[data.iselect-1])[0] = nameentry.get("1.0", END).strip("\n")
        (data.itemlist[data.iselect-1])[1] = priceentry.get("1.0", END).strip("\n")
        update()
        window.destroy()
    
    def cancelfunc():
        window.destroy()    
         
    window = Toplevel(padx=25, pady=10)
    Label(window, text="Enter item information:").grid(column=0, row=0, columnspan=2, pady=15)
    
    Label(window, text="Item Name: ").grid(column=0, row=1, sticky="w")
    nameentry = Text(window, height=1, width=16)
    nameentry.grid(column=1, row=1, pady=10)
    nameentry.insert(END, data.itemlist[data.iselect-1][0])
    Label(window, text="Enter Item Price ($)").grid(column=0, row=2, sticky="w")
    priceentry = Text(window, height=1, width=16)
    priceentry.grid(column=1, row=2, pady=10)
    priceentry.insert(END, data.itemlist[data.iselect-1][1])
    
    savebutton = Button(window, text="Save", command=savefunc).grid(column=0, row=3, sticky="e", pady=(10,0))
    cancelbutton = Button(window, text="Cancel", command=cancelfunc).grid(column=1, row=3, sticky="w", pady=(10,0))      

def disablefunc():
    if(data.disablelist[data.iselect-1] == True):
        data.disablelist[data.iselect-1] = False
    elif(data.disablelist[data.iselect-1] == False):
        data.disablelist[data.iselect-1] = True
    else:
        print("ERROR IN DISABLE FUNC")
    update()

def deletefunc():
    for i in range(data.iselect, len(data.itemlist)):
        data.itemlist[i-1] = data.itemlist[i]
        data.disablelist[i-1] = data.disablelist[i]
    data.itemlist.pop(len(data.itemlist)-1)
    data.disablelist.pop(len(data.disablelist)-1)
    if(data.iselect-1 == len(data.itemlist)):
        data.iselect -= 1
    update()

root = Tk()
#root.minsize(800,600)

mainframe = LabelFrame(root, text="NUTSACK!!!", padding=20)
mainframe.grid(column=0, row=0, padx=20, pady=20)

#title
title = Label(mainframe, text="MONEYSAVER.EXE")
title.grid(column=0, row=0, columnspan=5)

# BANK ACCOUNT
Label(mainframe, text="Current Bank Amt ($)").grid(column=0, row=1, columnspan=4, sticky="w")
bankbutton = Button(mainframe, text="Edit", command=bankedit)
bankbutton.grid(column=4, row=1, sticky="e")
bankentry = Text(mainframe, height=1, width=30)
bankentry.grid(column=0, row=2, columnspan=5, pady=(0,20))

# PAYCHECK/INCOME
Label(mainframe, text="Average Monthly Income ($)").grid(column=0, row=3, columnspan=4, sticky="w")
incomebutton = Button(mainframe, text="Edit", command=incomeedit)
incomebutton.grid(column=4, row=3, sticky="e")
incomeentry = Text(mainframe, height=1, width=30)
incomeentry.grid(column=0, row=4, columnspan=5, pady=(0,20))

# SPENDING/CREDIT CARD
Label(mainframe, text="Current Credit Card Bill ($)").grid(column=0, row=5, columnspan=4, sticky="w")
spendingbutton = Button(mainframe, text="Edit", command=spendedit)
spendingbutton.grid(column=4, row=5, sticky="e")
spendingentry = Text(mainframe, height=1, width=30)
spendingentry.grid(column=0, row=6, columnspan=5, pady=(0,20))

# BIG ENTRY BOX
Label(mainframe, text="Stuff you wanna buy/have bought").grid(column=0, row=7, columnspan=5, sticky="w")
itemtext = Text(mainframe, height=8, width=30)
itemtext.grid(column=0, row=8, columnspan=5, sticky="w")

Label(mainframe, text="Total: ").grid(column=0, row=9, sticky="w")
totaltext = Text(mainframe, height=1, width=25)
totaltext.grid(column=1, row=9, columnspan=4, sticky="w")

upbutton = Button(mainframe, text="Up", width=5, command=upfunc).grid(column=0, row=10, sticky="w")
downbutton = Button(mainframe, text="Down", width=5, command=downfunc).grid(column=0, row=11, sticky="w")
editbutton = Button(mainframe, text="Edit", width=15, command=editfunc).grid(column=1, row=10, sticky="e")
addbutton = Button(mainframe, text="Add", width=15, command=addfunc).grid(column=3, row=10, sticky="w", columnspan=2)
disablebutton = Button(mainframe, text="No Selection", width=15, command=disablefunc)
disablebutton.grid(column=1, row=11, sticky="e")
deletebutton = Button(mainframe, text="Delete", width=15, command=deletefunc).grid(column=3, row=11, sticky="e", columnspan=2)

# SAVE AND LOAD
loadbutton = Button(mainframe, text="Load", width=18, command=loadfunc).grid(column=5, row=11)
newbutton = Button(mainframe, text="New", width=18, command=newfunc).grid(column=5, row=10, sticky="s")

# SECOND FRAME THAT HOLDS OUTPUT
outputframe = LabelFrame(root, padding=20)
outputframe.grid(column=1, row=0)

update()

root.mainloop()
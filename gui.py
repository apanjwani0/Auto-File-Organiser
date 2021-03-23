import tkinter as tk
import tkinter.filedialog
import organiseFiles
# import organiseFiles.py

root=tk.Tk('Auto File Mover','some Basename','some classname',1)


directoryFrame=tk.Frame(root)
inputFrame=tk.Frame(root)
buttonFrame=tk.Frame(root)

directoryFrame.pack()
inputFrame.pack()
buttonFrame.pack()


directory=tk.StringVar()
dirLabel=tk.Label(directoryFrame,text='Enter Directory path : ').grid(row=0,column=0)
dirEntry=tk.Entry(directoryFrame,textvariable=directory)
dirEntry.grid(row=0,column=1)
def browseDir():
    dirname = tk.filedialog.askdirectory()
    directory.set(dirname)
browseButton=tk.Button(directoryFrame,text="Browse",command=browseDir).grid(row=0,column=2)
directoryFrame.columnconfigure(1,weight=1)


i=0
tinkerDict={}
typeFolder={}
def addField():
    global i
    type=tk.StringVar()
    folder=tk.StringVar()
    label=tk.Label(inputFrame,text='File type : ').grid(row=i,column=0)
    entry=tk.Entry(inputFrame,textvariable=type).grid(row=i,column=1)
    label=tk.Label(inputFrame,text='Folder Name : ').grid(row=i,column=2)
    entry=tk.Entry(inputFrame,textvariable=folder).grid(row=i,column=3)
    
    tinkerDict[i]=type,folder
    i+=1
    print('Added')

addField()

def submit():
    print('get values')
    for i in tinkerDict:
        type=tinkerDict[i][0].get()
        folder=tinkerDict[i][1].get()
        if type is '' or folder is '':
            continue
        typeFolder[type]=folder
    print(typeFolder)
    directory.get()
    print(directory.get())
    
    #Validate
    #Confirmation
    organiseFiles.calledFromOther(directory.get(),typeFolder)
    #call orgainseFiles

    root.destroy()


addButton=tk.Button(buttonFrame,text='Add Field',width=25,command=addField)
addButton.grid(row=0,column=0)

submitButton=tk.Button(buttonFrame,text='Submit',width=25,command=submit)
submitButton.grid(row=0,column=1)




root.mainloop()



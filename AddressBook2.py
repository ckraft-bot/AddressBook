#import library
from tkinter import *

#initialize window
root = Tk()
root.geometry('400x400')
root.config(bg = 'SlateGray3')
root.title('Ivy League School Admission')
root.resizable(0,0)
contactlist = [
    ['Harvard',   '617-495-1551'],
    ['Yale',  '203-432-9316'],
    ['Princeton',  '609-258-3060'],
    ['Columbia',  '212-854-2522'],
    ['Brown',  '401-863-1000'],
    ['Dartmouth','603-646-2875'],
    ['U Penn',  '215-898-7507'],
    ['Cornell','607-255-5241'],
    ]

Name = StringVar()
Number = StringVar()


#create frame
frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)


########### function to get select value

def Selected():
    return int(select.curselection()[0])
    
##fun to add new contact
def AddContact():
    contactlist.append([Name.get(), Number.get()])
    Select_set()

# fun to edit existing contact(first select the contact then click on view button then edit the contact and then click on edit button)
def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get()]
    Select_set()
    
#to delete selected contact
def DELETE():
    del contactlist[Selected()]
    Select_set()
   
# to view selected contact(first select then click on view button)
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)


###exit game window   
def EXIT():
    root.destroy()

#empty name and number field
def RESET():
    Name.set('')
    Number.set('')


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
Select_set()



######define buttons #####labels and entry widget
Label(root, text = 'NAME', font='Avenir 12 bold', bg = 'SlateGray3').place(x= 30, y=20)
Entry(root, textvariable = Name).place(x= 100, y=20)
Label(root, text = 'PHONE NO.', font='Avenir 12 bold',bg = 'SlateGray3').place(x= 30, y=70)
Entry(root, textvariable = Number).place(x= 130, y=70)

Button(root,text=" ADD", font='Avenir 12 bold',bg='SlateGray4', command = AddContact).place(x= 50, y=110)
Button(root,text="EDIT", font='Avenir 12 bold',bg='SlateGray4',command = EDIT).place(x= 50, y=260)
Button(root,text="DELETE", font='Avenir 12 bold',bg='SlateGray4',command = DELETE).place(x= 50, y=210)
Button(root,text="VIEW", font='Avenir 12 bold',bg='SlateGray4', command = VIEW).place(x= 50, y=160)
Button(root,text="EXIT", font='Avenir 12 bold',bg='tomato', command = EXIT).place(x= 300, y=320)
Button(root,text="RESET", font='Avenir 12 bold',bg='SlateGray4', command = RESET).place(x= 50, y=310)


root.mainloop()
  

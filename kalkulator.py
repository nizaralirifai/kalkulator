from tkinter import *
import math

root = Tk()
blank_space = " "

# namaapknya
root.title (50 * blank_space + "Calculating App")
# buat matiin auto sizeny
root.resizable(width =FALSE, height = False)
# atur size apknya
root.geometry("438x505+460+40")

# create a frame
coverFrame = Frame (root, bd=20, pady=2, relief = RIDGE)
coverFrame.grid()

# child of coverFrame
coverMainFrame = Frame (coverFrame, bd=10, pady=2, bg='darkcyan',  relief = RIDGE)
coverMainFrame.grid()

# mainframe child of coverMainFrame
MainFrame = Frame (coverMainFrame, bd=5, pady=2, relief = RIDGE)
MainFrame.grid()

# membuat class
class Calculator():
    # membuat function namanya self
    def __init__(self):
        # manggil functionnya 'self'
        self.total = 0
        self.current =""
        self.input_value= True
        self.check_sun = False
        self.op = ""
        self.result = False

    # membuat function agar buttonnya mulai berfungsi
    def numberEnter(self,num):
        self.result = False
        firstnum = entDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum():
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def display(self,value):
        entDisplay.delete(0, END)
        entDisplay.insert(0, value)

    def sum_of_total(self):
              self.result = True
              self.current = float(self.current)
              if self.check_sun==True:
                     self.valid_function()
              else:
                     self.total= float(entDisplay.get())
    def valid_function(self):
              if self.op == "add":
                     self.total += self.current
              if self.op == "sub":
                     self.total -= self.current
              if self.op == "multi":
                     self.total *= self.current
              if self.op == "divide":
                     self.total /= self.current
              if self.op == "mod":
                     self.total %= self.current
              self.input_value = True
              self.check_sun = False
              self.display(self.total)

    def opration(self, op):
        self.current = float(self.current)
        if self.check_sun:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sun = True
        self.op = op
        self.result = False

    def backspace(self):
        numLen = len(entDisplay.get())
        entDisplay.delete(numLen - 1, 'end')
        if numLen == 1:
            entDisplay.insert(0, "0")

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True
    
    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def matchPM(self):
        self.result = False
        self.current = -(float(entDisplay.get()))
        self.display(self.current)
    
# added_value: var global
# manggil class calculator
added_value = Calculator()
# Child of MainFrame
# Ini desain buat yang form calculatornya
entDisplay = Entry(MainFrame, font=('arial',18, 'bold'), bd=14, width=26,bg='black',fg= 'white', justify=RIGHT)
entDisplay.grid(row =0, column=0, columnspan=4, pady=1)
entDisplay.insert(0, "0")

numpad = "789456123"

i = 0
btn = []

for j in range(3,6):
    # pas ngatur column manggil k berarti columnnya 3
    for k in range(3):
        # letaknya dalam mainframe
        btn.append(Button(MainFrame, width=6,height=2, font=('arial',16, 'bold'), bd=4, text=numpad[i]))
        # bd :border
        btn[i].grid(row=j, column=k, pady=1)
        # kan ngambil dari numpad, abis itu kita tampilin si [i] nya
        # kaya gitu terus sambil i nya itu di tambahin 1+1 terus, jadi dia menampilkan semua datanya, systemnya kayanya dia array deh
        btn[i]["command"] = lambda x=numpad[i]: added_value.numberEnter(x)
        i += 1

# BACKSPACE
# Membuat button backspace, child dari mainframe ((biar si backspacenya itu didalam grid MainFrame))
btnBackSpace = Button(MainFrame, width=13, height=2, font=('arial', 16, 'bold'), bd=4, text="←", 
bg='red', fg='white', command= added_value.backspace) 
# Posisi buttonnya
btnBackSpace.grid(row=1, column=0,columnspan=2, pady=1)

# CLEAR
btnClear=Button(MainFrame, width=13, height=2, font=('arial', 16, 'bold'), bd=4, text=chr(67),
bg='darkcyan', command= added_value.all_Clear_Entry)
# chr(67) itu diambil dari tabel karakter unicode
# posisi buttonnya
btnClear.grid(row =1, column=2, columnspan=2, pady=1)

#=============================================Scientific=====================================================#

btnAdd = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="+", bg='darkcyan',
command = lambda:added_value.opration("add"))
# posisi buttonnya
btnAdd.grid(row=3, column=3, pady=1)

btnSub = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="-", bg='darkcyan',
command = lambda:added_value.opration("sub"))
# posisi buttonnya
btnSub.grid(row=4, column=3, pady=1)

btnMult = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="x", bg='darkcyan',
command = lambda:added_value.opration("multi"))
# posisi buttonnya
btnMult.grid(row=5, column=3, pady=1)

btnDiv = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=chr(247), bg='darkcyan',
command = lambda:added_value.opration("divide"))
# posisi buttonnya
btnDiv.grid(row=6, column=3, pady=1)

btnZero = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="0", bg='darkcyan',
command = lambda:added_value.numberEnter(0))
# posisi buttonnya
btnZero.grid(row=6, column=0, pady=1)

btnDot = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=".", bg='darkcyan', 
command = lambda:added_value.numberEnter("."))
# posisi buttonnya
btnDot.grid(row=6, column=1, pady=1)

btnEquals = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="=", bg='darkcyan',
command = added_value.sum_of_total)
# posisi buttonnya
btnEquals.grid(row=6, column=2, pady=1)

#===========================================================================================================#

root.mainloop()


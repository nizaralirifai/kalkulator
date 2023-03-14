import tkinter
from tkinter import *

#membuat GUI (interface kontaknya)
root=Tk()
root.title("Kalkulatorku App")
root.geometry("570x600+100+200")
root.resizable(False,False)
#root.configure()(bg="#171616")
root["bg"] = "#171616"
#inisialisasi variabel global equation dengan nilai awal kosong
equation = ""

#fungsi untuk menambahkan karakter ke dalam equation
def show(value):
    global equation
    if value in ["+", "-", "*", "/"]:
        if len(equation) < 1:
            return
    equation+=value
    label_result.config(text=equation)

#fungsi untuk membersihkan semua karakter
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def deleteone():
    global equation
    # delete=equation-value
    equation= equation[:-1]
    label_result.config(text=equation)

#fungsi untuk mengevaluasi equation dan menampilkan hasilnya
def calculate():
    global equation
    result="" 
    if equation !="":
        try:
            # fungsi eval untuk menyelesaikan operasi matematika pada bilangan bulat atau float, bahkan dalam bentuk stringnya
            result= eval(equation)
            result= round(result,5)
        except ZeroDivisionError:
            result = "error"
            equation = ""
            print("Data yang anda masukkan salah")
    label_result.config(text=result)

#label untuk menampilkan equation 
label_result = Label(root,width=25,height=2,text="", font=("arial",30))
label_result.pack()

#tombol-tombol untuk operator
Button(root, text="C", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#D14343", command=lambda:clear()).place(x=10,y=100)
Button(root, text="←", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#D14343", command=lambda:deleteone()).place(x=150,y=100)
Button(root, text="/", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#51545E", command=lambda:show("/")).place(x=290,y=100)
Button(root, text="*", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#51545E", command=lambda:show("*")).place(x=430,y=100)

Button(root, text="7", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#111111", command=lambda:show("7")).place(x=10,y=200)
Button(root, text="5", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#111111", command=lambda:show("5")).place(x=150,y=200)
Button(root, text="9", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#111111", command=lambda:show("9")).place(x=290,y=200)
Button(root, text="-", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#51545E", command=lambda:show("-")).place(x=430,y=200)

Button(root, text="4", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#111111", command=lambda:show("4")).place(x=10,y=300)
Button(root, text="5", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#111111", command=lambda:show("5")).place(x=150,y=300)
Button(root, text="6", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#111111", command=lambda:show("6")).place(x=290,y=300)
Button(root, text="+", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#51545E", command=lambda:show("+")).place(x=430,y=300)

Button(root, text="1", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#111111", command=lambda:show("1")).place(x=10,y=400)
Button(root, text="2", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#111111", command=lambda:show("2")).place(x=150,y=400)
Button(root, text="3", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#111111", command=lambda:show("3")).place(x=290,y=400)
Button(root, text="0", width=11, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#111111", command=lambda:show("0")).place(x=10,y=500)

Button(root, text=".", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#51545E", command=lambda:show(".")).place(x=290,y=500)
Button(root, text="=", width=5, height=3, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#51545E", command=lambda:calculate()).place(x=430,y=400)

root.mainloop()
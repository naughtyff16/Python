from tkinter import*
from tkinter import messagebox
def dialog1():
    username=entry1.get()
    password=entry2.get()
    if (username=='karthi' and password=='harishini'):
     messagebox.showinfo('info','welcome')
    else:
        messagebox.showinfo('info','invalid username and password')
window=Tk()
window.title('Login form with username and password')
frame=Frame(window)
Label1=Label(window,text="username:",bg='yellow',fg='red')
Label1.pack(padx=15,pady=7)
entry1=Entry(window,bd=5)
entry1.pack(padx=15,pady=8)
Label2=Label(window,text='password:',bg='red',fg='blue')
Label2.pack(padx=15,pady=6)
entry2=Entry(window,bd=5)
entry2.pack(padx=15,pady=8)
btn=Button(frame,text='login',command=dialog1)
btn.pack(side=RIGHT,padx=5)
frame.pack(padx=100,pady=18)
window.mainloop()
from tkinter import *
window=Tk()
window.title('Simple Interest Calculator')
window.geometry('650x500')
window.configure(bg='teal')

def calculate_interest():
    p=float(principle_entry.get())
    r=float(rate_entry.get())
    t=float(time_entry.get())
    i=(p*r*t)/100
    interest=round(i,1)
    
    result_label.destroy()
   
    output_msg=Label(result_frame,text='Interest on Rs. '+str(p)+ ' at the rate of interest '+str(r)+' for '+str(t)+' years is Rs.'+str(interest),bg='lavender',font=('Calibri',12),width=55)
    output_msg.place(x=20,y=40)
    output_msg.pack()

app_label=Label(window,text='Simple Interest Calculator',bg='burlywood',fg='black',font=('Calibri',20),bd=5)
app_label.place(x=50,y=20)

principle_label=Label(window,text='enter principle(Rs)',fg='black',bg='burlywood',font=('Calibri',12),bd=1)
principle_label.place(x=20,y=90)
principle_entry=Entry(window,text='',bd=2,width=15)
principle_entry.place(x=150,y=92)

rate_label=Label(window,text='enter rate(/m)',fg='black',bg='burlywood',font=('Calibri',12),bd=1)
rate_label.place(x=20,y=140)
rate_entry=Entry(window,text='',bd=2,width=15)
rate_entry.place(x=150,y=142)

time_label=Label(window,text='enter time(years)',fg='black',bg='burlywood',font=('Calibri',12),bd=1)
time_label.place(x=20,y=185)
time_entry=Entry(window,text='',bd=2,width=15)
time_entry.place(x=150,y=187)

cal_button=Button(window,text='calculate',fg='black',bg='burlywood',bd=4,command=calculate_interest)
cal_button.place(x=20,y=250)

result_frame=LabelFrame(window,text='Result',bg='burlywood',font=('Calibri',12))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=300)
result_label=Label(result_frame,text='',bg='burlywood',font=('Calibri',12),width=33)
result_label.place(x=20,y=20)
result_label.pack()
window.mainloop()


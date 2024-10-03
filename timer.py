import time
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("390x390")

window.title("Timer Countdown")

hours = StringVar()
minutes = StringVar()
seconds = StringVar()

def timer():
    try:
        temp = int(hours.get())* 3600 + int(minutes.get()) * 60 + int(seconds.get())
    except:
        print("Please input a correct value")
    while temp > -1:
        m,s = divmod(temp,60)
        h = 00 
        if m > 60:
            h,m = divmod(m,60)
        hours.set("{00:2d}".format(h))
        minutes.set("{00:2d}".format(m))
        seconds.set("{00:2d}".format(s))
        window.update()
        time.sleep(1)
        if temp == 00:
            messagebox.showinfo("Times Up!!!", "Times Up!!!")
        temp = temp - 1
        
        
        
#setting the default values
hours.set("00")
minutes.set("00")
seconds.set("00")


hrs = Entry(window,width = 3,font=("Arial",30,""),textvariable = hours)
mins = Entry(window,width = 3,font=("Arial",30,""),textvariable = minutes)
secs = Entry(window,width = 3,font=("Arial",30,""),textvariable = seconds)

time_activate = Button(window,text = "Set the timer",bd = "5",command = timer, font =("Arial",30,""))

hrs.place(x = 80, y = 20)
mins.place(x = 180, y = 20)
secs.place(x = 280, y = 20)

time_activate.place(x = 70, y = 170 )
window.mainloop()
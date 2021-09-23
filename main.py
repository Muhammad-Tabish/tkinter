from tkinter import *

window = Tk()
window.title("Result App")
window.geometry("750x450")



text=Entry(window, width=20)
text.grid(row=0, column=3)

l1=Label(window, text="Name", font=15)
l1.grid(row=0, column=0)

def result():

    if text1 > 0 and text1 < 50:
        print('f')
    elif text1 > 50 and tex1 < 100:
        print('pass')
    else:
        print('marks should be correct')

text1=Entry(window,float, width=20,command= result() )
text1.grid(row=1, column=3)



l2=Label(window, text="Grades", font=15)
l2.grid(row=1, column=0)


def average_grade():
    res = "welcome to  " +text.get()
    l1.configure(text=res)





print(average_grade)

btn=Button(window, text= 'result', fg='black', command=average_grade)
btn.grid(row=4, column=3)




window.mainloop()
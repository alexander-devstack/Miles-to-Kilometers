from tkinter import  *

from numpy.ma.core import size
def miles_to_km():
    ans=float(input.get())*1.60934
    output.config(text=ans)

#window
window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=150, pady=90)

#input
input=Entry(width=10)
input.grid(column=4, row=0)
n=input.get()

#output
output=Label(text=0)
output.grid(column=4, row=1)

#button
button=Button(text="Calculate", command=miles_to_km)
button.grid(column=4, row=2)

#Labels
miles=Label(text="Miles")
miles.grid(column=6, row=0)

km=Label(text="Km")
km.grid(column=6, row=1)

equal=Label(text="is equal to")
equal.grid(column=2, row=1)




window.mainloop()
import tkinter as tk
from main import GetImages,Recognise,RemoveMultipleEnteries
from train import Train

def show_entry_fields():
    GetImages(e1.get(), int(e2.get()))


master = tk.Tk()
tk.Label(master, text="Name").grid(row=0)
tk.Label(master, text="Roll No").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
# e1.insert(10, "Miller")
# e2.insert(10, "Jill")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text='Collect Data', command=show_entry_fields).grid(row=3, 
                                                               column=0, 
                                                               sticky=tk.W, 
                                                               pady=4)
tk.Button(master, text='Recognise', command=Recognise).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)
                                                               
tk.Button(master, text='Train', command=Train).grid(row=3, 
                                                               column=2, 
                                                               sticky=tk.W, 
                                                               pady=4)

                                                               
tk.Button(master, text='Sort Attendance', command=RemoveMultipleEnteries).grid(row=3, 
                                                               column=3, 
                                                               sticky=tk.W, 
                                                               pady=4)


master.mainloop()

tk.mainloop()

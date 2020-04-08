import tkinter as tk
from main import Recognise,Capture,Train,Sort

def show_entry_fields():
    Capture(e2.get(), e1.get())


master = tk.Tk()
tk.Label(master, text="Name").grid(row=0)
tk.Label(master, text="Roll No").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, 
          text='Capture', 
          command=show_entry_fields).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, text='Train', command=Train).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)

tk.Button(master, 
          text='Recognise', 
          command=Recognise).grid(row=3, 
                                    column=2, 
                                    sticky=tk.W, 
                                    pady=4)


tk.Button(master, 
          text='Sort Attendance', 
          command=Sort).grid(row=3, 
                                    column=3, 
                                    sticky=tk.W, 
                                    pady=4)


master.mainloop()

tk.mainloop()

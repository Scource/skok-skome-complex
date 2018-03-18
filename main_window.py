import tkinter as tk
from tkinter import ttk



class main_window:

    def __init__(self, master):
        self.master=master
        master.title("jakis tam tkst")
        master.geometry("400x400")
   

        self.main_nb=ttk.Notebook(self.master)
        self.main_nb.pack(fill='both', expand=True)


        #main frame widegets
        self.frame_main=ttk.Frame(self.main_nb)
        self.button_1=tk.Button(self.frame_main,text="asd")
        self.button_1.pack()
        self.button_2=tk.Button(self.frame_main,text="asdsdfsdf")
        self.button_2.pack()
        #self.datepicker=datepicker(self.frame_main)
        #self.datepicker.pack()


        #CSB frame widegets /Centralny system bilingowy
        self.frame_CSB=ttk.Frame(self.main_nb)
        self.button_3=tk.Button(self.frame_CSB,text="asd")
        self.button_3.grid(column=0, row=0)
        self.button_4=tk.Button(self.frame_CSB,text="asdsdfsdf")
        self.button_4.grid(column=1, row=1)


        #CSPR frame widegets /Centralny system pomiarowo-rozliczeniowy
        self.frame_CSPR=ttk.Frame(self.main_nb)
        self.button_3=tk.Button(self.frame_CSPR,text="asd")
        self.button_3.grid(column=0, row=0)
        self.button_4=tk.Button(self.frame_CSPR,text="asdsdfsdf")
        self.button_4.grid(column=1, row=1)       


        #Data_enetry frame widegets
        self.frame_data_entry=ttk.Frame(self.main_nb)
        self.button_3=tk.Button(self.frame_data_entry,text="asd")
        self.button_3.grid(column=0, row=0)
        self.button_4=tk.Button(self.frame_data_entry,text="asdsdfsdf")
        self.button_4.grid(column=1, row=1)  



        self.main_nb.add(self.frame_main, text="Main Window")
        self.main_nb.add(self.frame_CSB, text="CSB Data")
        self.main_nb.add(self.frame_CSPR, text="CSPR Data")
        self.main_nb.add(self.frame_data_entry, text="Addidtional Data")
        self.main_nb.pack()




        
if __name__ == '__main__':
    root = tk.Tk()
    my_gui = main_window(root)
    root.mainloop()


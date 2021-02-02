
import wmi
import psutil

try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *




    



class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        

        

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('starttime', 'endtime', 'status','ok','lsa')
        tv.heading("#0", text='    PID', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('starttime', text='Parent ID')
        tv.column('starttime', anchor='center', stretch=NO)
        tv.heading('endtime', text='Owner')
        tv.column('endtime', anchor='center', stretch=NO)
        tv.heading('status', text='Process name')
        tv.column('status', anchor='center', stretch=NO)
        tv.heading('ok', text='Start time')
        tv.column('ok', anchor='center', stretch=NO)
        tv.heading('lsa', text='Virtual size')
        tv.column('lsa', anchor='center',stretch=NO)
        tv.grid(sticky = (N,S,W,E))
        tv.grid_rowconfigure(0, weight = 1)
        tv.grid_columnconfigure(0, weight = 1)
        scroll_y = Scrollbar(self, orient="vertical", command=tv.yview)
        scroll_y.grid(row=0, column=1, sticky="ns")
        tv.configure(yscrollcommand=scroll_y.set)
        tv.grid_rowconfigure(0, weight = 1)
        tv.grid_columnconfigure(0, weight = 1)
        
        self.treeview = tv
       

    def LoadTable(self):
        c=wmi.WMI()
        try:
            for process in c.Win32_Process():
                self.treeview.insert('', 'end', text=process.ProcessID, values=(process.ParentProcessId,
                             psutil.Process(process.ProcessId).username(),process.Name,process.CreationDate,process.VirtualSize))
        except:
            pass


root = Tk()
App(root)
root.mainloop()

   
    

    
    



    
   

    

    
  
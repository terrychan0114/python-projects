from tkinter import *
import time
from threading import *
  
# Create Object
root = Tk()
  
# Set geometry
root.geometry("400x400")

def threading():
    t1=Thread(target=work)
    t1.start()
  
def work():
  
    print("sleep time start")
  
    for i in range(10):
        print(i)
        time.sleep(1)
  
    print("sleep time stop")
  
  
# Create Button
Button(root, text="Click Me", command=threading).pack()
  
# Execute Tkinter
root.mainloop()
from tkinter import*

root=Tk()
root.geometry("600x600")


list_name = ["Levi" , "Mikasa" , "Armin" , "Erwin"]
dict_name = {"name" : "Eren" , "Age" : "19"}


try:
    print(list_name[38])
    
    print(dict_name["I'm Gonna Destroy Them! Every Last One Of Those Animals That's On This Earth!"])
    
    
except IndexError:
    messagebox.showinfo("Error","This Index does not exist")
except KeyError:
    messagebox.showinfo("Error","This Key does not exist")    
    
root.mainloop()
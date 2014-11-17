import tkinter as tk
#basically the tkinter CSS
from tkinter import ttk
import brailleConversion



#define a font
LARGE_FONT = ("Verdana", 12)

class printGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # choose an icon for the window
        tk.Tk.iconbitmap(self, default="ainp.ico")
        tk.Tk.wm_title(self, "Braille Printing")
        
       
        #Set up the container
        container = tk.Frame(self)
        #if fill space and can expand past that
        container.pack(side="top", fill="both", expand= True)
        # min, priority
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #contains all the frames, top frame is interacted on
        self.frames = {}
        
        for i in (startPage, PageOne, PageTwo):      
            #start the initial frame
            frame = i(container, self)
            self.frames[i] = frame
            #instead of pack, north south east west
            frame.grid(row=0, column=0, sticky="nsew")
            
        #display it
        self.show_frame(startPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        #raises the frame to the front
        frame.tkraise()
        
def qf(param):
    #call the text printer on param
    param = param.lower()
    test = brailleConversion.brailleConverter(param)
    brailleConversion.printFormat(test.getCellList())    
    
class startPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text= "Braille Printer - Input Printing", font=LARGE_FONT)
        #pack to add rather than the grid as small. padding
        label.pack(pady=10, padx=10)
        
        frame = tk.Frame(self, height=150, width=1000)
        frame.pack()
        
        eLab = tk.Label(self, font=LARGE_FONT, padx=10, 
                        text="Enter the text to be converted: ",
                        justify= tk.LEFT)
        eLab.pack()

        entry = tk.Entry(self, bd = 5, font=LARGE_FONT, width= 75)
        entry.pack()
        
        frame2 = tk.Frame(self, height=150, width=1000)
        frame2.pack()        
        #calling the function on button call
        button1 = ttk.Button(self, text="Print the Text", 
                            command = lambda: qf(entry.get()))
        
        button2 = ttk.Button(self, text="File Printer", 
                                    command = lambda: controller.show_frame(PageOne))        
        #pack the button
        button1.pack()
        button2.pack(side = tk.RIGHT)

def fileqf(param):
    brailleConversion.filePrint(param)
    #call the file printer for param
        
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text= "Braille Printer - File Printing", font=LARGE_FONT)
        #pack to add rather than the grid as small. padding
        label.pack(pady=10, padx=10)
        
        frame = tk.Frame(self, height=150, width=800)
        frame.pack()
        
        eLab = tk.Label(self, font=LARGE_FONT, padx=10, 
                        text="Enter file to print: ",
                        justify= tk.LEFT)
        eLab.pack()

        entry = tk.Entry(self, bd = 5, font=LARGE_FONT, width= 75)
        entry.pack()
        
        frame2 = tk.Frame(self, height=150, width=800)
        frame2.pack()  
        
        button1 = ttk.Button(self, text="Print the File",
                                                    command = lambda: fileqf(entry.get()))        
        
        
        button2 = ttk.Button(self, text="Back to input Printing",
                                            command = lambda: controller.show_frame(startPage))        
        button1.pack()
        button2.pack(side = tk.RIGHT)
        

class PageTwo(tk.Frame):  
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text= "Page 2", font=LARGE_FONT)
        #pack to add rather than the grid as small. padding
        label.pack(pady=10, padx=10)
        
        frame = tk.Frame(self, height=300, width=800)
        frame.pack()        
        
        button1 = ttk.Button(self, text="To Page 1", 
                                            command = lambda: controller.show_frame(PageOne))
        
        
        button2 = ttk.Button(self, text="Back to Home", 
                                            command = lambda: controller.show_frame(startPage))        
        button1.pack()
        button2.pack()
        



app = printGUI()

def donothing():
    print("nothing")
   
menubar = tk.Menu(app)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=app.destroy)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

app.config(menu=menubar)

app.mainloop()
        
        
        

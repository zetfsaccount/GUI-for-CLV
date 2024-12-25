# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 14:03:29 2022

@author: win10
"""

import tkinter as tk
import tkinter.font as tkFont
import os
from tkinter import ttk
from tkinter import filedialog as fd






class App:
    def __init__(self,root):
        #arrangementwindow
        root.title("Customer Segmentation")
        width=750
        height=500
        screenwidth=root.winfo_screenwidth()
        screenheight=root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        
        
        # ====================================
        # =========== START OF UI ============
        # This is for the Lines =======================
        
        #Brows File Button
        self.browseFile_button = tk.Button(root, text = "Browse File")
        self.browseFile_button.place(x = 150, y = 90)
        
        #TabDefinition
        tabControl = ttk.Notebook(root)
  
        self.tabML = ttk.Frame(tabControl)
        self.tabRFM = ttk.Frame(tabControl)
        self.tabARIMA = ttk.Frame(tabControl)
   
        tabControl.add( self.tabML, text ='ML')
        tabControl.add( self.tabRFM, text ='RFM')
        tabControl.add( self.tabARIMA, text ='ARIMA')
       
        tabControl.pack(expand = 1, fill ="both")
        
        """ canvas=tk.Canvas(root, width=750, height=350)
        # Lines for select file
        canvas.create_line(65, 15, 740, 15, fill="black", width=1)
        canvas.create_line(740, 15, 740, 175, fill="black", width=1)
        canvas.create_line(740, 175, 18, 175, fill="black", width=1)
        canvas.create_line(18, 175, 18, 15, fill="black", width=1)
        
        # Lines for Customer Segmentation
        canvas.create_line(85, 190, 740, 190, fill="black", width=1)
        canvas.create_line(740, 190, 740, 340, fill="black", width=1)
        canvas.create_line(740, 340, 18, 340, fill="black", width=1)
        canvas.create_line(18, 340, 18, 190, fill="black", width=1)
        
        canvas.pack(expand = 1, fill ="both")"""
       
        
        ###### Tab ML #####
        # Labels
        ttk.Label(self.tabML, 
          text ="!WARNING!\n Dataset must include:\n   *CustomerID \n   *InvoiceDate \n   *Quantity\n   *Price\n   *Invoice", font=("Arial", 12)).place(x = 400, y = 50)
        ttk.Label(self.tabML, text = "Select File", font=("Arial", 10)).place(x=10, y=30)
        ttk.Label(self.tabML, text = "Please \nLoad a Dataset:", font=("Arial", 10)).place(x = 25, y = 90)
        ttk.Label(self.tabML, text = "Customer Lifetime Value Machine Learning Algorithms------------------------------------------------------------------------------------------------------", font=("Arial", 10)).place(x=10, y=200)
        ttk.Label(self.tabML, text = "Please Choose an Algorithm:", font=("Arial", 10)).place(x=30, y=250)
        ttk.Label(self.tabML, text = "Please Choose How Many Days\nAhead to Predict CLV:", font=("Arial", 10)).place(x=400, y=250)
        #Algorithm Choice Buttons
        var=tk.IntVar()
        self.RF = ttk.Radiobutton(self.tabML, text="Random Forest", variable=var, value=1).place(x=30, y=300)
        self.LR =ttk.Radiobutton(self.tabML, text="Linear Regression", variable=var, value=2).place(x=30, y=320)
        self.NN = ttk.Radiobutton(self.tabML, text="Neural Network", variable=var, value=3).place(x=30, y=340)
        #CLV Choice Buttons
        varCLV=tk.IntVar()
        self.CLV30 = ttk.Radiobutton(self.tabML, text="30", variable=varCLV, value=1).place(x=400, y=300)
        self.CLV60 =ttk.Radiobutton(self.tabML, text="60", variable=varCLV, value=2).place(x=400, y=320)
        self.CLV90 = ttk.Radiobutton(self.tabML, text="90", variable=varCLV, value=3).place(x=400, y=340)
        #SelectFileButton
        ttk.Button(self.tabML, text="Browse File",command=lambda:self.browseFile()).place(x=120, y=100)
        ttk.Button(self.tabML, text="Run").place(x=300, y=420)
        ttk.Button(self.tabML, text="Quit",command=lambda:self.quitApp()).place(x=400, y=420)
        tk.Button(root, text="Help",command=lambda:self.helpOpen()).place(x=710, y=20)
        
        
        ####### Tab RFM #####
        
        # Labels
        ttk.Label(self.tabRFM, 
            text="RFM Window",font=("Arial", 12)).place(x = 335, y = 15)
        ttk.Label(self.tabRFM, 
          text ="!WARNING!\n Dataset must include:\n   *CustomerID \n   *InvoiceDate \n   *Quantity\n   *Price\n   *Invoice", font=("Arial", 12)).place(x = 80, y = 50)
        ttk.Label(self.tabRFM, text = "Please \nLoad a Dataset:", font=("Arial", 10)).place(x = 300, y = 290)
       
        #SelectFileButton
        ttk.Button(self.tabRFM, text="Browse File",command=lambda:self.browseFile()).place(x=410, y=300)
        ttk.Button(self.tabRFM, text="Run").place(x=300, y=420)
        ttk.Button(self.tabRFM, text="Quit",command=lambda:self.quitApp()).place(x=400, y=420)

       
        
        # Tab ARIMA
        ttk.Label(self.tabARIMA, 
            text="ARIMA Window",font=("Arial", 12)).place(x = 335, y = 15)
        tk.Label(self.tabARIMA,
            text ="!WARNING!\n Dataset must include:\n   *CustomerID \n   *InvoiceDate \n   *Quantity\n   *Price\n   *Invoice", font=("Arial", 12)).place(x = 80, y = 50)
        ttk.Label(self.tabARIMA, text = "Please \nLoad a Dataset:", font=("Arial", 10)).place(x = 300, y = 290)
       
        #SelectFileButton
        ttk.Button(self.tabARIMA, text="Browse File",command=lambda:self.browseFile()).place(x=410, y=300)
        ttk.Button(self.tabARIMA, text="Run").place(x=300, y=420)
        ttk.Button(self.tabARIMA, text="Quit",command=lambda:self.quitApp()).place(x=400, y=420)
        
        
        # Tab HELP

      
        
        
    def helpOpen(self):
        window=tk.Tk()
        window.title("Help")
    def quitApp(self):
        root.destroy()
    def browseFile(self):
        #filetypes = (('excel files', '*.csv'),)
        filetypes=[('excel', '.xlsx'),('csv', '.csv')]
       
        filename = fd.askopenfilename(
        title='Open a file', initialdir='/', filetypes=filetypes)
  
        
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__=="__main__":
    root=tk.Tk()
    app=App(root)
    root.mainloop()
    
        
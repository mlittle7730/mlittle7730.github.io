"""
============================================================================
Name        : VectorSorting.cpp
Author      : Miguel Little
Date        : 08/19/24
Version     : 4.0
Copyright   : Copyright © 2017 SNHU COCE
Description : Python Gov Bid Sorting Application

Intent      : This class was created to handle the creation of the GUI,
              and to run the proper functions when each option is selected.

============================================================================

"""

import tkinter as tk
from tkinter import ttk
from data import Data
import re

class GUI:
    def __init__(self):
        self.data = Data()
        self.root = tk.Tk()
        self.root.title('Government Bids')
        #self.root.option_add("*tearOff", False)

        
        # Create a Style object to manage themes
        self.style = ttk.Style()
        self.style.theme_use('clam')
        columns = ("Bid ID", "Title", "Amount", "Closing Date", "Funds")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        #Configure column headings
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        self.selected_option = tk.StringVar(value='You need to make a selection')


        options = ['Load Bids', 'Load From DB', 'Sort by Title',
           'Sort by Amount', 'Insert a New Bid', 'Sort by Closing Dates', 'Bubble Sort by Title']
        
        radio_frame = tk.Frame(self.root, width = 350, height = 250)
        radio_frame['relief'] = 'sunken'
        radio_frame['borderwidth'] = 2
        
        # Create Radiobuttons for each option
        for option in options:
            radio_button = tk.Radiobutton(radio_frame, text=option, variable=self.selected_option, value=option, command=self.on_select)
            radio_button.pack()
    
        # Create a label to display the selected option
        self.result_label = tk.Label(radio_frame, text=f"You selected: {self.selected_option.get()}")
        self.result_label.pack()

        # Create a button that is initially disabled
        self.submit_button = tk.Button(radio_frame, text="Submit", state='disabled', command=self.on_button_click, bg='black', fg='white')
        self.submit_button.pack()
        
        #Create time label for timing display
        self.time_label = tk.Label(radio_frame, text="")
        self.time_label.pack()
        
        radio_frame.pack_propagate(False)
        radio_frame.pack()
        
        #Creating seperate frame for input fields
        entry_frame = tk.Frame(self.root, width = 300, height = 250)
        entry_frame['relief'] = 'sunken'
        entry_frame['borderwidth'] = 2
        self.entry_frame = entry_frame
        
        bidID = tk.Label(entry_frame, text='Enter Bid ID:')
        bidID.pack()
        
        
        
        # Create an Entry widget for user input
        self.bidEntry = tk.Entry(entry_frame)
        self.bidEntry.pack()
        
        #Get user input
        # Create a label for the Entry widget
        titleLabel = tk.Label(entry_frame, text='Enter the Title:')
        titleLabel.pack()
        
        # Create an Entry widget for user input
        self.titleEntry = tk.Entry(entry_frame)
        self.titleEntry.pack()
        
        #Get user input
        # Create a label for the Entry widget
        amountLabel = tk.Label(entry_frame, text='Enter the Amount:')
        amountLabel.pack()
        
        # Create an Entry widget for user input
        self.amountEntry = tk.Entry(entry_frame)
        self.amountEntry.pack()
        
        #Get user input
        # Create a label for the Entry widget
        closingDateLabel = tk.Label(entry_frame, text='Enter the closing date:')
        closingDateLabel.pack()
        
        # Create an Entry widget for user input
        self.closingDateEntry = tk.Entry(entry_frame)
        self.closingDateEntry.pack()
        
        #Get user input
        # Create a label for the Entry widget
        fundLabel = tk.Label(entry_frame, text='Pick the Fund:')
        fundLabel.pack()
        
        # Create an Entry widget for user input
        self.fundSource = ttk.Combobox(entry_frame, state='readonly')
        self.fundSource['values'] = ('Enterprise', 'General Fund')
        self.fundSource.pack()
        
        # Create a button that will submit the input when clicked
        self.entry_button = tk.Button(entry_frame, text='Submit', command=self.submit_input, bg='black', fg='white')
        self.entry_button.pack()
        
        #The entry fields won't be visible unless "Insert a New Bid is selected"
        entry_frame.pack_propagate(False)
        entry_frame.pack()
        entry_frame.pack_forget()
        
        self.root.mainloop()
        
    ###### ENSURING ERROR HANDLING AND BASIC SECURITY #######
    #This provides basic security so the user cant execute SQL commands to the database
        
    #Checking that the Article ID is a digit or throwing exception
    def get_bidEntry(self):
        bid = self.bidEntry.get()
        if bid.isdigit():
            return bid
        raise ValueError('Article ID is not valid')
        
    #Checking that the title is not NULL or throwing exception
    def get_titleEntry(self):
        title = self.titleEntry.get()
        if len(title)>0:
            return title
        raise ValueError('Article Title is empty')
        
    #Checking that the amount entered for the bid amount is a REAL number or throwing exception
    def get_amountEntry(self):
        amount = self.amountEntry.get()
        if re.match(r"\d+\.*\d*", amount):
            return amount
        raise ValueError('Bid must be a REAL number')
        
    #Checking the formatting of the date entry or throwing exception
    def get_closingDateEntry(self):
        closingDate = self.closingDateEntry.get()
        if re.match(r"^[0,1]?\d{1}\/(([0-2]?\d{1})|([3][0,1]{1}))\/(([1]{1}[9]{1}[9]{1}\d{1})|([2-9]{1}\d{3}))$", closingDate):
            return closingDate
        raise ValueError('Closing date format incorrect e.g. MM/DD/YYYY')
    
    #user bid input handler
    def submit_input(self):
        
        try:
            bid = {}
            bid['bid'] = self.get_bidEntry()
            bid['title'] = self.get_titleEntry()
            bid['amount'] = self.get_amountEntry()
            bid['closingDate'] = self.get_closingDateEntry()
            bid['fund'] = self.fundSource.get()
            
            self.data.submit_input(bid)
            self.load_dataframe_into_treeview()
            self.clear_input()
            #entry input fields hide after input is submitted
            self.entry_frame.pack_forget()
            return True
        #Returns exception if Article ID is not UNIQUE
        except Exception as EE:
            tk.messagebox.showerror( "Error", f"{EE}")
            return False
    
    #Clearing inputs after the user submits a new entry into the database
    def clear_input(self):
        self.bidEntry.delete(0,'end')
        self.titleEntry.delete(0,'end')
        self.amountEntry.delete(0,'end')
        self.closingDateEntry.delete(0,'end')
        self.fundSource.delete(0,'end')
    
    #Each button click and what they call
    def on_button_click(self):
        
        selected = self.selected_option.get()
                
        if selected == 'Load Bids':
            self.data.df = self.data.load_bids()
        elif selected == 'Sort by Title':
            message = self.data.sort_by_title()
            self.time_label.config(text=message)
        elif selected == 'Sort by Amount':
            message = self.data.sort_by_amount()
            self.time_label.config(text=message)
        elif selected == 'Bubble Sort by Title':
            message = self.data.custom_sort_title()
            self.time_label.config(text=message)
        elif selected == 'Insert a New Bid':
            self.insert_bid()
        elif selected == 'Sort by Closing Dates':
            message = self.data.sort_by_closing_date()
            self.time_label.config(text=message)
        elif selected == 'Load From DB':
            self.data.load_from_db(self)
            # Perform an action with the selected option (e.g., print it)
            self.load_dataframe_into_treeview()
            
        print(f"You clicked the button after selecting: {selected}")
    
    #this function decides which function to run based on user selection
    def on_select(self):
        print(f'You selected: {self.selected_option.get()}')
        self.submit_button.config(state='normal')
        self.result_label.config(text=f"You selected: {self.selected_option.get()}")
    
        
    #this function is used to update the gui with all the bids
    def load_dataframe_into_treeview(self):
    # Clear the Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        # Insert data into the Treeview
        for idx, row in self.data.df.iterrows():
            # Convert row to tuple
            values = tuple(row)
            # Insert the row into the Treeview
            self.tree.insert('', 'end', values=values)
        
    def insert_bid(self):
        
        self.entry_frame.pack()
    
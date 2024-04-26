import tkinter as tk
from tkinter import ttk
from data import Data

class GUI:
    def __init__(self):
        self.data = Data()
        self.root = tk.Tk()
        self.root.title('Bids')
        
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


        options = ['Load Bids', 'Sort by Title',
           'Sort by Amount', 'Insert a New Bid', 'Sort by Closing Dates', 'Load From DB']

        # Create Radiobuttons for each option
        for option in options:
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=option, command=self.on_select)
            radio_button.pack(anchor='w')
    
        # Create a label to display the selected option
        self.result_label = tk.Label(self.root, text=f"You selected: {self.selected_option.get()}")
        self.result_label.pack()

        # Create a button that is initially disabled
        self.submit_button = tk.Button(self.root, text="Submit", state='disabled', command=self.on_button_click)
        self.submit_button.pack()
        
        
        bidID = tk.Label(self.root, text='Enter Bid ID:')
        bidID.pack()
        
        # Create an Entry widget for user input
        self.bidEntry = tk.Entry(self.root)
        self.bidEntry.pack()
        
        #Get user input
        # Create a label for the Entry widget
        titleLabel = tk.Label(self.root, text='Enter the Title:')
        titleLabel.pack()
        
        # Create an Entry widget for user input
        self.titleEntry = tk.Entry(self.root)
        self.titleEntry.pack()
        
        #Get user input
        # Create a label for the Entry widget
        amountLabel = tk.Label(self.root, text='Enter the Amount:')
        amountLabel.pack()
        
        # Create an Entry widget for user input
        self.amountEntry = tk.Entry(self.root)
        self.amountEntry.pack()
        
        #Get user input
        # Create a label for the Entry widget
        closingDateLabel = tk.Label(self.root, text='Enter the closing date:')
        closingDateLabel.pack()
        
        # Create an Entry widget for user input
        self.closingDateEntry = tk.Entry(self.root)
        self.closingDateEntry.pack()
        
        #Get user input
        # Create a label for the Entry widget
        fundLabel = tk.Label(self.root, text='Enter the Fund:')
        fundLabel.pack()
        
        # Create an Entry widget for user input
        self.fundEntry = tk.Entry(self.root)
        self.fundEntry.pack()
        
        # Create a button that will submit the input when clicked
        self.entry_button = tk.Button(self.root, text='Submit', command=self.submit_input)
        self.entry_button.pack()
        
        self.root.mainloop()
        
        
    def submit_input(self):
        self.data.submit_input(self)
        self.load_dataframe_into_treeview()
        
    def on_button_click(self):
        selected = self.selected_option.get()
        if selected == 'Load Bids':
            self.data.df = self.data.load_bids()
        elif selected == 'Sort by Title':
            self.data.sort_by_title()
        elif selected == 'Sort by Amount':
            self.data.sort_by_amount()
        elif selected == 'Insert a New Bid':
            self.data.insert_bid()
        elif selected == 'Sort by Closing Dates':
            self.data.sort_by_closing_date()
        elif selected == 'Load From DB':
            self.data.load_from_db(self)
            # Perform an action with the selected option (e.g., print it)
        self.load_dataframe_into_treeview()
        print(f"You clicked the button after selecting: {selected}")
        
    def on_select(self):
        print(f'You selected: {self.selected_option.get()}')
        self.submit_button.config(state='normal')
        self.result_label.config(text=f"You selected: {self.selected_option.get()}")
        
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
    
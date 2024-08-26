"""
============================================================================
Name        : VectorSorting.cpp
Author      : Miguel Little
Date        : 08/19/24
Version     : 4.0
Copyright   : Copyright © 2017 SNHU COCE
Description : Python Gov Bid Sorting Application

Intent      : This class will handle each function selected from the GUI.
              This is where a database and time complexity is incorportated.
              The database functions have now been added as well.
              
Credits     : Big O scenarios were found using https://www.programiz.com/dsa/

============================================================================

"""


# IMPORT LIBRARIES #

import pandas as pd
import time
import sqlite3

# CREATE CLASS #

class Data:
    def __init__(self):
        self.df = pd.DataFrame(columns=["ArticleID", "ArticleTitle", "WinningBid ", "CloseDate ", "Fund"])
        db_path = "bids.db"  # Path to the SQLite database file
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        
        # Create the bids table if it doesn't exist
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bids (
            ArticleID TEXT PRIMARY KEY UNIQUE NOT NULL,
            ArticleTitle TEXT NOT NULL,
            WinningBid REAL NOT NULL,
            CloseDate TEXT NOT NULL,
            Fund TEXT NOT NULL
        )
        """)
        #KeyID INTEGER PRIMARY KEY AUTOINCREMENT,
    
    #This loads the bids from the database and appends them to the current bids
    def load_from_db(self, gui):
        self.cursor.execute("SELECT * FROM bids")
        rows = self.cursor.fetchall()
        for row in rows:
            new_row = {col: value for col, value in zip(self.df.columns, row)}
            self.df.loc[len(self.df)] = new_row
        self.df['WinningBid '] = self.df['WinningBid '].astype(str)
    
    #This function loads data from a csv defined in filename
    def load_csv_data(self, filename):
        return pd.read_csv(filename)
    
    #grabs the data submitted by the user through the GUI and appends 
    #them to the dataframe and database
    def submit_input(self,bid):

        # Retrieve the input from the Entry widget
        # Process the user input as needed
        new_row = {
            'ArticleID':bid['bid'],
            'ArticleTitle':bid['title'],
            'WinningBid ':bid['amount'],
            'CloseDate ':bid['closingDate'],
            'Fund':bid['fund']}

        self.df.loc[len(self.df)] = new_row
        self.df['WinningBid '] = self.df['WinningBid '].astype(str) #fixes the sorting after 
        print(self.df.info()) #debugging purposes
        
        #SQL bid query entry
        ##################################################
        # Insert the new bid into the SQLite database
        
        self.cursor.execute("""
                            INSERT INTO bids (ArticleID, ArticleTitle, 
                            WinningBid, CloseDate, Fund) 
                            VALUES (?, ?, ?, ?, ?)""", (
                            bid['bid'], 
                            bid['title'], 
                            bid['amount'], 
                            bid['closingDate'], 
                            bid['fund']))
        
        # Commit the transaction
        self.conn.commit()
        ##################################################
                
        #gui.load_dataframe_into_treeview(df, tree)
    def load_bids(self):
        csv_df = self.load_csv_data("eBid_Monthly_Sales_Dec_2016.csv")
        csv_df = csv_df[["ArticleID", "ArticleTitle", "WinningBid ", "CloseDate ", "Fund"]]
        df_new = self.df._append(csv_df, ignore_index=True)
        self.df['WinningBid '] = self.df['WinningBid '].astype(str)
        return df_new
    
    #Heap sort time complexity
    #Heap Sort Best Case = O(nlog n) Average Case = O(nlog n) Worst Case = O(nlog n)
    #Heap Sort is the most efficient sorting algorithm used compared to Quick Sort and Bubble Sort
    def sort_by_title(self):
        start_time = time.time()
        self.df = self.df.sort_values(by="ArticleTitle", ascending=True, kind="heapsort")
        #load_dataframe_into_treeview(df, tree)
        end_time = time.time()
        duration = end_time - start_time
        return "Sort by title using Heap Sort took {:.4f} seconds to execute.".format(duration)
    
    #This function sorts by amount using quick sort.
    #Quick Sort Best Case = O(n*log n) Average Case = O(n*log n) Worst Case = O(n^2)
    #Quick Sort has an average case that is more efficient than Bubble Sort's average case
    def sort_by_amount(self):
        start_time = time.time() #starting timer
    # Clean the 'WinningBid' column
    # This verifies that it is a number
        try:
            self.df['WinningBid '] = self.df['WinningBid '].str.replace('$', '')  # Remove currency symbol
            self.df['WinningBid '] = self.df['WinningBid '].str.replace(',', '')  # Remove currency symbol
            #df['WinningBid '] = df['WinningBid '].str.replace('.', '')  # Remove currency symbol this was causing another bug of adding zeros because we need a decimal for float
            self.df['WinningBid '] = self.df['WinningBid '].str.strip()  # Remove leading and trailing whitespace
        except:
            
            print("already a number")
            
            
        print(self.df['WinningBid ']) #debugging purposes
        self.df['WinningBid '] = self.df['WinningBid '].astype(float)
        self.df = self.df.sort_values(by="WinningBid ", ascending=True)
        self.df['WinningBid '] = self.df['WinningBid '].astype(str)
        print(self.df['WinningBid ']) #debugging purposes
        end_time = time.time() #end timer
        duration = end_time - start_time
        return "Sort by amount using Quick Sort took {:.4f} seconds to execute.".format(duration) #returns time taken
        
    #Merge Sort Best Case = O(n*log n) Average Case = O(n*log n) Worst Case = O(n*log n)
    #Merge Sort is on par with Heap Sort, but the space complexity is higher
    def sort_by_closing_date(self):
        start_time = time.time()
        self.df['CloseDate '] = pd.to_datetime(self.df['CloseDate '])
        self.df = self.df.sort_values(by='CloseDate ',ascending=False, kind="mergesort")
        end_time = time.time()
        duration = end_time - start_time
        return "Sort by date using Merge Sort took {:.4f} seconds to execute.".format(duration)
    
    # Bubble Sort Best Case: O(n), Average Case: O(n^2), Worst Case:O(n^2)
    def custom_sort_title(self):
        start_time = time.time()
        #convert to a list of tuples
        data = [tuple(row) for row in self.df.values]
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j][1] > data[j+1][1]:  # Sort by the first column (Name in this case)
                    data[j], data[j+1] = data[j+1], data[j]
                    
        end_time = time.time()
        duration = end_time - start_time
        #reconstruct dataframe
        self.df = pd.DataFrame(data, columns=self.df.columns)
        return "Sort by title using Bubble Sort took {:.4f} seconds to execute.".format(duration)
        
        
    
    def insert_bid(self):
        print()
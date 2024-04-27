import pandas as pd
import time
import sqlite3

class Data:
    def __init__(self):
        self.df = pd.DataFrame(columns=["ArticleID", "ArticleTitle", "WinningBid ", "CloseDate ", "Fund"])
        db_path = "bids.db"  # Path to the SQLite database file
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        
        # Create the bids table if it doesn't exist
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bids (
            ArticleID TEXT PRIMARY KEY,
            ArticleTitle TEXT,
            WinningBid REAL,
            CloseDate TEXT,
            Fund TEXT
        )
        """)
        
    def load_from_db(self, gui):
        self.cursor.execute("SELECT * FROM bids")
        rows = self.cursor.fetchall()
        for row in rows:
            new_row = {col: value for col, value in zip(self.df.columns, row)}
            self.df.loc[len(self.df)] = new_row
        self.df['WinningBid '] = self.df['WinningBid '].astype(str)
        #print(rows)
        #gui.load_dataframe_into_treeview(self.df, tree)
        
    def load_csv_data(self, filename):
        return pd.read_csv(filename)
    
    def submit_input(self,gui):
        # Retrieve the input from the Entry widget
        #form = '%b %d %Y'
        bid = gui.bidEntry.get()
        title = gui.titleEntry.get()
        amount = gui.amountEntry.get()
        closingDate = gui.closingDateEntry.get()
        fund = gui.fundEntry.get()
        # Process the user input as needed
        # Here, we'll just print the input to the console
        #print(f"User input: {user_input}")
        new_row = {'ArticleID':bid, 'ArticleTitle':title, 'WinningBid ':amount, 
                                'CloseDate ':closingDate, 'Fund':fund}
        
        #df = pd.concat([df, new_row], ignore_index=False)
        self.df.loc[len(self.df)] = new_row
        self.df['WinningBid '] = self.df['WinningBid '].astype(str) #fixes the sorting after 
        print(self.df.info())
        
        #SQL bid query entry
        ##################################################
            # Insert the new bid into the SQLite database
        self.cursor.execute("""
        INSERT INTO bids (ArticleID, ArticleTitle, WinningBid, CloseDate, Fund)
        VALUES (?, ?, ?, ?, ?)""", (bid, title, amount, closingDate, fund))
        
        # Commit the transaction
        self.conn.commit()
        ##################################################
        
        #gui.load_dataframe_into_treeview(df, tree)
    def load_bids(self):
        csv_df = self.load_csv_data("eBid_Monthly_Sales_Dec_2016.csv")
        csv_df = csv_df[["ArticleID", "ArticleTitle", "WinningBid ", "CloseDate ", "Fund"]]
    
        # for row in csv_df:
        #     new_row = {col: value for col, value in zip(csv_df.columns, row)}
        #     df.loc[len(df)] = new_row
        df_new = self.df.append(csv_df, ignore_index=True)
        self.df['WinningBid '] = self.df['WinningBid '].astype(str)
        #print(df)
        #gui.load_dataframe_into_treeview(df, tree)
        return df_new
    
    #Heap sort time complexity
    #Worst case scenario O(n log n)
    def sort_by_title(self):
        start_time = time.time()
        self.df = self.df.sort_values(by="ArticleTitle", ascending=True, kind="heapsort")
        #load_dataframe_into_treeview(df, tree)
        end_time = time.time()
        duration = end_time - start_time
        print("Sort by title took {:.2f} seconds to execute.".format(duration))
        
    def sort_by_amount(self):
        start_time = time.time()
    # Clean the 'WinningBid' column
        try:
            self.df['WinningBid '] = self.df['WinningBid '].str.replace('$', '')  # Remove currency symbol
            self.df['WinningBid '] = self.df['WinningBid '].str.replace(',', '')  # Remove currency symbol
            #df['WinningBid '] = df['WinningBid '].str.replace('.', '')  # Remove currency symbol this was causing another bug of adding zeros because we need a decimal for float
            self.df['WinningBid '] = self.df['WinningBid '].str.strip()  # Remove leading and trailing whitespace
        except:
            
            print("already a number")
        print(self.df['WinningBid '])
        self.df['WinningBid '] = self.df['WinningBid '].astype(float)
        self.df = self.df.sort_values(by="WinningBid ", ascending=True)
        self.df['WinningBid '] = self.df['WinningBid '].astype(str)
        print(self.df['WinningBid '])
        end_time = time.time()
        duration = end_time - start_time
        print("Sort by amount took {:.2f} seconds to execute.".format(duration))
        #load_dataframe_into_treeview(df, tree)
        
    def sort_by_closing_date(self):
        self.df['CloseDate '] = pd.to_datetime(self.df['CloseDate '])
        self.df = self.df.sort_values(by='CloseDate ',ascending=False)
        
    # Bubble Sort
    def custom_sort_title(self):
        print('hi')
        #convert to a list of tuples
        data = [tuple(row) for row in self.df.values]
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j][1] > data[j+1][1]:  # Sort by the first column (Name in this case)
                    data[j], data[j+1] = data[j+1], data[j]
        #reconstruct dataframe
        self.df = pd.DataFrame(data, columns=self.df.columns)
        
    
    def insert_bid(self):
        print()
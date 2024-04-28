"""
============================================================================
Name        : VectorSorting.cpp
Author      : Miguel Little
Date        : 04/14/24
Version     : 3.0
Copyright   : Copyright © 2017 SNHU COCE
Description : Python Gov Bid Sorting Application

Intent      : This project was converted to a Python application as to
              demonstrate a complex language conversion and implement
              a GUI that was more visually appealing than terminal.
              This artifact will import bids from a CSV file, where
              you can then sort the data by different parameters.
              The application will also allow the user to add a bid,
              and the added bids will be uploaded to the database.

============================================================================

"""

from data import Data
from gui import GUI
#TODO:
#Fix bugs:
    #after loading from db and sorting the values go to nan -> Complete
    #it loads the contents from csv when loading from db ->  Complete
#Tasks:
    #add the time complexity
    #create classes for object oriented -> Complete
    
#Extra points
    #db add the cvs data on request


gui = GUI()


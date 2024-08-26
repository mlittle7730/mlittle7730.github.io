"""
============================================================================
Name        : VectorSorting.cpp
Author      : Miguel Little
Date        : 08/19/24
Version     : 4.0
Copyright   : Copyright © 2017 SNHU COCE
Description : Python Gov Bid Sorting Application

Intent      : This project was converted to a Python application as to
              demonstrate a complex language conversion and implement
              a GUI that was more visually appealing than terminal.
              This artifact will import bids from a CSV file, where
              you can then sort the data by different parameters.
              The application will also allow the user to add new bids.
              
              This Python application sorts utilizing bubble sort, heap sort,
              merge sort, and quick sort algorithms. Time complexity has been
              added and each sort function displays the time it takes when the
              application is run.
              
              Every time a user adds a bid to the system it is uploaded to
              to the SQL Lite database. All the added bids can be sorted
              and viewed.

============================================================================

"""

#from data import Data
from gui import GUI
#TODO:
#Fix bugs:
    #after loading from db and sorting the values go to nan -> Complete
    #it keeps the contents from csv when loading from db ->  Complete
#Tasks:
    #add the time complexity -> Complete
    #create classes for object oriented -> Complete

gui = GUI()


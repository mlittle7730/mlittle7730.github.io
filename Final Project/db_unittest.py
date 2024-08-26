"""
============================================================================
Name        : VectorSorting.cpp
Author      : Miguel Little
Date        : 08/20/24
Version     : 4.0
Copyright   : Copyright © 2017 SNHU COCE
Description : Python Gov Bid Sorting Application

Intent      : This unit test tests the code for a Unique article ID and
              a title that isn't NULL

============================================================================

"""

import unittest
from data import Data
from time import time

class TestDatabaseMethods (unittest.TestCase):
    
    #Unit test to ensure that article ID's in the database are unique
    def test_uniqueArticle(self):
        
        db = Data()
        
        bid = {}
        bid['bid'] = str(time())
        bid['title'] = 'Test Unique Article'
        bid['amount'] = 25.25
        bid['closingDate'] = '04/25/24'
        bid['fund'] = 'Enterprise'
        
        result01 = db.submit_input(bid)
        result02 = db.submit_input(bid)
        db.close_all()
        self.assertNotEqual(result01, result02)

    #Test to ensure that Title isn't NULL
    
    ### FUTURE TO-DO FIX NOT NULL TITLE TEST ###
    
    #def test_notNullTitle(self):
        
     #   db = Data()
        
        #Create dictionary for specific items
     #   bid = {}
     #   bid['bid'] = str(time())
     #   bid['title'] = None
     #   bid['amount'] = 124.26
     #   bid['closingDate'] = '04/25/24'
     #   bid['fund'] = 'Enterprise'
        
     #  result01 = db.submit_input(bid)
     #  db.close_all()
     #  self.assertFalse(result01)

if __name__ == '__main__':
    unittest.main()
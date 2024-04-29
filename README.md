# <pre align="center">Final Project</pre>

*Note: Due to Libary version, "append" on line 74 of the "data.py" file may have to be updated to "_append" or vise versa.*
*Note: Make sure Date added when using "Add a Bid" is an existing date*

## <pre align="center">Functionality</pre>

Originally, this code was a [C++ Project](https://github.com/mlittle7730/mlittle7730.github.io/tree/Vector-Sorting) that has now been updated to a Python Application. This project allows the user to view data off of a CSV file, sort the data using different parameters using sorting alorithms, and upload new bids/data to a database through SQL Lite. All of this was implemented through a visually pleasing GUI using tkinter and done with security practices in mind.

## Updates and Issues

First update I made to this project was creating it in Python, reimplementing the sorting algorithms I created in C++ and applying a tkinter GUI was the next step. Following this I was able to make the code modular using classes.

Next updates was creating new algorithm functionality, where I used bubble sort. I then added time complexity to the code for the sorting functions, which initially only displayed 0s but is fixed now.

Lastly I used SQL Lite to add a database to the code. Now all bids that are added will be stored in the database and the user will be able to display and sort them at any time.

Issues and Complications:

One of the challenges faced was changing the project to a Python application as it was difficult to reimplement all the app functionalities. Creating the classes to convert the code to an object-oriented design was one of the biggest challenges. One of the difficulties in doing this was that the memory kept getting deallocated whenever the function calls didn’t store the data. In order to fix this, I had to learn about deallocation of memory and using the built-in copy function that would create new memory sources.

The sort by functions were returning “nan” for date and amount for a very long time. Initially it was because I was mixing up float and int for the values.  Another difficulty was converting the dates into date time objects to be able to sort by date. Also, another issue that I was running into was calculating what was the actual runtime of the functions because they were running very quick so it would return an output of 0 seconds. Because of this it was difficult to verify whether the logic was correct and if time complexity was properly implemented.

One of the challenges with databases was coming up with a way to implement data from a database as well as the CSV file when loading bids. Once that worked the next issue was that the data types were not matching, so when sorting the values would return as “nan”. A choice that took a lot of consideration was choosing which database management system would be best for security, using SQL Lite turned out to be the most secure when using this app.

## Future Plans

I plan to add a server based database with users and permissions in the future. This will allow for companywide implementation of this application, since they will be able to pull the same information with permissions and higher security.
I also plan on giving the GUI another theme using customtkinter at some point in the future, since it is using a basic GUI for now.
Adding "Update a bid" and "Search bid" functions will also make this project a lot more lucrative.

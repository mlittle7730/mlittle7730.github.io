# <pre align="center">Final Project</pre>

*Note: Due to Libary version, "append" on line 100 of the "data.py" file may have to be updated to "_append" or vise versa.*

## <pre align="center">Functionality</pre>

Originally, this code was a [C++ Project](https://github.com/mlittle7730/mlittle7730.github.io/tree/Vector-Sorting), it has been converted to a Python Application. This project allows the user to load data off of a CSV file, sort that data using different parameters with sorting alorithms, and upload new bids to a database through SQL Lite. The application runs a visually pleasing GUI using tkinter and was created with security practices in mind.

## Updates and Issues

First update I made to this project was creating it in Python, after adding a GUI with tkinter then I had to recreate the sorting algorithms I had created in C++ and make them more efficient.  Next I was able to modularize the code using classes.

To enhance the algorithms further, I implemented time complexity and diversified the sorting algorithms used per function. Merge Sort and Heap Sort algorithms were the best. I used SQL Lite to add a database to the code. Now all bids that are added will be stored in the database and the user will be able to display and sort them at any time.

My last changes were implementing unit tests and error handling protocols, this was a user can't just input any data into the database, which is another layer of security.

Issues and Complications:

One of the challenges faced was changing the project to a Python application as it was difficult to reimplement all the app functionalities. Creating the classes to convert the code to an object-oriented design was one of the biggest challenges. One of the difficulties in doing this was that the memory kept getting deallocated whenever the function calls didn’t store the data. In order to fix this, I had to learn about deallocation of memory and using the built-in copy function that would create new memory sources.

The sort by functions were returning “nan” for date and amount for a very long time. Initially it was because I was mixing up float and int for the values.  Another difficulty was converting the dates into date time objects to be able to sort by date. Also, another issue that I was running into was calculating what was the actual runtime of the functions because they were running very quick so it would return an output of 0 seconds. Because of this it was difficult to verify whether the logic was correct and if time complexity was properly implemented.

One of the challenges with databases was coming up with a way to implement data from a database as well as the CSV file when loading bids. Once that worked the next issue was that the data types were not matching, so when sorting the values would return as “nan”. A choice that took a lot of consideration was choosing which database management system would be best for security, using SQL Lite turned out to be the most secure when using this app.

In the data.py file, I localized the submit_input function instead of having it call gui.py which was difficult. I then made the time taken to sort the data by parameters display on the GUI which took me some time.

## Future Plans

I plan to add a server based database with users and permissions in the future. This will allow for companywide implementation of this application, since they will be able to pull the same information with permissions and higher security.
I want to create more unit tests to run situational tests in the code and fix my Not Null unit test so that it runs properly.
Adding "Update a bid" and "Search bid" functions will also make this project a lot more lucrative.

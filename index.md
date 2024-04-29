<center>
  <img src="MiguelLittle.png" height=250 width=250>
</center>

# <center>CS499 - Computer Science Capstone</center>

## <center>Southern New Hampshire University</center>

### <center>Professional Self Assessment</center>

Here at Southern New Hampshire University I have learned many skills, both technical and practical. In studying Computer Science, it has not always been the easiest of projects, but it has taught me how to overcome problems and how to really learn new abilities and skills. One of the hardest courses I took was my OpenGL course, CS-330 Computer Graphics and Visualization. In that course I had to create a 3D environment that mirrored a photo I took of three objects. Through all of the struggle in this class I was finally able to learn how to create the environment. That class helped me to apply skills needed in this industry, which are practical skills such as thinking outside the box, learning and planning before executing, and enjoying the challenges while pushing through. My CS-260 class really helped me to develop my skills in software engineering, as well as how to work with data structures and algorithms. I also took DAD-220 which focused on database, learning how to sort and display data helped a lot with the enhancements I have made in this ePortfolio. My CS-310, Collaboration and Team Project course helped me to understand how to collaborate in team environments by understanding how companies plan and push to organizational repositories for updates and changes.

All of the changes I made to the artifact to enhance it really showcased my skills in software engineering/design, data structures and algorithms, and databases. All of these changes were made while keeping security in mind. There were many hurdles to overcome, even as small as adding an underscord to <code>_append</code> as the updated library broke the code. Overcoming each hurdle taught me what it will be like to work in the CS industry. When I first started here at SNHU I was unsure if I was going to be able to finish my degree in CS as it was difficult for me. Time and time again I'd get stuck and feel an underlying motive to give up, even in this last class. But showing up everyday and giving it my all has taken me this far, and I won't be giving up that quality for anything.

Here in my ePortfolio, I will showcase a summary of core skills (Categories: Software Design/Engineering, Data Structures and Algorithms, Databases, Security) I have learned here at SNHU, this is part of my Computer Science Capstone course. I will perform a code review of a chosen artifact, and demonstrate how it was updated in three primary categories.

### *Code Review*

Why conduct Code Review anyway?
Whether the project is large scale or a small project, code review should be a prioritized process. The objective of a successful code review is reviewing it and making sure it is functional, doesn't have any logic errors or bugs within the code, making sure it is organized and practically written, and lastly verifying its security.

Here I review the code I enhanced. I go over the functionality of the original code, how the structure, logic, efficiency, functionality, security, testing, commenting, and documenting can be improved, and lastly a walkthrough of the planned enhancements and how they will meet the five course outcomes accross the three categories.

<code>Click HERE to watch the code review video.</code>

## <center>ORIGINAL ARTIFACT</center>

This is the artifact project I will be making enhancements to. This application is written in C++ and it has a basic terminal interface for users to display bids and sort them using basic sort algorithms. The reason I chose this project as an artifact to enhance is because it has a lot of room for improvement such as a creating a proper GUI, making the code modular, better algorithm utilization such as sorting by parameters, and enhancing the user experience and usability such as creating an "Add a bid" function and a database to store the added bids.

Here is the original terminal interface for the application:

<img src="Category1 Before.JPG" height=250>

View the original artifact code [HERE](https://github.com/mlittle7730/mlittle7730.github.io/tree/Vector-Sorting).

## <center>ENHANCED ARTIFACT</center>

This is my Python Application after all of the changes have been made to meet all of the three categories. The GUI is visually appealing and the application functions allow the user to display the bids, sort them by a few different parameters, add a bid entry, and to display the bids that have been uploaded to the database.

Here is the new and improved GUI for this application:

<img src="Category1 After.JPG" height=250>

View the Artifact code [HERE](https://github.com/mlittle7730/mlittle7730.github.io/tree/Gov-Bids-Application).

### <center>Meeting Each Category</center>

### *Software Design and Engineering*

I enhanced the Software Design and Engineering in this artifact by converting it from a C++ project to a Python application. This application loads bid data from a CSV file and uses sorting algorithms to sort those bids by different parameters. When it was a C++ project the program would launch in a terminal window that was not visually pleasing, so it has been updated to a nicer GUI that now has radio select buttons and displays the data in an organized column using tkinter. Since the application was solely driven by functions in the main file, I then made it modular by creating classes for the functionality.

View my narrative for this enhancement [HERE](https://github.com/mlittle7730/mlittle7730.github.io/blob/Narratives/Software%20Engineering%20and%20Design%20-%20Narrative.pdf).

### *Algorithms and Data Structures*

I then enhanced the Algorithms and Data Structures in this artifact by first implementing time complexity to the sort algorithms so that it displays how long it took to sort the data by parameters. To increase algorithm complexity I added a new algorithm for sort by title using Bubble sort by Big-O, and created a radio select button for it ("Bubble Sort by Title"). Here are the scenarios for the bubble sort algorithm, where N is the number of items in the data it's sorting.

<img src="scenarios.png" height=250>

<code><a href="https://big-o.io/">Image Source</a>.</code>

View my narrative for this enhancement [HERE](https://github.com/mlittle7730/mlittle7730.github.io/blob/Narratives/Data%20Structures%20and%20Algorithms%20-%20Narrative.pdf).

### *Databases*

Lastly, I added a Database to this artifact using SQL Lite. The user could add bids to the data but it wasn't stored anywhere and was lost once the program was shut. By adding a database to this application to hold the added bids they were able to save through each run. The user can now load the bids from the database with or seperate from the CSV data, and sort through the data as usual.

View my narrative for this enhancement [HERE](https://github.com/mlittle7730/mlittle7730.github.io/blob/Narratives/Data%20Structures%20and%20Algorithms%20-%20Narrative.pdf).

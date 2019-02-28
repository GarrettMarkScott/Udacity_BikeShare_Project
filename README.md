### Date created
February 27th, 2019

### Project Title
Udacity Bike Share Project & Git Final

### Description
This program will help investigate the usage of City Bike data from Washington, New York City, and Chicago.

### Required Modules
- numpy
- pandas
- time
- re

### Files used
- chicago.csv
- new_york_city.csv
- washington.csv
- bikeshare_2.22.py

### Known Bugs
1. After telling the program you would like to restart, the second pass will show the entire DataFrame when "All" months are selected. This is isolated to just the month selection. If a particular month is chosen (I.E. March) it will work as normal regardless of other user inputs.
2. Washington.csv contains utf-16 text inside the file and panda.read_csv() requires utf-8 to function. 

Both bugs were brought to [Udacity's](udacity.com) attention through the student hub and both project submissions but their staff neglected to help with these issues.

### Credits
There were many sources outside of Udacity that were used as references.


Some credits I have open at the moment are the following:
- https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000597044--Couldn-t-check-the-working-tree-for-unmerged-files-because-of-an-error-
- https://stackoverflow.com/questions/5772908/trouble-merging-upstream-changes-back-into-my-branch
- https://stackoverflow.com/questions/8949252/dont-understand-what-this-attributeerror-means



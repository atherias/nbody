# nbody

A Python and a C++ implementation of a n-body simulator, taken from [The Computer Language Benchmarks Game](https://salsa.debian.org/benchmarksgame-team/benchmarksgame/).

To be used in the GEO1000 Python Programming for [Geomatics](https://www.tudelft.nl/onderwijs/opleidingen/masters/gm/msc-geomatics) course at Delft University of Technology, Q1, 2021.

--- 

October 29 2021  
Python for Geomatics  
Assignment 4

#### Name(s) and student number(s):
Adele Therias: **5485193**  
Jonas Stappers: **4603001**

#### Link to the Git repository:

#### Number of words in report:

#### Difference between Python and C++ programs:
A paragraph (max. 200 words) explaining how the Python and C++ programs are different (How is the information in the simulation represented: Which data types do the programs use to represent the data for the simulation?)
Adele:
- python stores information about the bodies and their original features in a dictionary with body name as key and tuple of list for position, list for velocity and floating point number for mass.
- python then creates tuples that include the data in the dictionary, then forms a list that contains all possible combinations of bodies (their values)
- as python iterates, it updates the values of the bodies in the list
- C++ stores information about the bodies in the form of a user-defined class called "object" that includes a string name, a vector for position, a vector for velocity and a floating point number with 2 decimal precision for mass.
- C++ updates the values in the vectors during the iterations
- 
#### How we solved the task:
A paragraph reflection on how you went about solving the task (max. 400 words). Which steps did you take? How did you measure the runtime? How did collaboration go with Git? Did you get stuck? Which sources did you consult when you got stuck? Did you expect the results you obtained? Etc.
Adele:
1. To understand the nbody simulation procedure, I went through the original python code line by line and ran the debugger with stops at multiple points in the script.
2. I added comments to describe each step taken in the program, including the object types and purpose of each step.
3. Based on this understanding, I then determined where in the program should be added the write-to-file steps. I felt stuck regarding how to write the introductory line and timestep lines in the same file.
4. When writing to the csv file, I was stuck at how to include the name of the body as the first item in the csv line. I thought I should retrieve the name from the dictionnary but was 
unsure how considering that dictionaries are unordered. I found a comment on stackexchange that suggested iterating over dictionary items and returning the key that matches the desired value. https://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems-in-python2 
5. In order to track the run time for different n values, I imported the time module, created a start_time variable at the beginning of the program, and calculated the difference between start_time and end time at the beginning of the program. I found support in this resource: https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
6. When running the code for 5 million and 50 million iterations, the processing time was way too long. I modified the file opening and closign processes to take place outside of a loop, which significantly reduced the run time. For example, for 500,000 iterations the time decreased from ~800 seconds to ~11 seconds.
7. I compared the C++ code to the Python code to understand the differences in implementation.
8. I began by writing out the header row into the csv to ensure it was working.
9. Then, I identified the line in the program where each position should be written to the csv file. I initially found it confusing to format and refer to an element from the vector.
10. To address this challenge, I referred to two resources. One focussed on formatting strings in C++ (https://www.codegrepper.com/code-examples/c/string+format+c%2B%2B), the other focused on referencing vector elements (https://thispointer.com/c-how-to-get-element-by-index-in-vector-at-vs-operator/)
11. I started by writing one vector attribute to the cv (name) and once the code worked I added the other attributes.
12. I tried to open the file stream within the state function to reduce computing time, but the program still took longer in C++ than python.
13. 
#### Run times:
Timings for Python, C++ Debug and C++ Release, in a table and visualised in a chart (x-axis: instance size/y-axis: run time).

|             | n=5000 | n=500.000 | n=5.000.000 | n=50.000.000 |
|-------------|---------------|----------------|-----------------|-----------------|
| Python      | 0.109 seconds | 11.164 seconds | 124.840 seconds | 1268.621 seconds|
| C++ Debug   | 0.739 seconds | 77.812 seconds |  87.705 seconds |              |
| C++ Release | 0.774 seconds | 86.477 seconds | 1322.458 seconds|              |

#### QGIS visualization:
One (or more, e.g. 1 overview and 1 close-up) screenshot of QGIS, where you have loaded the CSV files your code did produce for 5’000 iterations (for both C++ as well as Python programs) 

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

#### How we solved the task:
A paragraph reflection on how you went about solving the task (max. 400 words). Which steps did you take? How did you measure the runtime? How did collaboration go with Git? Did you get stuck? Which sources did you consult when you got stuck? Did you expect the results you obtained? Etc.
Adele:
1. To understand the nbody simulation procedure, I went through the original python code line by line and ran the debugger with stops at multiple points in the script.
2. I added comments to describe each step taken in the program, including the object types and purpose of each step.
3. Based on this understanding, I then determined where in the program should be added the write-to-file steps. I felt stuck regarding how to write the introductory line and timestep lines in the same file.
4. 
#### Run times:
Timings for Python, C++ Debug and C++ Release, in a table and visualised in a chart (x-axis: instance size/y-axis: run time).

|             | n=5000 | n=500.000 | n=5.000.000 | n=50.000.000 |
|-------------|--------|-----------|-------------|--------------|
| Python      |        |           |             |              |
| C++ Debug   |        |           |             |              |
| C++ Release |        |           |             |              |

#### QGIS visualization:
One (or more, e.g. 1 overview and 1 close-up) screenshot of QGIS, where you have loaded the CSV files your code did produce for 5’000 iterations (for both C++ as well as Python programs) 

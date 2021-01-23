# Computing session 1: 
#   Introduction to development tools

This session should be done in 3 hours.
You are advised to refer the the C++ lectures and the links given below in order to
achieve the goals mentioned below.
The subject (described in *Context*) as been given choosen to be simple in order to allow students to be focussed on getting familiar with the environment and good practices of C++ development.

## Goals:
  - Becoming familiar with C++ development environment
  - Practicing basic C++ development with well structured files
  - Producing a shared library
  - Getting used to basic stl classes


## Context:
The aim of the program is to read a binary file saved by a certain device, decode its content and allow an *a posterio* treatment if its data through the production of an output csv file.

## The tools:
   - **editor**: feel free to use the editor of our choice. Several are available on virtual machine (including emacs, gedit, nedit, vi/vim)
   - **compiler**: by default you can use **g++** (clang can also be used) 
   - **git**: requires to have an accound on [github](https://github.com/)


## Steps

In order to ease the realization of this computing session, it has been decomposed into short steps.
At the end of each of them, you can compile and test our program becore going further.


### Prerequisites

#### Downloading our main github repository

   - On Linux/macOS, you can launch in a terminal the command
   ```
      git clone https://github.com/echabert/ESIPAPCpp.git
   ```
   - On Windows but also other system, you can simply download an zip of the code (needed to be unzip)
   https://github.com/echabert/ESIPAPCpp/archive/main.zip

You will then be able to access to all files

#### Creating your private github repository for these sessions

The goal of this section is to save your results into the revisionning software **git**.
You need to follow the instructions described in [../../doc/git/GitRepository.md](the section GitRepository).
Once the repository is created, you can *download it* (*clone* it) by using the command:
```
git clone https://github.com/your_username/ESICppCS.git
```
where your\_username as to be replace by your username.
A password will be asked.
Then follow the instructions:
   - Go to the directory<br/>
   On Linux/Windows you can use the command ```cd ESICppCS```
   - Create a directory "Session1" <br/>
   On Linux/Windows you can use the command ```mkdir Session1```
   - Create an helloworld.cpp file <br/>
   ```#include <
   - Add our file
   ```
   git add MYFILE
   ```
   - Commit our file
   ```
   git commit -m 'first commit for test' MYFILE
   ```
   - Push our file into our directory
   ```
   git push
   ```

### Step 1: using stl classes

The goal of this section is to be able to utilize classes available in the Standard Template Library (stl).
For our application, several classes will be useful:
   - [ifstream](http://www.cplusplus.com/reference/fstream/ifstream/) : a class which allow to open file
   - [ofstream](http://www.cplusplus.com/reference/fstream/ofstream/) : a class which allow to write file
   - [cout](http://www.cplusplus.com/reference/iostream/cout/?kw=cout): an object of the class ostream that represents the standard output stream 
   - [vector](http://www.cplusplus.com/reference/vector/vector/?kw=vector): a template class that is a container representing an arrays that can change in size

Write a program which:
   - Write a message to inform users that the program has started 
   - Open a **binary** file *data.dat* which is available HERE
   - Write an error message if something went wrong during this operation
   - Close the file 
   - Write a message to inform users that the program ended

Note that we don't yet try to read the file content as it is in a binary mode.
This will be the goal of the next step.
Save, compile and test our program before going to the next step.

### Step 2: binary decoding 

The goal of this section is to decode the binary content of the file opened in step 1.
In order to achieve this task, the developper need to know the data structure used to encode the content.
If this is not the case, meaningless results or even errors could be obtained. 
The data structure in our case, can be summarize as described below:


Modify you program to:
   - Read the values sequentially
   - Write them with cout commands

Save, compile and test our program before going to the next step.
In order to check that you program is working properly, the values value you should read are:
XXX

### Step 3: exporting the data in a human readable format: csv file

The goal of this section is to produce a csv file (comma separated value) with numerical values corresponding the data: *output.csv*.
The produced output file could later be tested by other program/applications such as OpenOffice/Excell.
Instructions:
   - Open a new file in writing mode: an instance of [ofstream](http://www.cplusplus.com/reference/fstream/ofstream/)
   - Write the data in a structured way: values separated by a comma, one line per entry into the csv file
   - Write a short report into the terminal (cout command) at the end of the reading to report the number of entries.

Save, compile and test our program before going to the next step.


Tests:
   - Compare the size of the binary file and the csv file. How can you intepret the difference ?
   - Open the file with an external program as mentioned earlier and check the integrity of the data
   - Produce the graphics of XXXX


### Step 4: use of a function

The goal of this section is to move the block of instructions that deal with the binary decoding into a well-defined function in order to be reused in other applications if needed.
In order to do this, you need to:
   - Define properly the prototype of the function (return type and ordered list of arguments with there type)
   - Implement the function *Decoding*
   - Call the function in the *main*

You have the freedom to design the prototype as you which.

Save, compile and test our program before going to the next step.


### Step 5: file splitting

The goal of this section is to split the program into 3 files:
   - An header file containing the prototype of the function: *Decode.h*
   - A source file containing the definition of the function: *Decode.cpp*
   - A main file containing the function main: *main.cpp*

Few advices:
   - The header file need to be protected against multiple inclusion
   - The compilation can be done in several step as there is 2 cpp files

Save, compile and test our program before going to the next step.


### Step 6: creating a library

The goal of this section is to create a shared library.
In our application, this library will only contain the decoding function.
Relevant instructions have been given during the lecture.
You can refer to them.
Actions to be done:
   - Create a shared library decode.so (.dylib or .dll)
   - Link the library to the executable  (*main*)

Excute the program to check that the compilation chain and the link edition worked well.






### Step 7: going further

This last step is **not mandatory**. 
If you have already finished the previous steps and want to go further, we provide you several options:
   - Use arguments of the *main* function to pass the name of the input file into the command line
   - Compute basic statistics (mean and std-deviation) for each of the main variables and report them at the end of the execution


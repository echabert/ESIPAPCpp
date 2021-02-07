# Computing session 1: Introduction to development tools

This session should be done in 3 hours.
You are advised to refer the the C++ lectures and the links given below in order to
achieve the goals of this computing session.

## Goals
The subject of this first computing session is voluntarily simple in order to allow you to acquaint yourself with the environment and good practices of C++ development. During this session, you must write in C++ a program from scratch and step-by-step. The program to design and to code must be able to read data, acquired by a sensor device and encoded in a binary file, to decode them and to save them into a CSV which can be read by a spreadsheet like Excel or OpenCalc.

## Skills to develop
  - Becoming familiar with C++ development environment (compiler, linker, text editor, ...).
  - Writing a simple C++ program.
  - Manipulating bits in order to decipher data.
  - Using the STL classes for reading/writing a file and for displaying informations at the screen.
  - Structuring the program in functions and in different source files.
  - Saving and sharing the C++ code with a version-control system (Git in our cases).

## Tools used
   - **Compiler**: 
       - on Linux/MacOSX machines, the default compiler is **g++**. Alternatively, **clang** can also be used.
	   - on Windows machines, we use Visual Studio 2013 compiler, named **cl**.
   - **Text editor**: feel free to use the editor of our choice:
       - on the Linux virtual machine, several editors are available including emacs, gedit, nedit, vi/vim, ...
	   - on Windows machines, the Visual Studio IDE (Integrated Development Environment) is recommended or a smart text editor such as [NotePad++](https://notepad-plus-plus.org/downloads/).   
   - **Git**: requires to have an accound on [github](https://github.com/)

## Instructions

In order to ease the realization of this computing session, it has been decomposed into short steps.
At the end of each of them, you can compile and test our program before going further.

### Step 0: Preparing your work environment

#### Step 0.1: Downloading the instructions 

You must access to the last version of our instructions order to do the computing sessions. Please follow the instructions in order to have the updated code.

   - Opening a new console session:
     - On Linux/macOSX machines, you must click on the icon of the Terminal.
	 - On Windows machines, you must open the program "VS2013 x86 Native Tools Command Prompt" (not the x64!).

   - Creating a working folder
     - On Linux/macOSX machines, you must issue the following commands:
       ```
          cd 
          mkdir esipap_instructions
		  cd esipap_instructions
       ```
     - On Windows machines, you must issue the following commands:	   
        ```
          cd C:\
          mkdir esipap_instructions
		  cd C:\workingdir
        ```
   - Download our main github repository by typing the command:
   ```
      git clone https://github.com/echabert/ESIPAPCpp.git
   ```
     Comment: This last step can also carry out by downloading a zip archive of the code (needed to be unzip)
   https://github.com/echabert/ESIPAPCpp/archive/main.zip

#### Step 0.2: Creating your own repository

  - The goal of this section is to create a remote repository where you can save your results. You need to follow the instructions described in [../../doc/git/GitRepository.md](the section GitRepository).

   - Opening a new console session:
     - On Linux/macOSX machines, you must click on the icon of the Terminal.
	 - On Windows machines, you must open the program "VS2013 x86 Native Tools Command Prompt" (not the x64!).

   -  Once the repository is created, you can *download it* (*clone* it). To do that, first, opening a new console session:
     - On Linux/macOSX machines, you must issue the following commands:
       ```
          cd 
          mkdir esipap_sessions
		  cd esipap_sessions
       ```
     - On Windows machines, you must issue the following commands:	   
        ```
          cd C:\
          mkdir esipap_sessions
		  cd C:\esipap_sessions
        ```
   - Downloading your github repository by typing the command:
     ```
       git clone https://github.com/your_username/ESICppCS.git
     ```
     where your\_username as to be replaced by your username.
     A password will be asked.

#### Step 0.3: Creating your working folder for Computing Session 1

  - In a console session, entering the folder ```ESICppCS``` by issuing the command lines:
	   - On Linux/MacOSX machines: ```cd ~/esipap_sessions/ESICppCS```
	   - On Windows machines: ```cd C:\esipap_sessions\ESICppCS```
	   
  - Creating a folder devoted to Computing Session 1 code: 
	```
	   mkdir Session1
	   cd Session1
	```
	
  - In the folder ```Session1```, creating a new text file called ```readme.txt``` containing the sentence ```Folder corresponding to ESIPAP-2021 Computing Session 1```
	
  - Telling Git that you have added a new file by issue the command line in the console:
      ```git add readme.txt```
	  
  - Recording the changes to the local repository with the following command:
	  ```git commit -m 'add readme.txt file` readme.txt```
	  
  - Propagating the changes to the remote repository with the following command:
	  ```git push```


### Step 1: Creating, building and running a 'Hello World!' program

   - In the folder `Session1` folder, creating a source file called `helloworld.cpp` with the following content:
     ```
	   #include<iostream>
	   
	   int main()
	   {
	     std::cout << "Hello World!" << std::endl;
		 return 0;
	   }
	 ```
	 
   - The way to build this program depends on your machine:
       - On Linux/MacOSX machines, the building (compilation + link + creation of an executable file called `helloworld`) can be done by typing the command `
	     ```
		   g++ helloworld.cpp -c helloworld
		 ```
	   - On Windows machines by using command lines, the building (compilation + link + creation of an executable file called `helloworld.exe`) can be done by typing the command `
	     ```
		   cl helloworld.cpp -c helloworld.exe
		 ```
	   - On Windows machines by using the Visual Studio interface, the building (compilation + link + creation of an executable file called `helloworld.exe`) can be done by following the different steps:
	   
          - ERIC TO DOCUMENT
		  - ERIC TO DOCUMENT

   - Executing the program:
       - On Linux/MacOSX machines: ```./helloworld```
	   - On Windows machines by using command lines: ```helloworld```
	   - On Windows machines by using the Visual Studio interface: click on the button "Local Windows Debugger"
	  
   - Saving the code in the remote repository:
	
	  - Telling Git that you have added a new file by issue the command line in the console:
      ```git add helloworld.cpp```
	  
      - Recording the changes to the local repository with the following command:
	  ```git commit -m 'add helloworld program' helloworld.cpp```
	  
      - Propagating the changes to the remote repository with the following command:
	  ```git push```
	  
### Step 2: using STL classes

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


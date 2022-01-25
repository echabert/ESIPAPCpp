# Checking the setup on Linux / macOSX system


## Step 1: Checking git

 ### 1.1. Testing the git command
 
  - Launching the console application.
  - Typing the command line `git --version`
  - If git is properly installed on your system, the previous command should display the version of the git package.

 ### 1.2. Cloning a public repository
 
For testing that git manages to access GitHub from the internet, we propose you to clone a public repository which will be useful in the following.
 
  - Launching the console application.
  - Creating a work folder. For instance <br/>
  ```cd ~```<br/>
  ```mkdir workdir```<br/>
  ```cd workdir```<br/>
  - Typing the command line `git clone https://github.com/echabert/ESIPAPCpp.git`
  - If git works properly, a folder called `ESIPAPCpp` must appear on your disk.
  - If it fails via the https access and you have an ssh-key, you can use the command line `git clone git@github.com:echabert/ESIPAPCpp.git` 

## Step 2: Checking the C++ compiler
 
  - Go into the folder  `~/ESIPAPcpp/validation_tests`
  - Issue the command line at the prompt: `python test-gpp-linux.py`. This Python-2 script will test the C++ compiler configuration in several situations. 
  - The C++ compiler is properly installed if all the validation tests have succeed. If you have at least one failure, please contact the supervisors.
	
## Step 3: Checking the ROOT installation

  - Go into the folder  `~/ESIPAPcpp/validation_tests`
  - Issue the command line at the prompt: `python test-root-linux.py`. This Python-2 script will test the C++ compiler configuration in several situations. 
  - The C++ compiler is properly installed if all the validation tests have succeed. If you have at least one failure, please contact the supervisors.
  

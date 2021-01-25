# Checking the setup on Linux system


## Step 1: Checking git

 ### 1.1. Testing the git command
 
   - Launching the console application.
   - Typing the command line `git --version`
   - If git is properly installed on your system, the previous command should display the version of the git package.

 ### 1.2. Cloning a public repository
 
For testing that git manages to access GitHub from the internet, we propose you to clone a public repository which will be useful in the following.
 
    - Launching the console application.
	- Type the command line `git clone https://github.com/echabert/ESIPAPCpp.git`
    - If git works properly, a folder called `ESIPAPCpp` must appear on your disk.

## Step 2: Checking 
 
On Fedora: 
   - ```yum install doxygen```

On Ubuntu:
   - ```apt-get install doxygen```
 
 ### 1.3. Installing Git
 
On Fedora: 
   - ```yum install git```

On Ubuntu:
   - ```apt-get install git```
	
 
 
## Step 2: Installing the ROOT package

There are several ways to install ROOT including:
   - downloading and compiling the sources <br/>
The pros are to choose the list of libraries compiled and to make sure that you are compliant with our environment. The cons are that it may appear as more complex and anyway time consumming.
   - using a pre-compiled version <br/>
   We suggest this solution for Ubuntu distributions.
   - using a package manager<br/>
This is the simplest way to proceed.
Several package managers can be available on our OS depending on our installation. By example on Fedora, you could either use yum (the default linux package manager), conda (if installed) or snap (if installed). 

Instructions on the website can found using this link [https://root.cern/install/](https://root.cern/install/). We have extracted the most relevant one for linux distribution but you can refer to the website if necessary.

Note that if ROOT is already installed on our machine and even if it is an old version, you don't need to update it to the latest one as we will only uses the basics of ROOT functionnalities.

On CentOS:
   - ```yum install epel-release```
   - ```yum install root```

On Fedora:
   - ```yum install root```

On Ubuntu:
   - **Download the latest pre-compiled version** corresponding to our OS: 6.22.06 in this link: [https://root.cern/releases/release-62206/](https://root.cern/releases/release-62206/). <br/>
   You could also use the wget command as following (for Ubuntu 19)<br/>
   ```wget https://root.cern/download/root_v6.22.00.Linux-ubuntu19-x86_64-gcc9.2.tar.gz```
  - **Move the archive** in a location when you want to install ROOT (could be our home directory)
  - **untar** the file downloaded:<br/>
   ```tar -xzvf root_v6.22.00.Linux-ubuntu19-x86_64-gcc9.2.tar.gz```
  - **Setup** <br/>
  Each time you want to be able to access ROOT, you need to launch the command (assuming that the directory root is located in our current directory) <br/>
  ```source root/bin/thisroot.sh ```
  - We suggest to add this instruction into our **~/.bashrc** file to make sure that it is always accessible (once you open a terminal). Make sure that you use the correct path. If you don't do that, you will need to launch the former command each time you open a terminal.



  


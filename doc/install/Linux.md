# Installation on Linux system


The procedure depends on the linux distribution you are using.

There are two main ways to install which depends on the linux package manager.

   - Fedora, CentOS, etc:    command **yum**
   - Ubuntu, etc: 	     command **apt-get**

Those commands will be launched in our **terminal**.


On Ubuntu-like distribution, we advice to refresh the list of package by typing:
```
apt-get update 
```

## Step 1: Installing the classical packages related to software development

 ### 1.1. C++ compiler and text editor 

To code in C++, we need at least a text editor (name it **EDITOR**) and a C++ compilor, **g++**.

**EDITOR** could be *emacs*, *gedit*, *nedit*, *vim*, etc

In almost all distributions, there are available by default.

To test if it is the case, you can simple type the commands in the terminal
   - ```EDITOR```
   - ```g++ --version```
 
If there are not available or if you want to install a specific editor, you can launch the following commands:

On Fedora: 
   - ```yum install g++```
   - ```yum install EDITOR```

On Ubuntu:
   - ```apt-get install g++```
   - ```apt-get install EDITOR```


 
 ### 1.2. Installing Doxygen
 
On Fedora: 
   - ```yum install doxygen```

On Ubuntu:
   - ```apt-get install doxygen```
 
 ### 1.3. Installing Git
 
On Fedora: 
   - ```yum install git```

On Ubuntu:
   - ```apt-get install git```
	
 ### 1.4. Installing CMake

On Fedora: 
   - ```yum install cmake```

On Ubuntu:
   - ```apt-get install cmake```
 
 
## Step 2: Installing the ROOT package

There are several ways to install ROOT including:
   - downloading the sources and compiling

The pros are to choose the list of libraries compiled and to make sure that you are compliant with our environment. The cons are that it may appear as more complex and anyway time consumming.
   - using a pre-compiled version
   - using a package manager<br/>
Several ones can be used on the same OS. By example on Fedora, you could either use yum, conda (if installed) or snap (if installed). 
   This is the simplest way to proceed.

Instructions on the website can found using this link [https://root.cern/install/](https://root.cern/install/).


For the sake of simplicity, we will propose to use the package manager when possible.
If ROOT is already installed on our machine, you don't need to update our version to the latest one as we will only uses the basics of ROOT functionnalities.

On CentOS:
   - ```yum install epel-release```
   - ```yum install root```

On Fedora:
   - ```yum install root```

On Ubuntu:
   - Download the latest pre-compiled version corresponding to our OS: 6.22.06 in this link: [https://root.cern/releases/release-62206/](https://root.cern/releases/release-62206/). You could also use the wget command as following (for ubuntu 19)
   ```wget https://root.cern/download/root_v6.22.00.Linux-ubuntu19-x86_64-gcc9.2.tar.gz```
  - Move the archive in a location when you want to install ROOT (could be our home directory)
  - untar the file downloaded:
   ```tar -xzvf root_v6.22.00.Linux-ubuntu19-x86_64-gcc9.2.tar.gz```
  - Each time you want to be able to access ROOT, you need to launch the command
  ```source root/bin/thisroot.sh ```
  - We suggest to add this insctruction into our ~/.bashrc file to make sure that it is always accessible (once you open a terminal). Make sure that you use the correct path 



  


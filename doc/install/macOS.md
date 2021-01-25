# Installation on macOS system



There are several ways to perform software installation on macOS:
   - from dmg files
   - using package managers:
      - brew [used as example here]
      - port
      - fink
   - downloading and compiling sources
   two main ways to perform installation which depends on the linux package manager.

We propose here an example of installation procedure.
If you are used to different methods, feel free to change the procedure.
But anyway, make sure that your environment is ready to work by launching the tests
at the end of the installation.


## Step 0: Installing brew [optional but advised]
 
Whithin a terminal, launch the command: <br/>
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Note that it may take some time. Be patient.
In order to check that brew is installed and obtained the version (2.7.5), type:
```
brew --version
```

## Step 1: Installing the classical packages related to software development

 ### 1.1. Xcode 

In principe, to develop in C++ you need at least a text editor and a C++ compiler such as **g++**.
In principle, **g++** is already available on macOS.<br/>
You can test can this is the case by typing into a terminal <br/>
```g++ --version```

**Xcode** is a developper environment under macOS that can be used.
If it is not yet installed (check on *Applications*), you can download and install it using the link https://developer.apple.com/download/ <br/>
Once **Xcode** is installed, you should normally access to:
   - C++ compiler: **g++** (already installed by default) and **clang**
   - A program editor 

Other options to install **Xcode**:
   - Using Apple Store
   - Launching the command (in a terminal): ```xcode-select --install```


 ### 1.2. Installing Doxygen

   - If **brew** has been installed, you can type the command:<br/>
   ```brew install --cask  doxygen```
   - Otherwise, you can download and install doxygen from the link https://macdownload.informer.com/doxygen/

 
 ### 1.3. Installing Git

   - Check if **git** is already installed <br/>
In principle, git should be available once **Xcode** has been installed.
You can test by launching the following command in a terminal<br/>
```git --version``` <br/>
If it fails, you need to install git.
   - **git** installation:
Instructions can be found here: https://git-scm.com/download/mac.<br/>
If *brew* has been installed (cf section XX), you can type in a terminal:<br/>
```brew install git```

 
## Step 2: Installing the ROOT package

There are several ways to install ROOT including:
   - downloading and compiling the sources <br/>
The pros are to choose the list of libraries compiled and to make sure that you are compliant with our environment. The cons are that it may appear as more complex and anyway time consumming.
   - using a pre-compiled version <br/>
   We suggest this solution for Ubuntu distributions.
   - using a package manager<br/>
This is the simplest way to proceed.

Note that if ROOT is already installed on our machine and even if it is an old version, you don't need to update it to the latest one as we will only uses the basics of ROOT functionnalities.

Instructions on the website can found using this link [https://root.cern/install/](https://root.cern/install/). 

**Ordered list of possibilities to install ROOT:**
   - If **brew** has been installed [adviced], type into our terminal:<br/>
   ``` brew install root```
   - If instead you have **macports** installed, type:<br/>
   ```sudo port install root6```
   - If none of this option is possible, **download and install the binaries** which correspond to you macOS version and our XCode version from the link: https://root.cern/releases/release-62206/. You should firstly make sure that XCode was installed.
   - Last solution is to ** buid from source**. This requires to that **Cmake** has been installed). <br/>
   Instructions can be found here: https://root.cern/install/#build-from-source





  


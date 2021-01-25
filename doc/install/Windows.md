# Installation on Windows system

```diff
-These instructions do not work currently because ROOT is not compatible yet with the last release of Visual Studio.
```

## Step 1: Installing the classical packages related to software development

### 1.1. Installing Visual Studio 2019
 
  - Downloading the free version (community version) of Microsoft Visual Studio 2019 (release 16.X) from the official website: (https://visualstudio.microsoft.com/fr/downloads/)
  - Selecting the development for "C++ desktop applications", for "C++ linux applications", for "scientific package for python and F#".
 
### 1.2. Installing Doxygen
 
  - Downloading and installing the package from the website (https://www.doxygen.nl/index.html)
 
### 1.3. Installing Git
 
  - Downloading and installing the package from the website (https://github.com/)
  - Keeping all the default settings.
	
### 1.4. Installing CMake
 
  - Downloading the package (format .msi) from the website (https://cmake.org/download/)
  - Executing the .msi file in order to install it.
  - Specifiying that CMake must be set in the PATH environment variable for all users.  
 
## Step 2: Installing the ROOT package
 
### 2.1. Disclaimer
 
  - Do not download and install the binaries file because some problems can occur when you will link Visual C++ 2019 to ROOT.
 
### 2.2. Downloading the source tarball
 
  - Downloading the last release of ROOT (v6.22.06) :  https://root.cern/download/root_v6.22.06.source.tar.gz
  - Unzip the tarball and put the content in a new folder C:\SourceDir. If you have no software for untarring the file, please download 7Zip. 
 
### 2.3. Building ROOT  

  - Creating two folders: `C:\ROOT` and `C:\BuildDir`
  - In the `Start` menu of Windows, go to `Visual Studio 19` and select `x86 Native Tools Command Prompt for VS 2019` (not the 64bits one).
  - Type the following lines
    ```
    cd C:\BuildDir
	cmake -G "Visual Studio 16 2019" -A Win32 -Thost=x64 -DCMAKE_VERBOSE_MAKEFILE=ON -Dpyroot=ON -DACTIVATE_MULTITHREADED_COMPILATION=OFF -DCMAKE_INSTALL_PREFIX=..\ROOT -DCMAKE_CXX_STANDARD=14 ..\SourceDir
	```
  - If there is no mistake, then launch the building by the above command line. It last about 1 hour.
    ```
    cmake --build . --config Debug -j1
	```
  - If there is no mistake, then launch the installation in the binaries in the folder `C:\ROOT` by the command line:
    ```
	cmake --install
	```
  - Add `C:\ROOT` in the `$PATH` environment variable.
  

  


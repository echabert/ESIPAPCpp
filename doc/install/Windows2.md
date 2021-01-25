# Installation on Windows system

```diff
+These instructions allow us to build and install ROOT on Windows 10. But an old version of ROOT and Visual Studio are used.
```

## 1. Installing Visual Studio 2013
 
  - Downloading the free version of Microsoft Visual Studio 2013 update 5 (release XXX) from the official website: (https://visualstudio.microsoft.com/fr/vs/older-downloads/). It is possible that you need to create an account in order to download this old package.
  - Selecting the development for "C++ desktop applications" and "python applications".
 
## 2. Installing Doxygen
 
  - Downloading and installing the package from the website (https://www.doxygen.nl/index.html)
 
## 3. Installing Git
 
  - Downloading and installing the package from the website (https://github.com/)
  - Keeping all the default settings.
	
## 4. Installing CMake
 
  - Downloading the package (format .msi) from the website (https://cmake.org/download/)
  - Executing the .msi file in order to install it.
  - Specifiying that CMake must be set in the PATH environment variable for all users.  
 
## 5. Installing ROOT 5
 
  - Downloading the last release of ROOT 5 (v5.34.38):  https://root.cern/download/root_v5.34.38.win32.vc12.exe
  - Executing the file and installing ROOT *in a folder containing no space* in the name. Advised folder: `C:\ROOT` 
 
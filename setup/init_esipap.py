#!/usr/bin/env python
VERSION = '2.4'

import os
import logging
import sys
import getopt
import commands
import datetime
import subprocess
import time
import shutil
import glob
import os

print ""
print "----------------------------------------------"
print "        ESIPAP environment version " + VERSION
print "----------------------------------------------"
print ""
print "Information about the machine:"
import platform
print " - distribution:    "+' '.join(platform.dist())
import multiprocessing
print " - number of cores: "+str(multiprocessing.cpu_count())

print ""
print "Development packages:"

# g++
p = subprocess.Popen("g++ --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - GNU g++    NOT FOUND"
else:
    words = output.split()
    if len(words)<3:
        print " - GNU g++    FOUND      version UNKOWN"
    else:
        print " - GNU g++    FOUND      version "+words[2]

# clang
p = subprocess.Popen("clang --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - Clang      NOT FOUND"
else:
    words = output.split()
    if len(words)<3:
        print " - Clang      FOUND      version UNKOWN"
    else:
        print " - Clang      FOUND      version "+words[2]

        
# make
p = subprocess.Popen("make --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - GNU make   NOT FOUND"
else:
    words = output.split()
    if len(words)<3:
        print " - GNU make   FOUND      version UNKOWN"
    else:
        print " - GNU make   FOUND      version "+words[2]

# cmake
p = subprocess.Popen("cmake --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - CMake      NOT FOUND"
else:
    words = output.split()
    if len(words)<3:
        print " - CMake      FOUND      version UNKOWN"
    else:
        print " - CMake      FOUND      version "+words[2]
	
# python2
print " - Python2    FOUND      version "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])

	
# python3
p = subprocess.Popen("python3 --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - Python3    NOT FOUND"
else:
    words = output.split()
    if len(words)!=2:
        print " - Python3    FOUND      version UNKOWN"
    else:
        print " - Python3    FOUND      version "+words[1]

# doxygen
p = subprocess.Popen("doxygen --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - Doxygen    NOT FOUND"
else:
    words = output.split()
    if len(words)==0:
        print " - Doxygen    FOUND      version UNKOWN"
    else:
        print " - Doxygen    FOUND      version "+words[0]
	
# graphviz
p = subprocess.Popen("dot -V", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - Graphviz   NOT FOUND"
else:
    words = output.split()
    if len(words)<5:
        words = err.split()
	if len(words)<5:
            print " - Graphviz   FOUND      version UNKOWN"
        else:
            print " - Graphviz   FOUND      version "+words[4]
    else:
        print " - Graphviz   FOUND      version "+words[4]

# git
p = subprocess.Popen("git --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - Git        NOT FOUND"
else:
    words = output.split()
    if len(words)<3:
        print " - Git        FOUND      version UNKOWN"
    else:
        print " - Git        FOUND      version "+words[2]


        
print ""
print "High-Energy Physics frameworks:"

# root
p = subprocess.Popen("root-config --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - ROOT       "+"NOT FOUND"
else:
    words = output.split()
    if len(words)==0:
        print " - ROOT       FOUND      "+"version UNKOWN"
    else: 
        print " - ROOT       FOUND      "+"version "+words[0]

# root for python
try:
    from ROOT import TCanvas, TF1, gROOT
except:
    print " - pyROOT     NOT FOUND"
else: 
    myversion = gROOT.GetVersion()
    print " - pyROOT     FOUND      version "+myversion

# geant4
p = subprocess.Popen("geant4-config --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - Geant4     NOT FOUND"
else:
    words = output.split()
    if len(words)==0:
        print " - Geant4     FOUND      version UNKOWN"
    else:
        print " - Geant4     FOUND      version "+words[0]
		
print ""
print "Text editors:"

# emacs
p = subprocess.Popen("which emacs", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - GNU emacs  NOT FOUND"
else:
    print " - GNU emacs  FOUND"

# vi
p = subprocess.Popen("which vi", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - vi/vim     NOT FOUND"
else:
    print " - vi/vim     FOUND"

# gedit
p = subprocess.Popen("which gedit", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - gedit      NOT FOUND"
else:
    print " - gedit      FOUND"

# nedit
p = subprocess.Popen("which nedit", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - nedit      NOT FOUND"
else:
    print " - nedit      FOUND"

# kate
p = subprocess.Popen("which kate", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - kate       NOT FOUND"
else:
    print " - kate       FOUND"

# nano
p = subprocess.Popen("which nano", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - nano       NOT FOUND"
else:
    print " - nano       FOUND"

# leafpad
p = subprocess.Popen("which leafpad", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - leafpad    NOT FOUND"
else:
    print " - leafpad    FOUND"

# geany
p = subprocess.Popen("geany --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - geany      NOT FOUND"
else:
    print " - geany      FOUND"

# kwrite
p = subprocess.Popen("kwrite --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - kWrite     NOT FOUND"
else:
    print " - kWrite     FOUND"
    
print ""
print "PDF viewers:"

# evince
p = subprocess.Popen("which evince", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - evince     NOT FOUND"
else:
    print " - evince     FOUND"

# acroread
#p = subprocess.Popen("which acroread", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
#(output, err) = p.communicate()
#p_status = p.wait()
#if p_status!=0:
#    print " - Acrobat    NOT FOUND"
#else:
#    print " - Acrobat    FOUND"

# ghostview
p = subprocess.Popen("which gv", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - GhostView  NOT FOUND"
else:
    print " - GhostView  FOUND"

# xpdf
p = subprocess.Popen("which xpdf", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - Xpdf       NOT FOUND"
else:
    print " - Xpdf       FOUND"
    
# okular
p = subprocess.Popen("which okular", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - Okular     NOT FOUND"
else:
    print " - Okular     FOUND"

print ""
print "Image viewers/editors:"

# pinta
p = subprocess.Popen("pinta --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - Pinta      NOT FOUND"
else:
    words = output.split()
    if len(words)<1:
        print " - Pinta      FOUND      version UNKOWN"
    else:
        print " - Pinta      FOUND      version "+words[0]

# gpicview
p = subprocess.Popen("gpicview --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - gpicview   NOT FOUND"
else:
    words = output.split()
    if len(words)<2:
        print " - gpicview   FOUND      version UNKOWN"
    else:
        print " - gpicview   FOUND      version "+words[1]
	
print ""
print "Raspberry programs and detection:"

# RTIMULib
test1=True
try:
    from RTIMU import RTIMU
except:
    test1=False

if not test1:
    print " - Python RTIMU lib      NOT FOUND"
else:
    print " - Python RTIMU lib      FOUND"

# sense hat python libs
test1=True
try:
    from sense_hat import SenseHat
except:
    test1=False

if not test1:
    print " - Python SenseHat API   NOT FOUND"
else:
    print " - Python SenseHat API   FOUND"

# sense hat C++ libs
p = subprocess.Popen("sensehat-test", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p = subprocess.Popen("sensehat-test --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print     " - C++ SenseHat          NOT FOUND"
else:
    words = output.split()
    if len(words)<1:
        print " - C++ SenseHat          FOUND      version UNKOWN"
    else:
        print " - C++ SenseHat          FOUND      version "+words[0]

# sense hat C++ libs - dummy
p = subprocess.Popen("sensehat-test-dummy --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print     " - C++ SenseHat-dummy    NOT FOUND"
else:
    words = output.split()
    if len(words)<1:
        print " - C++ SenseHat-dummy    FOUND      version UNKOWN"
    else:
        print " - C++ SenseHat-dummy    FOUND      version "+words[0]

# sense hat C++ libs - root
p = subprocess.Popen("sensehat-test-root --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print     " - C++ SenseHat-root     NOT FOUND"
else:
    words = output.split()
    if len(words)<1:
        print " - C++ SenseHat-root     FOUND      version UNKOWN"
    else:
        print " - C++ SenseHat-root     FOUND      version "+words[0]

# test sense hat communication
test4=False
if test1:
    test4=True
    try:
        sense = SenseHat()
    except:
        test4=False

if not test4:
    print " - Link with SenseHat    FAILURE"
else:
    print " - Link with SenseHat    OK"
    
print "----------------------------------------------"
print ""

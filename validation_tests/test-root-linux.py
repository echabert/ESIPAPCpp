import os
import os
import tempfile
import subprocess
import glob
import shutil


location = os.path.abspath(os.path.dirname(__file__))


#####################################################################################################
# FUNCTION LAUNCHTEST
#####################################################################################################
def launchtest(mycommands):

    # Creating a tmp folder
    folder = tempfile.mkdtemp()
    print "Working in the folder: "+folder
    
    # Copy the source files in a tmp folder
    files = glob.glob(location+"/root/*.cpp")
    files.extend(glob.glob(location+"/root/*.h"))
    for item in files:
        dest = shutil.copyfile(item, folder+'/'+os.path.basename(item))

    # Loop over the tests
    item=0
    for line in mycommands:
        item+=1
        print "  * Test "+str(item)+": "+line[0]

        # launch the command line
        p = subprocess.Popen(line[1], stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, cwd=folder)
        (output, err) = p.communicate()
        p_status = p.wait()
        if p_status!=0:
            print "            -> FAILURE: error during the building"
            continue

        # check the produced file
        if not os.path.isfile(folder+'/'+line[2]):
            print "            -> FAILURE: the produced file "+line[2]+" is not found"
            continue

        # stop if library or object file
        if line[2].endswith('.o') or line[2].endswith('.a') or line[2].endswith('.so'):
            print "            -> OK"
            continue

        # setting LD_LIBRARY_PATH
        old  = os.environ.get('LD_LIBRARY_PATH')
        old2 = os.environ.get('DYLD_LIBRARY_PATH')
        if line[5]:
            if old==None:
                os.environ['LD_LIBRARY_PATH']=folder+'/'
            else:
                os.environ['LD_LIBRARY_PATH']=old+'/:'+folder+'/'
            if old2==None:
                os.environ['DYLD_LIBRARY_PATH']=folder+'/'
            else:
                os.environ['DYLD_LIBRARY_PATH']=old2+'/:'+folder+'/'

        # execute the produced file
        p = subprocess.Popen('./'+line[2], stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, cwd=folder)
        (output, err) = p.communicate()
        p_status = p.wait()
		
        # go back to old LD_LIBRARY_PATH		
        if line[5]:
            if old!=None:
                os.environ['LD_LIBRARY_PATH']=old
            if old2!=None:
                os.environ['DYLD_LIBRARY_PATH']=old2

        # result
        if p_status!=line[3]:
            print "            -> FAILURE: error during the execution of the generated file"
            continue
        
        # look inside the output display
        if line[4]=='':
            print "            -> OK"
            continue

        else:
            if output.find(line[4])!=-1:
                print "            -> OK"
                continue
            else:
                print "            -> FAILURE: not found the pattern inside the output"
                continue
                 
    #os.removedirs(folder)




#####################################################################################################
# MAIN PROGRAM
#####################################################################################################
    
print ""
print "Detection of C++ compilers:"

isgpp = False
isclang = False
isroot = False

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
    isgpp=True


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
    isclang=True


print ""
print "Detection of ROOT:"

# root
p = subprocess.Popen("root-config --version", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
(output, err) = p.communicate()
p_status = p.wait()
if p_status!=0:
    print " - Root       NOT FOUND"
else:
    words = output.split()
    if len(words)<1:
        print " - Root       FOUND      version UNKOWN"
    else:
        print " - Root       FOUND      version "+words[0]
    isroot=True

if isroot:
    p = subprocess.Popen("root-config --cflags", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
    (output, err) = p.communicate()
    p_status = p.wait()
    if p_status!=0:
        print "   cflags:    NOT FOUND"
        isroot=False
    else:
        words = output.split()
        cflags = ' '.join(words)
        print "   cflags:    "+cflags

if isroot:
    p = subprocess.Popen("root-config --libs", stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
    (output, err) = p.communicate()
    p_status = p.wait()
    if p_status!=0:
        print "   libs:      NOT FOUND"
        isroot=False
    else:
        words = output.split()
        libs = ' '.join(words)
        print "   libs:      "+libs

    
print ""
print "Check ROOT+g++:"
if isroot and isgpp:
    # FORMAT
    # [ Test_name  Command_line  Produced_exectutable  returned_value  pattern_to_look_for  add_folder_to_lD_lIBRARY_PATH]
    commands_gpp = [ ['the simpliest program','g++ '+cflags+' basic.cpp '+libs+' -o basic','basic',42,'BEGIN Test',False],\
                     ['creating an histogram','g++ '+cflags+' histo.cpp '+libs+' -o histo','histo',42,'END Test',False] ]
    launchtest(commands_gpp)

print ""
print "Check ROOT+Clang:"
if isroot and isclang:
    # FORMAT
    # [ Test_name  Command_line  Produced_exectutable  returned_value  pattern_to_look_for  add_folder_to_lD_lIBRARY_PATH]
    commands_clang = [ ['the simpliest program','g++ '+cflags+' basic.cpp -lstdc++ '+libs+' -o basic','basic',42,'BEGIN Test',False],\
                     ['creating an histogram','g++ '+cflags+' histo.cpp -lstdc++ '+libs+' -o histo','histo',42,'END Test',False] ]
    launchtest(commands_clang)



print ""


import os
import os
import tempfile
import subprocess
import glob
import shutil


# FORMAT
# [ Test_name  Command_line  Produced_exectutable  returned_value  pattern_to_look_for  add_folder_to_lD_lIBRARY_PATH]
commands_gpp = [ ['the simpliest program','g++ basic.cpp -o basic','basic',42,'',False],\
                 ['using the standard library','g++ std.cpp -o std','std',42,'END Test',False],\
                 ['creating an object file','g++ -c -o file2.o file2.cpp','file2.o',42,'END Test',False],\
                 ['building project with several files','g++ file1.cpp file2.o -o several1','several1',42,'END Test',False],\
                 ['creating a static library','ar rvs file2.a file2.o','file2.a',42,'END Test',False],\
                 ['building a project with a static library','g++ file1.cpp file2.a -o several2','several2',42,'END Test',False],\
                 ['creating a dynamic library','g++ -shared -o libfile2.so file2.o','libfile2.so',42,'END Test',False],\
                 ['building a project with a dynamic library','g++ file1.cpp -L./ -lfile2 -o several3','several3',42,'END Test',True] ]


commands_clang = [ ['the simpliest program','clang basic.cpp -o basic','basic',42,'',False],\
                 ['using the standard library','clang -lstdc++ std.cpp -o std','std',42,'END Test',False],\
                 ['creating an object file','clang -c -o file2.o file2.cpp','file2.o',42,'END Test',False],\
                 ['building project with several files','clang -lstdc++ file1.cpp file2.o -o several1','several1',42,'END Test',False],\
                 ['creating a static library','ar rvs file2.a file2.o','file2.a',42,'END Test',False],\
                 ['building a project with a static library','clang -lstdc++ file1.cpp file2.a -o several2','several2',42,'END Test',False],\
                 ['creating a dynamic library','clang -lstdc++ -shared -o libfile2.so file2.o','libfile2.so',42,'END Test',False],\
                 ['building a project with a dynamic library','clang file1.cpp -lstdc++ -L./ -lfile2 -o several3','several3',42,'END Test',True] ]


location = os.path.abspath(os.path.dirname(__file__))




#####################################################################################################
# FUNCTION LAUNCHTEST
#####################################################################################################
def launchtest(mycommands):

    # Creating a tmp folder
    folder = tempfile.mkdtemp()
    print "Working in the folder: "+folder
    
    # Copy the source files in a tmp folder
    files = glob.glob(location+"/gpp/*.cpp")
    files.extend(glob.glob(location+"/gpp/*.h"))
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

if isgpp:
    print ""
    print "Launching test for g++"
    launchtest(commands_gpp)

if isclang:
    print ""
    print "Launching test for clang"
    launchtest(commands_clang)

print ""


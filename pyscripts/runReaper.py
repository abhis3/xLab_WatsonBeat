from __future__ import print_function
import os
import sys
import time
import commands
import subprocess


if __name__ == '__main__' :
    fname = sys.argv[1]
    dirname = sys.argv[2]
    reaperDir = sys.argv[3]


    fnameNoExt = fname.replace ( ".zip", "")
    # remove directory if it exists
    cmd = "rm -rf " + dirname + "/" + fnameNoExt
    #print ( "remove directory if it exists: ", cmd )
    os.system ( cmd )

    # create directory
    cmd = "mkdir " +  dirname + "/" + fnameNoExt
    #print ( "create directory: ", cmd )
    os.system ( cmd )

    # mv zip file to directory
    #cmd = "mv " +  dirname + "/" + fname + " " + dirname + "/" + fnameNoExt
    ##print ( "mv zip file: ", cmd )
    #os.system ( cmd )

    # change working directories
    os.chdir(dirname + "/" + fnameNoExt)
    #retval = os.getcwd()
    #print ( "current working directory:", retval)

    #write config file
    zipDir   = dirname + "/" + fnameNoExt
    configFname = reaperDir + "/config"
    cmd = "echo " + zipDir + " > " + configFname
    #print ( "Create config file for reascript: ", cmd)
    os.system(cmd)

    #unzip files
    cmd = "unzip " + dirname + "/" + fname
    #print ( "Unzip file: ", cmd )
    os.system ( cmd )

    # remove project if it exists
    cmd = "rm -rf " + reaperDir + "/WatsonBeat-" + fnameNoExt + ".RPP"
    #print ( "remove project if it exists: ", cmd )
    os.system ( cmd )

    # remove mp3 if it exists
    cmd = "rm -rf " + reaperDir + "/WatsonBeat-" + fnameNoExt + ".mp3"
    #print ( "remove mp3 if it exists: ", cmd )
    os.system ( cmd )

    # remove render flags if they exist
    cmd = "rm -rf " + reaperDir + "/WatsonBeat-" + fnameNoExt + ".startRendering"
    #print ( "remove render flags if they exists: ", cmd )
    os.system ( cmd )
    cmd = "rm -rf " + reaperDir + "/WatsonBeat-" + fnameNoExt + ".renderComplete"
    #print ( "remove render flags if they exists: ", cmd )
    os.system ( cmd )


    #create reaper project by saving from empty project
    cmd = "cp " + reaperDir + "/WatsonBeatEmptyProject.RPP" + " " + reaperDir + "/WatsonBeat-" + fnameNoExt + ".RPP"
    #print ( "Create project:", cmd)
    os.system(cmd)

    # call reaper
    reaperCmd = "/Applications/REAPER64.app/Contents/MacOS/REAPER  " + reaperDir + "/WatsonBeat-" + fnameNoExt + ".RPP"
    #print ( "Call Reaper:", reaperCmd)
    #os.system(cmd)


    newProc = os.fork()
    if ( newProc == 0 ) :
        #print ( "Inside Child process" )
        output = subprocess.check_output ( reaperCmd, shell=True )
        #print ( "output: ", output )
    else :
        #print ( "Inside Parent process" )

        timeout = 60
        fileRendered = False
        wbOutputFile = reaperDir + "/WatsonBeat-" + fnameNoExt + ".mp3"
        wbOutputFile = reaperDir + "/WatsonBeat-" + fnameNoExt + ".renderComplete"
        startRendering = reaperDir + "/WatsonBeat-" + fnameNoExt + ".startRendering"

        for i in range( timeout ) :
            #print ( "time: ", i )
            #print ( wbOutputFile )
            time.sleep( 1 )
            if ( os.path.exists(startRendering) ) :
                #print ( "Start Rendering: ", i )
                time.sleep( 6 )
                fileRendered = True
                break

            if (  os.path.exists(wbOutputFile) ) :
                #print ( "Finish Rendering: ", i )
                fileRendered = True
                break
                #else :
                #     print ( "File Not Found" )

        if ( not fileRendered ) :
            sys.exit(-1)
        print ( 100 )

from __future__ import print_function
import sys
import commands

def getMp3Id ( mood, dirname, ftype ) :

    lsCmd = "ls -t " + dirname + "/" + mood + "*." + ftype

    #lsCmd = "ls -t " + dirname + "/" + mood + "*.mp3"
    #print ( lsCmd)
    lsVal = commands.getoutput(lsCmd)
    if ( lsVal.endswith("No such file or directory")) :
        return -1

    #print ( lsVal)
    data = lsVal.split()

    lastWrittenFile = data[0].replace(dirname, "",  1)
    #print("1: ", data[0], lastWrittenFile)

    lastWrittenFile = lastWrittenFile.replace( ".mp3", "", 1)
    #print("2: ", data[0], lastWrittenFile)
    lastWrittenFile = lastWrittenFile.replace( "/", "", 1)
    #print("3: ", data[0], lastWrittenFile)
    id = lastWrittenFile.replace( mood+"-", "", 1)

    return id

    print(data[0], lastWrittenFile)
    print(type(data))

if __name__ == '__main__' :

    mood = sys.argv[1]
    dirname = sys.argv[2]
    fType = sys.argv[3]

    id = getMp3Id ( mood, dirname, fType)
    print (id)




    #dirname = sys.argv[2]

    #id = getMp3Id ( mood, dirname )
    #print ( "Id", id)

    #id = getMp3Id ( "spooky" , "/Users/jmukund/Repo/Electron/WatsonBeatDesktopApp/app/mp3/")

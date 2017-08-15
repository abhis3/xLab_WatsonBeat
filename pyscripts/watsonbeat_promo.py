import os
import sys
import math
import random
import collections



#user = "Richard"
startScript = True
#user = "jmukund"


#importDirectory = "/Users/" + user + "/Repo/wbRLRBM/src/"

Kontakt5     = "Kontakt 5 (Native Instruments GmbH) (8 out)"
Kontakt5_16  = "Kontakt 5 (Native Instruments GmbH) (16 out)"
Massive      = "Massive (Native Instruments GmbH )"
Battery      = "Battery 4 (Native Instruments GmbH)"
Omnisphere   = "Omnisphere (Spectrasonics)"
GuitarRig    = "Guitar Rig 5 (Native Instruments GmbH)"
Play         = "Play (East West) (2->18ch)"


# set a default volume for all the instruments.
# volume for the different instruments will be set at the preset files
#volume = random.uniform ( 0.35, 0.5 )
volume = 0.35
Movement = collections.OrderedDict()

proj, projectNameExt, buf_sz = RPR_GetProjectName(1, 1, 100)
projectName = projectNameExt.replace ( ".RPP", "",  1)
#udid = projectName.replace ( "WatsonBeatProject", "",  1)

projectPath, bufSz = RPR_GetProjectPath("", 512)
configFile = projectPath + "/config"

#RPR_ShowConsoleMsg ( projectName + "\n" )
#RPR_ShowConsoleMsg ( projectPath + "\n" )
#RPR_ShowConsoleMsg ( configFile + "\n")

file = open (configFile, 'r')
importDirectory = file.readline ()
file.close ()
importDirectory = importDirectory.strip() + "/"
#RPR_ShowConsoleMsg ( importDirectory)



def SetProjectTempoAndTimeSignature (tempo, num, den, measure) :

    RPR_SetTempoTimeSigMarker( 0, -1, -1, measure-1, 0, tempo, num, den, False )




def parseCompositionSettings ( finName ) :

    fin = open ( finName, mode='r' )

    for line in fin :
        line = line.rstrip()

        #print ( "line: ", line )

        if ( line.startswith ( "Movement" ) ) :
            data = line.split ()
            for item in range(0, len(data), 2)  :
                if ( data[item] == 'Movement' ) :
                    mvNum = int(data[item+1] )
                    Movement[mvNum] = collections.OrderedDict()
                    Movement[mvNum]['Sections'] = collections.OrderedDict()

                elif ( data[item] == 'NumSections' ) :
                    Movement[mvNum]['numSections'] = int(data[item+1] )

                elif ( data[item] == 'Mood' ) :
                    Movement[mvNum]['mood'] = data[item+1]

                elif ( data[item] == 'type' ) :
                    Movement[mvNum]['type'] = data[item+1]



        elif ( line.startswith ( "SectionNum" ) ) :

            data = line.split ()
            for item in range(0, len(data), 2)  :
                #print ( item, data[item],  data[item+1] )
                if ( data[item] == 'SectionNum' ) :
                    secNum = int(data[item+1] )
                    Movement[mvNum]['Sections'][secNum] = collections.OrderedDict()

                elif ( data[item] == 'NumPhrases' ) :
                    numPhrases = int(data[item+1])
                    Movement[mvNum]['Sections'][secNum]['numPhrases'] = numPhrases
                    Movement[mvNum]['Sections'][secNum]['Phrases'] = collections.OrderedDict()

                elif ( data[item] == 'NumChords' ) :
                    numChords = int(data[item+1])
                    Movement[mvNum]['Sections'][secNum]['numChords'] = numChords

        elif ( line.startswith ( "SectionLayers" ) ) :

            data = line.split ()
            lyr = []
            layers = data[1].replace ( "[", "" )
            layers = layers.replace ( "]", "" )
            layers = layers.replace ( ",", " " )
            layers = layers.replace ( "'", "" )
            layers = layers.split ( )
            for l in layers :
                lyr.append ( l )
            Movement[mvNum]['Sections'][secNum]['layers'] = lyr
            #print ( "SecId", secNum, "layers:", lyr, Movement[mvNum]['Sections'][secNum]['layers'] )
            #print()

        elif ( line.startswith ( "Phrase" ) ) :

            data = line.split ()
            for item in range(0, len(data), 2)  :
                #print ( item, data[item],  data[item+1] )
                if ( data[item] == 'PhraseNum' ) :
                    phNum = int(data[item+1] )
                    Movement[mvNum]['Sections'][secNum]['Phrases'][phNum] = collections.OrderedDict()

                elif ( data[item] == 'StartClk' ) :
                    startClk = int(data[item+1] )
                    Movement[mvNum]['Sections'][secNum]['Phrases'][phNum]['startClk'] = startClk

                elif ( data[item] == 'EndClk' ) :
                    endClk = int(data[item+1] )
                    Movement[mvNum]['Sections'][secNum]['Phrases'][phNum]['endClk'] = endClk

                elif ( data[item] == 'Layers' ) :
                    layers = (data[item+1] )
                    layers = layers.replace ( "]" , "" )
                    layers = layers.replace ( "[" , "" )
                    layers = layers.replace ( "'", "" )
                    layers = layers.replace ( "," , " " )


                    layers = layers.split ( )
                    lyr = []
                    for l in layers :
                        lyr.append ( l )
                    Movement[mvNum]['Sections'][secNum]['Phrases'][phNum]['layers'] = lyr




def getLayersForSection ( mvNum, secNum ) :
    #print ( "Layers for Movement: ", mvNum, "Section: ", secNum , Movement[mvNum]['Sections'][secNum]['layers'] )
    #print()
    return Movement[mvNum]['Sections'][secNum]['layers']


def getLayersForPhrase ( mvNum, secNum, phNum ) :
    #print ( "Layers for Movement: ", mvNum, "Section: ", secNum , "Phrase: ", phNum, Movement[mvNum]['Sections'][secNum]['Phrases'][phNum]['layers'] )
    #print()
    return Movement[mvNum]['Sections'][secNum]['Phrases'][phNum]['layers']




'''

def ReadCompositionSettings () :
    #test = RPR_ShowConsoleMsg ("test")
    #finName = importDirectory + "\\CompositionSettings"   #Windows
    finName = importDirectory + "/CompositionSettings"    #Mac
    fin = open ( finName, mode='r' )

    compositionSettings = collections.OrderedDict()
    movementSettings = collections.OrderedDict()

    files = {}
    allLayerNames = []
    layerNames = []#set()
    sections = []
    sectionCounter = -1
    for line in fin :

        line = line.rstrip()
        layerNames = []#set()

        if ( line.startswith ( "Phrase" ) ) :
            data = line.split()

            for layers in range (9, len(data)) :
                layerNames.insert(layers-9,data[layers])

        if ( line.startswith ( "Phrase 0") ) :
            sectionCounter = sectionCounter + 1
            sections.insert(sectionCounter, sectionCounter)
            files.update({str(sectionCounter): layerNames}


    for x, y in files.items() :
        test = RPR_ShowConsoleMsg ("SECTION #" + str(x) + ": " + str(y) + "\n")
    return test
#WB_Mvmt0_Sec0_bass1

    for line in fin :
        line = line.rstrip()

        #print ( "line: ", line )

        if ( line.startswith ( "Movement" ) ) :

            data = line.split ()
            for item in range(0, len(data), 2)  :
                if ( data[item] == 'Movement' ) :
                    mvNum = int(data[item+1] )
                    compositionSettings[mvNum] = collections.OrderedDict()
                    movementSettings[mvNum] = collections.OrderedDict()
                elif ( data[item] == 'Mood' ) :
                    movementSettings[mvNum]['mood'] = data[item+1]
                elif ( data[item] == 'Element' ) :
                    movementSettings[mvNum]['element'] = data[item+1]
                elif ( data[item] == 'Genre' ) :
                    movementSettings[mvNum]['genre'] = data[item+1]

        elif ( line.startswith ( "SectionNum" ) ) :

            data = line.split ()
            for item in range(0, len(data), 2)  :
                #print ( item, data[item],  data[item+1] )
                if ( data[item] == 'SectionNum' ) :
                    secNum = int(data[item+1] )
                    compositionSettings[mvNum][secNum] = collections.OrderedDict()
                    movementSettings[mvNum][secNum]    = collections.OrderedDict()
                elif ( data[item] == 'NumPhrases' ) :
                    numPhrases = int(data[item+1])
                    for ph in range(numPhrases) :
                        compositionSettings[mvNum][secNum][ph] = {'clock': 0, 'mute': False }
                        #print ( "Section: ", secNum, "Phrase Num: ", ph )
                elif ( data[item] == 'Type' ) :
                    movementSettings[mvNum][secNum]['type'] = data[item+1]
                elif ( data[item] == 'tse' ) :
                    movementSettings[mvNum][secNum]['tse'] = data[item+1]
                elif ( data[item] == 'tempo' ) :
                    movementSettings[mvNum][secNum]['tempo'] = data[item+1]

        elif ( line.startswith ( "StartofSection" ) ) :

            data = line.split ()
            for item in range(0, len(data), 2)  :
                #print ( "SoS: ", item, data[item],  data[item+1] )
                if ( data[item] == 'StartofSection' ) :
                    secNum = int(data[item+1] )
                    #print ( "Sec Num: ", secNum )
                elif ( data[item] == 'PhraseNum' ) :
                    phNum = int(data[item+1] )
                    #print ( "Phrase Num: ", phNum )
                elif ( data[item] == 'Clock' ) :
                    compositionSettings[mvNum][secNum][phNum]['clock'] = int(data[item+1] )
                elif ( data[item] == 'Mute' ) :
                    compositionSettings[mvNum][secNum][phNum]['mute'] = data[item+1]

    fin.close()

    print()
    print()
    for mvNum in compositionSettings :
        print ( "Movement: ", mvNum, "Mood: ", movementSettings[mvNum]['mood'], "Element: ", movementSettings[mvNum]['element'], "Genre: ", movementSettings[mvNum]['genre'] )
        for sec in compositionSettings[mvNum] :
            print ( "Section: ", sec, "Type: ",  movementSettings[mvNum][sec]['type'], "Time Signature: ",  movementSettings[mvNum][sec]['tse'], "Tempo: ",  movementSettings[mvNum][sec]['tempo'] )
            for ph in compositionSettings[mvNum][sec] :
                print ( "phrase: ", ph, "Clock: ", compositionSettings[mvNum][sec][ph]['clock'], "Mute: ", compositionSettings[mvNum][sec][ph]['mute'] )

    return ( compositionSettings, movementSettings )
    '''




def CreateLayer (file, type, presets, midiFX, audioFX, volume) :

    preset = random.choice ( presets )
    instrumentName = preset.split ("_", 1)
    instrument = getInstrumentType (instrumentName)

    # put clock to 0
    RPR_SetEditCurPos (0, True, True)
    # inserts an empty track with no instrument added to it. 0 indicates track is inserted at 0th position
    RPR_InsertTrackAtIndex (0, True)
    curTrack = RPR_GetTrack (0, 0)

    RPR_Main_OnCommand (40297, 1) # unselects all tracks
    RPR_Main_OnCommand (40939, 1) # selects first track


    for f in range (0, len(file)) :
        RPR_InsertMedia (file[f], 0) # inserts MIDI on new track
        RPR_SetEditCurPos (0, True, True)

    count = 0

    #inserts MIDI FX onto track
    if midiFX != "" :
        for fxName, fxPreset in midiFX.items() :
            RPR_TrackFX_GetByName (curTrack, fxName, True)
            RPR_TrackFX_SetPreset (curTrack, count, fxPreset)
            count = count + 1

    # the first track id will always be 0
    RPR_TrackFX_GetByName (curTrack, instrument, True)  # adds instrument=kontakt5 on to the newly created track
    RPR_TrackFX_SetPreset (curTrack, count, preset) # set preset on the instrument
    count = count + 1

    #inserts AUDIO FX onto track
    if audioFX != "" :
        for fxName, fxPreset in audioFX.items() :
            RPR_TrackFX_GetByName (curTrack, fxName, True)
            RPR_TrackFX_SetPreset (curTrack, count, random.choice(fxPreset))
            count = count + 1

    #RPR_TrackFX_GetByName (curTrack, "ReaEQ (Cockos)", True)
    #RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 1, eq)

    #if eq == "HPF_melody" :
    #    ParameterRandomization ( 1, 130, 235, 1, 0 ) #HiPass Filter Frequency

    RPR_SetMediaTrackInfo_Value (curTrack, "D_VOL", volume)
    RenameTrack (0, type)



def GroupAllTracksBelowSelectedTrack (selectedTrack) :

    groupTrack = selectedTrack + 40939 # converts to Reaper Action ID
    RPR_Main_OnCommand (40297, 1)      # unselects all tracks
    RPR_Main_OnCommand (groupTrack, 1) # selects track passed in (selectedTrack)
    RPR_Main_OnCommand (1041, 1)       # makes current track a group folder and groups all tracks below it




def GroupNumOfTracksBelowSelectedTrack (selectedTrack, tracks) :

    #folder cycle 1 time on next vi track
    #folder cycle 2 times on (last track in phrase)

    groupTrack  = selectedTrack + 40939 # converts to Reaper Action ID
    numOfTracks = tracks + 40939

    RPR_Main_OnCommand (40297, 1)      # unselects all tracks
    RPR_Main_OnCommand (groupTrack, 1) # selects track passed in (selectedTrack)
    RPR_Main_OnCommand (1041, 1)       # makes current track a group folder and groups all tracks below it

    for t in range ( 0, 2 ) :
        RPR_Main_OnCommand (40297, 1)      # unselects all tracks
        RPR_Main_OnCommand ( numOfTracks, 1 )
        RPR_Main_OnCommand (1041, 1)       # makes current track a group folder and groups all tracks below it







def CreateInstrumentTrack () :

    if mood == epic :
        presets = ["WB_Kontakt5_percMelody", "WB_Majestica_stringsBrassPercMelody", "WB_Kontakt5_Majestica_stringsMelody", "WB_Kontakt5_Majestica_stringsMelody", "WB_Kontakt5_Majestica_wwArpStringsMel", "WB_Majestica_stringsBrassMelody"]
        #RPR_ShowConsoleMsg (str(presets[1]))
    elif element == "Water" :
        presets = ["water_mel1", "water_mel2", "water_mel3", "water_mel4"]

    maxNumberOfInstruments = int ((energy / 25) + 2)


    #RPR_ShowConsoleMsg ("ENERGY: " + str(energy) + ",  Max#Instruments: " + str(maxNumberOfInstruments))
    #random.shuffle (presets)
    preset                 = random.choice (presets)
    numOfInstruments       = random.randint (1, maxNumberOfInstruments)

    for x in range (0, 4) : #numOfInstruments) :

        preset = random.choice (presets)
        RPR_SetEditCurPos (0, True, True) # sets scroll cursor to the beginning 0 on timeline
        RPR_InsertTrackAtIndex (0, True)

        RPR_Main_OnCommand (40297, 1) # unselects all tracks
        RPR_Main_OnCommand (40939, 1) # selects first track

        instrument = Kontakt5
        volume     = .6

        RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), instrument, True)
        RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 0, preset)
        RPR_SetMediaTrackInfo_Value (RPR_GetTrack (0, 0), "D_VOL", volume)

        trackName = "MELODY_" + str(x)
        RenameTrack (0, trackName)

    return ( numOfInstruments )




def ImportMelodyLayer (file) :

    RPR_SetEditCurPos (0, True, True) # sets scroll cursor to the beginning 0 on timeline
    RPR_InsertTrackAtIndex (0, True)

    RPR_Main_OnCommand (40297, 1) # unselects all tracks
    RPR_Main_OnCommand (40939, 1) # selects first track

    RPR_InsertMedia (file, 0) # inserts MIDI on new track.. Maybe change 1 to 0???

    instrument = Kontakt5
    volume     = .225




def OrganizeTracks (numOfMelodyTracks) :

    numOfTracks = RPR_CountTracks (0)
    #RPR_ShowConsoleMsg ("# of mel tracks: " + str(numOfMelodyTracks) + " \n")


    #organize midi tracks under mel tracks in this FOR loop
    #for mel in range ( 1, numOfMelodyTracks ) :
    #randomize / shuffle the list and then go in order

    random.shuffle ( sectionTypesMelody )

    for uniqueTypes in range ( 0, len(sectionTypesMelody) ) :

        # randomly choose section/type
        #randType = sectionTypesMelody [random.randint ( 0, len(sectionTypesMelody) )]

        randType = sectionTypesMelody[uniqueTypes]
        #RPR_ShowConsoleMsg ( sectionTypesMelody[1] )
        melList = []



        numOfTracks = RPR_CountTracks (0)


        for trr in range ( 0, numOfTracks ) :

            trId = RPR_GetTrack (0, trr)
            name = RPR_GetSetMediaTrackInfo_String (trId, "P_NAME", " ", False)
            RPR_Main_OnCommand (40297, 1)

            if name[3] == randType :
                RPR_SetTrackSelected( trId, True ) # selects that track
                RPR_Main_OnCommand (40337, 1)      # cut track
                RPR_Main_OnCommand (40297, 1)      # unselects all tracks


            melList = []
            numOfTracks = RPR_CountTracks (0)
            for m in range ( 0, numOfTracks ) :

                mId = RPR_GetTrack (0, m)
                melName = RPR_GetSetMediaTrackInfo_String (mId, "P_NAME", " ", False)
                #RPR_ShowConsoleMsg (melName[3])

                # return track number
                if melName[3][0] == "M" :
                    melList.append (m)

                #numOfTracks = RPR_CountTracks (0)
                #RPR_ShowConsoleMsg ( str(melList[uniqueTypes]) + "\n")
                lengthMelList = len(melList)
                #RPR_ShowConsoleMsg (str(lengthMelList) + ": " + str(melList) + "\n")

            if name[3] == randType :
                randMelTrack = melList[random.randint ( 0, lengthMelList-1 )]
                RPR_Main_OnCommand (40297, 1)      # unselects all tracks


                #if uniqueTypes <= len(melList) :
                #RPR_SetTrackSelected ( RPR_GetTrack (0, melList[uniqueTypes]), True )
                RPR_Main_OnCommand (40058, 1) # paste
                #numOfTracks = RPR_CountTracks (0)

       # RPR_ShowConsoleMsg (melList)









def Arrange () :

    for sect in range ( 1, numSections + 1 ) :
        numPhrases  = len(compositionSettings[0][sect])
        sectionMute = compositionSettings[0][sect][0]["mute"]    #finds mute for beginning of section
        sectionTypesAll.add(movementSettings[0][sect]["type"])

        if sectionMute == "False" :
            sectionTypesMelody.add(movementSettings[0][sect]["type"])


        for phr in range ( 0, numPhrases ) :
            phraseMute = compositionSettings[0][sect][phr]["mute"] #finds mute for beginning of phrase

            if phraseMute == "False" :
                importMIDIMelody = importDirectory + "WB_Mvmt0_mel5_Sec" + str(sect) + "_Phrase" + str(phr) + ".mid"
                ImportMelodyLayer (importMIDIMelody)
                RenameTrack (0, movementSettings[0][sect]["type"])



        sectionTempo = float (movementSettings[0][sect]["tempo"])
        tse          = movementSettings[0][sect]["tse"]
        tseNum       = int (ord(tse[0]) - 48)
        tseDen       = int (ord(tse[2]) - 48)
        clock        = compositionSettings[0][sect][0]['clock']
        startMeasure = (clock / tseNum / 480 ) + 1

        #SetProjectTempoAndTimeSignature (sectionTempo, tseNum, tseDen, startMeasure)

        sectionType = movementSettings[0][sect]["type"]


    #RPR_ShowConsoleMsg ( sectionTypesAll )



        #if sectionMute == "False" :
            #RPR_ShowConsoleMsg ( "creating virtual instrument track\n" )
            #numOfInstruments = CreateInstrumentTrack ()
            #RPR_ShowConsoleMsg ( numPhrases )
            #GroupNumOfTracksBelowSelectedTrack (0, numPhrases)




def Routing (sectionTypesMelody, numOfInstruments) :

    numOfTracks = RPR_CountTracks (0)

    for uniqueTypes in range ( 0, len(sectionTypesMelody) ) :

        randType = sectionTypesMelody[uniqueTypes]
        sendTrack = RPR_GetTrack (0, random.randint (0, numOfInstruments))

        #RPR_ShowConsoleMsg ( randType + ", " )
        for tr in range ( 0, numOfTracks ) :

            trId = RPR_GetTrack (0, tr)
            name = RPR_GetSetMediaTrackInfo_String (trId, "P_NAME", " ", False)
            RPR_Main_OnCommand (40297, 1)

            curTrack  = RPR_GetTrack (0, tr)

            #RPR_ShowConsoleMsg (name[3] )#+ ": " + randType "\n")

            if name[3] == randType :
                RPR_CreateTrackSend (curTrack, sendTrack)

                #send into one of the mel tracks randomly







def ImportGuitarLayer (file) :

    guitarPresets = ["guitar_strum1", "guitar_strum2", "guitar_strum3", "guitar_strum4"]


    preset = guitarPresets [random.randint (0, 3)]

    RPR_SetEditCurPos (0, True, True) # sets scroll cursor to the beginning 0 on timeline
    RPR_InsertTrackAtIndex (0, True)

    RPR_Main_OnCommand (40297, 1) # unselects all tracks
    RPR_Main_OnCommand (40939, 1) # selects first track

    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "midi_transpose", True)
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 0, "guitar_transpose_24va")

    RPR_InsertMedia (file, 0) # inserts MIDI on new track.. Maybe change 1 to 0???

    instrumentGuitar = Kontakt5
    volume        = .265

    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), instrumentGuitar, True)
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 1, preset)
    RPR_SetMediaTrackInfo_Value (RPR_GetTrack (0, 0), "D_VOL", volume)

    #adds fx to BASS track
    if mood == angrySimple or mood == angrySemiComplex or mood == "angrysimple" or mood == "angrycomplex" :
        RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), GuitarRig, True)
        RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 1, "angry_bass_fx")
        RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "ReaEQ (Cockos)", True)
        RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 2, "EQ_bass")

    else :
        RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "ReaEQ (Cockos)", True)
        RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 2, "EQ_bass")




def GroupTracksBelowSelectedTrack (selectedTrack) :
    #40939 = select Track1

    groupTrack = selectedTrack + 40939 # converts to Reaper Action ID
    RPR_Main_OnCommand (40297, 1)      # unselects all tracks
    RPR_Main_OnCommand (groupTrack, 1) # selects track passed in (selectedTrack)
    RPR_Main_OnCommand (1041, 1)       # makes current track a group folder and groups all tracks below it



def CreateSubmixTrack () :
    '''
    Creates Submix track. All tracks get routed into this. Adds Compressor/EQ/Reverb/Limiter FX chain to this track.
    '''

    RPR_InsertTrackAtIndex (0, 0)
    GroupTracksBelowSelectedTrack (0)
    RenameTrack (0, "SUBMIX")

    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "ReaComp (Cockos)", True)
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "ReaEQ (Cockos)", True)
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "ReaVerbate (Cockos)", True)
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "soft_clipper", True)
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "masterLimiter", True)


    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 0, "submix_comp")
    ParameterRandomization ( 0, 5, 10, 0, 1 )      #Ratio
    ParameterRandomization ( 0, 25, 80, 0, 2 )     #Attack time
    ParameterRandomization ( 0, 10, 20, 0, 3 )     #Release time
    ParameterRandomization ( 0, 500, 1500, 0, 13 ) #RMS size

    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 1, "submix_eq")
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 2, "submix_verb")
    ParameterRandomization ( 0, 400, 750, 2, 2 ) #Room Size
    ParameterRandomization ( 0, 350, 750, 2, 3 )  #Dampen factor
    ParameterRandomization ( 0, 500, 900, 2, 4 ) #Stereo Width
    ParameterRandomization ( 0, 400, 600, 2, 6 ) #Lowpass Filter
    ParameterRandomization ( 0, 3, 25, 2, 7 )    #Hipass Filter

    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 3, "submix_soft_clipper")

    if mood == epic :
        RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 4, "submix_orchestral_limiter")
    else :
        RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 4, "submix_limiter")





def ImportMidiFile (file) :

    RPR_SetEditCurPos (0, True, True) # sets scroll cursor to the beginning 0 on timeline
    RPR_InsertMedia   (file, 0) # inserts MIDI on new track.. Maybe change 1 to 0???



def RenameTrack (Id, name) :

    trackId = RPR_GetTrack (0, Id)
    RPR_GetSetMediaTrackInfo_String (trackId, "P_NAME", name, True)



def ParameterRandomization ( trackid, min, max, fxid, paramid ) :

    parameterValue = random.randint ( min, max ) * .001
    track          = RPR_GetTrack ( 0, trackid )
    RPR_TrackFX_SetParam ( track, fxid, paramid, parameterValue )




def setTempo () :

    if mood == romanticSimple or mood == romanticSemiComplex :
        tempo = random.randint ( 60, 76 )

    elif mood == "anthematic" :
        tempo = random.randint (84, 100)

    elif mood == "inspire" :
        tempo = random.randint (120, 136)

    elif mood == "bommarch" :
        tempo = random.randint (126, 136)

    elif mood == "popfunk" :
        tempo = random.randint (114, 124)

    elif mood == "propulsion" :
        tempo = random.randint (132, 140)

    elif mood == "peruvianwaltz" :
        tempo = random.randint (100, 130)

    RPR_SetTempoTimeSigMarker( 0, -1, 0, 0-1, 0, tempo, 4, 4, True )



def getMood () :
    '''
    get mood from the thematic knob file
    '''

    file = open ("/Users/" + user + "/Repo/DJWatson/ThematicKnob.txt", 'r')
    firstLine = file.readline ()
    mood = firstLine
    file.close ()
    return mood



def InitializeReaper () :
    '''
    this is needed to remove all tracks and then add new ones, everytime Reaper starts
    '''
    RPR_Main_OnCommand (40296, 1) # selects all tracks
    RPR_Main_OnCommand (40005, 1) # remove all tracks




def getInstrumentType (instrumentName) :

    #RPR_ShowConsoleMsg (instrumentName)
    if instrumentName[0].startswith ("Kontakt") :
        instrumentName = Kontakt5
    elif instrumentName[0].startswith ("Play") :
        instrumentName = Play
    elif instrumentName[0].startswith ("Omni") :
        instrumentName = Omnisphere
    elif instrumentName[0].startswith ("Massive") :
        instrumentName = Massive
    elif instrumentName[0].startswith ("Battery"):
        instrumentName = Battery

    return instrumentName






    preset = random.choice ( presets )
    instrumentName = preset.split ("_", 1)
    instrument = getInstrumentType (instrumentName)

    # put clock to 0
    RPR_SetEditCurPos (0, True, True)
    # inserts an empty track with no instrument added to it. 0 indicates track is inserted at 0th position
    RPR_InsertTrackAtIndex (0, True)
    curTrack = RPR_GetTrack (0, 0)

    RPR_Main_OnCommand (40297, 1) # unselects all tracks
    RPR_Main_OnCommand (40939, 1) # selects first track


    for f in range (0, len(file)) :
        RPR_InsertMedia (file[f], 0) # inserts MIDI on new track
        RPR_SetEditCurPos (0, True, True)

    count = 0

    #inserts MIDI FX onto track
    if midiFX != "" :
        for fxName, fxPreset in midiFX.items() :
            RPR_TrackFX_GetByName (curTrack, fxName, True)
            RPR_TrackFX_SetPreset (curTrack, count, fxPreset)
            count = count + 1

    # the first track id will always be 0
    RPR_TrackFX_GetByName (curTrack, instrument, True)  # adds instrument=kontakt5 on to the newly created track
    RPR_TrackFX_SetPreset (curTrack, count, preset) # set preset on the instrument
    count = count + 1

    #inserts AUDIO FX onto track
    if audioFX != "" :
        for fxName, fxPreset in audioFX.items() :
            RPR_TrackFX_GetByName (curTrack, fxName, True)
            RPR_TrackFX_SetPreset (curTrack, count, random.choice(fxPreset))
            count = count + 1

    #RPR_TrackFX_GetByName (curTrack, "ReaEQ (Cockos)", True)
    #RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 1, eq)

    #if eq == "HPF_melody" :
    #    ParameterRandomization ( 1, 130, 235, 1, 0 ) #HiPass Filter Frequency

    RPR_SetMediaTrackInfo_Value (curTrack, "D_VOL", volume)
    RenameTrack (0, type)




def StringArpSetParameters () :

    arpRate = random.choice ([5,8])
    ParameterRandomization ( 0, 1000/17*arpRate, 1000/17*arpRate, 0, 0 )

    if arpRate == 5 :
        repeatFactor = random.choice ([0,1,1,1,4,4])
    else :
        repeatFactor = random.choice ([0,0,0,1])

    ParameterRandomization ( 0, 1000/4*repeatFactor, 1000/4*repeatFactor, 0, 2 )

    octaveFactor = random.choice ([3,4,4,4,5])
    ParameterRandomization ( 0, 1000/8*octaveFactor, 1000/8*octaveFactor, 0, 1 )

    stepsFactor = random.choice ([0,1,2,3,4,5,6,7,8])
    ParameterRandomization ( 0, 1000/28*stepsFactor, 1000/28*stepsFactor, 0, 3 )




def WoodwindsOstinatoSetParamaters () :

    for currentInstrument in range ( 0, 2 ) :
        arpRate = random.choice ([5,8])
        ParameterRandomization ( 0, 1000/17*arpRate, 1000/17*arpRate, 0, currentInstrument )

    # if arpRate is 1/8 note
    if arpRate == 5 :
        repeatFactor = random.choice ([0,1,1,1,4,4])
    else :
        repeatFactor = random.choice ([0,0,0,1])




def RandomlyMuteTrack(tr) :

    muteChance = random.randint (0, 100)
    if muteChance <= 50 :
        RPR_SetMediaTrackInfo_Value( tr, "B_MUTE", True )






if __name__ == '__main__' :

    #finName = importDirectory + "/CompositionSettings"
    #mood = parseCompositionSettings ( finName )
    #RPR_ShowConsoleMsg (mood)

    if startScript == True :

        InitializeReaper ()

        finName = importDirectory + "/CompositionSettings"
        parseCompositionSettings ( finName )

        # to get number of sections in movement 0
        numSections = Movement[0]['numSections']

        # to get number of phrases in section 0 in movement 0
        numPhrases = Movement[0]['Sections'][0]['numPhrases']

        # to get the layers for section 3 in movement 0
        layers = getLayersForSection ( 0, 3 )

        mood = Movement[0]['mood']
        #RPR_ShowConsoleMsg (mood)

        romanticSimple        = "romantic_simple"
        romanticSemiComplex   = "romantic_semi_complex"
        epic                  = "anthematic"
        inspired              = "inspire"
        march                 = "bommarch"
        pop                   = "popfunk"
        propulsion            = "propulsion"
        peruvianWaltz         = "peruvianWaltz"

        # to get the layers for phrase 1 in section 4 in movement 0
        #layers = getLayersForPhrase ( 0, 4, 1 )



        melody     = []
        arpStrings = []
        doubleBass = []
        cello      = []
        viola      = []
        violin2    = []
        violin1    = []
        pianoLH    = []
        pianoRH    = []
        bassDrum   = []
        kickDrum   = []
        cymbals    = []
        snare      = []
        hiHat      = []
        bass1      = []
        bass2      = []
        fills      = []
        rhythm     = []



        #finds existing MIDI files for each layer and adds them to a list per each layer
        for section in range (0, numSections) :

            layers = getLayersForSection (0, section)

            for layer in range (0, len(layers)) :
                #RPR_ShowConsoleMsg (layers[layer] + '\n')


                if layers[layer] == 'mel5' :
                    melody.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_mel5.mid" )

                elif layers[layer] == 'arpStrings' :
                    arpStrings.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_arpStrings.mid" )

                elif layers[layer] == 'loStrings' :
                    doubleBass.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_loStrings_doubleBass.mid" )
                    cello.append      ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_loStrings_cello.mid" )

                elif layers[layer] == 'midStrings' :
                    viola.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_midStrings_viola.mid" )
                    violin2.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_midStrings_violin2.mid" )

                elif layers[layer] == 'hiStrings' :
                    violin1.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_hiStrings_violin1.mid" )

                elif layers[layer] == 'rightPiano' :
                    pianoRH.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_rightPiano.mid" )

                elif layers[layer] == 'leftPianoBass' :
                    pianoLH.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_leftPianoBass.mid" )

                elif layers[layer] == 'drumsBass' :
                    bassDrum.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_drumsBass.mid" )

                elif layers[layer] == 'drumsKick' :
                    kickDrum.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_drumsKick.mid" )

                elif layers[layer] == 'drumsKit' :
                    kickDrum.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_drumsKit.mid" )
                    fills.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_fillsForDrums.mid" )

                elif layers[layer] == 'drumsCymbalSwell' :
                    cymbals.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_drumsCymbalSwell.mid" )

                elif layers[layer] == 'drumsSnare' :
                    snare.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_drumsSnare.mid" )

                elif layers[layer] == 'drumsHihat' :
                    hiHat.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_drumsHihat.mid" )

                elif layers[layer] == 'fillsForDrums' :
                    fills.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_fillsForDrums.mid" )

                elif layers[layer] == 'drumsKitMarinera' :
                    kickDrum.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_drumsKitMarinera.mid" )

                elif layers[layer] == 'bass1' :
                    bass1.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_bass1.mid" )

                elif layers[layer] == 'bass2' :
                    bass2.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_bass2.mid" )

                elif layers[layer] == 'peruvianRhythmChords' or layers[layer] == 'rhythmChords' :
                    rhythm.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_peruvianRhythmChords.mid" )
                    rhythm.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_rhythmChords.mid" )


        #midi groups
        loStrings = cello + doubleBass
        hiStrings = violin1 + violin2 + viola
        midStrings = violin2 + viola
        drums = kickDrum



        if mood == "bommarch" :

            bassPresets = ["Kontakt5_March_bass1", "Kontakt5_March_bass2"]
            bassMidiFX = {'midi_transpose': '8vb', 'midi_arp': 'quarterNotes'}
            bassAudioFX = {'ReaEQ (Cockos)': ["EQ_Bass"]}

            upbeatsPresets = ["Kontakt5_March_upbeats1", "Kontakt5_March_upbeats2", "Play_March_upbeats1", "Play_March_upbeats2"]
            upbeatsMidiFX = {"midi_delay": "eighthNote", "midi_note_repeater": "quarterNote"}

            ostinatoPresets = ["Kontakt5_March_ostinato1", "Kontakt5_March_ostinato2", "Kontakt5_March_ostinato3", "Kontakt5_March_ostinato4", "Kontakat5_March_ostinato5"]
            ostinatoMidiFX = {"midi_arp": "wwArpEighthNotes"}

            bassDrumPresets = ["Kontakt5_March_bassDrum1", "Kontakt5_March_bassDrum2"]

            snarePresets = ["Kontakt5_March_snare1", "Kontakt5_March_snare2"]

            melodyPresets = ["", "", ""]

            CreateLayer (bass2, "BASS", bassPresets, bassMidiFX, bassAudioFX, .375)
            CreateLayer (pianoRH, "UPBEATS", upbeatsPresets, upbeatsMidiFX, "", .2)
            CreateLayer (pianoRH, "OSTINATO", ostinatoPresets, ostinatoMidiFX, "", .185)
            CreateLayer (bassDrum, "BASS DRUM", bassDrumPresets, "", "", .55)
            CreateLayer (snare, "SNARE", snarePresets, "", "", .315)
            CreateLayer (melody, "MELODY", melodyPresets, "", "", .25)


        elif mood == "popfunk" :

            bassPresets = ["Omnisphere_Pop_bass1", "Omnisphere_Pop_bass2", "Omnisphere_Pop_bass3", "Omnisphere_Pop_bass4", "Omnisphere_Pop_bass5", "Omnisphere_Pop_bass6", "Omnisphere_Pop_bass7"]
            bassAudioFX = {'ReaEQ (Cockos)': ["EQ_pop_synth_bass"]}

            arpPresets = ["Omnisphere_Pop_arp1", "Omnisphere_Pop_arp2", "Omnisphere_Pop_arp3", "Omnisphere_Pop_arp4", "Omnisphere_Pop_arp5", "Omnisphere_Pop_arp6"]
            arpAudioFX = {"ReaEQ (Cockos)": ["EQ_arp"]}

            guitarRhythmPresets = ["Omnisphere_Pop_rhythmGuitar1", "Omnisphere_Pop_rhythmGuitar2", "Omnisphere_Pop_rhythmGuitar3" "Omnisphere_Pop_rhythmGuitar4", "Omnisphere_Pop_rhythmGuitar5"]
            guitarAudioFX = {"ReaEQ (Cockos)": ["EQ_pop_rhythm_guitar"], GuitarRig: ["GuitarRig_funkyRhythmGuitar1", "GuitarRig_funkyRhythmGuitar2", "GuitarRig_funkyRhythmGuitar3"]}

            padPresets = ["Omnisphere_Pop_pad1", "Omnisphere_Pop_pad2", "Omnisphere_Pop_pad3", "Omnisphere_Pop_pad4" "Omnisphere_Pop_pad5"]
            padAudioFX = {"ReaEQ (Cockos)": ["EQ_pad"]}

            kitPresets = ["Battery4_Pop_kit1"]
            kitMidiFX = {"midi_transpose": "8va"}
            kitAudioFX = {"ReaEQ (Cockos)": ["bass_drum"]}

            melodyPresets = ["Kontakt5_Pop_melody1", "Omnisphere_Pop_melody2", "Omnisphere_Pop_melody3", "Omnisphere_Pop_melody4", "Omnisphere_Pop_melody5", "Omnisphere_Pop_melody6"]
            melodyAudioFX = {"ReaEQ (Cockos)": ["HPF_melody"]}

            rhythmPresets = ["Kontakt5_inspiredPiano"]

            CreateLayer (bass2, "BASS", bassPresets, "", bassAudioFX, .2225)
            CreateLayer (rhythm, "SYNTH ARP 2", arpPresets, "", arpAudioFX, .18)
            CreateLayer (pianoRH, "SYNTH ARP 1", arpPresets, "", arpAudioFX, .225)
            CreateLayer (pianoRH, "RHYTHM GUITAR", guitarRhythmPresets, "", guitarAudioFX, .1425)
            CreateLayer (hiStrings, "PAD", padPresets, "", padAudioFX, .35)
            CreateLayer (drums, "KIT", kitPresets, kitMidiFX, kitAudioFX, .7)
            #CreateLayer (rhythm, "PIANO", arpPresets, "", "", .2)
            CreateLayer (melody, "MELODY", melodyPresets, "", melodyAudioFX, .4)


        elif mood == "propulsion" :

            bassPresets = ["Omnisphere_Propulsion_bass1", "Omnisphere_Propulsion_bass2", "Omnisphere_Propulsion_bass3", "Omnisphere_Propulsion_bass4", "Omnisphere_Propulsion_bass5"]
            bassAudioFX = {'ReaEQ (Cockos)': ["EQ_Propulsion_bass"]}

            pianoLHPresets = ["Kontakt5_Propulsion_piano1"]
            pianoLHAudioFX = {}

            guitarPresets = ["Omnisphere_Propulsion_guitar1"]
            guitarAudioFX = {}

            pianoPresets = ["Kontakt5_Propulsion_piano1"]
            pianoAudioFX = {}

            arpPresets = ["Omnisphere_Propulsion_arp1"]
            arpAudioFX = {"ReaEQ (Cockos)": ["EQ_Arp"]}

            stringArpPresets = ["Kontakt5_Propulsion_stringArp1", "Kontakt5_Propulsion_stringArp2"]
            stringArpAudioFX = {}

            ostinatoPresets = ["Kontakt5_March_ostinato2", "Kontakt5_March_ostinato3"]
            ostinatoMidiFX = {"midi_arp": "wwArpEighthNotes"}

            hiStringsPresets = ["Kontakt5_Propulsion_hiStrings1"]
            hiStringsAudioFX = {}
            loStringsPresets = ["Kontakt5_Propulsion_loStrings1"]
            loStringsAudioFX = {}
            stringsSusMidiFX = {"MIDI_CCRider": "WB_MIDI_LFO_modwheel_dynamics", "midi_CC_mapper": "WB_MIDI_modwheel_limiter"}

            cymbalsPresets = ["Kontakt5_Propulsion_cymbals1"]
            cymbalsAudioFX = {}

            padPresets = ["Omnisphere_Propulsion_pad1"]
            padAudioFX = {"ReaEQ (Cockos)": ["EQ_Pad"]}

            kitPresets = ["Battery_Racecar_kit1", "Battery_Racecar_kit1"]
            kitAudioFX = {}

            CreateLayer (bass2, "BASS", bassPresets, "", bassAudioFX, .145)
            CreateLayer (pianoLH, "PIANO", pianoLHPresets, "", pianoLHAudioFX, .225)
            #CreateLayer ([random.choice([bass2, cello, viola])], "GUITAR", guitarPresets, "", "", .23)
            #CreateLayer ([pianoRH, pianoLH], "PIANO", pianoPresets, "", "", .33)
            #CreateLayer ([pianoRH], "ARP SYNTH", arpPresets, "", "", .215)
            CreateLayer (pianoRH, "OSTINATO", ostinatoPresets, ostinatoMidiFX, "", .25)
            CreateLayer (arpStrings, "ARP STRINGS", stringArpPresets, "", "", .25)
            CreateLayer (hiStrings, "HI STRINGS", hiStringsPresets, stringsSusMidiFX, "", .175)
            CreateLayer (loStrings, "LO STRINGS", loStringsPresets, stringsSusMidiFX, "", .2)
            #CreateLayer ([pianoRH], "PAD", padPresets, "", padAudioFX, .22)
            CreateLayer (cymbals, "CYMBALS", cymbalsPresets, "", "", .3)
            CreateLayer (drums, "DRUMS", kitPresets, "", "", .65)
            CreateLayer (fills, "DRUMS", kitPresets, "", "", .65)
            #CreateLayer (bassDrum, "BASS DRUM", ["Kontakt5_March_bassDrum1"], "", .2)


        elif mood == "peruvianwaltz" :

            percPresets = ["Kontakt5_PeruvianWaltz_perc1","Kontakt5_PeruvianWaltz_perc2","Kontakt5_PeruvianWaltz_perc3","Kontakt5_PeruvianWaltz_perc4"]
            percAudioFX = {}

            bassPresets = ["Kontakt5_PeruvianWaltz_bass1", "Kontakt5_PeruvianWaltz_bass2", "Kontakt5_PeruvianWaltz_bass3", "Kontakt5_PeruvianWaltz_bass4", "Kontakt5_PeruvianWaltz_piano1"]
            bassAudioFX = {}

            rhythmPresets = ["Omnisphere_PeruvianWaltz_guitar1", "Omnisphere_PeruvianWaltz_guitar2", "Omnisphere_PeruvianWaltz_guitar3", "Omnisphere_PeruvianWaltz_guitar4", "Kontakt5_PeruvianWaltz_piano1", "Kontakt5_PeruvianWaltz_guitar1", "Kontakt5_PeruvianWaltz_guitar1", "Kontakt5_PeruvianWaltz_bandoneon1", "Kontakt5_PeruvianWaltz_mallets1"]
            rhythmAudioFX = {}

            melodyPresets = ["Kontakt5_PeruvianWaltz_piano1", "Kontakt5_PeruvianWaltz_guitar1", "Kontakt5_PeruvianWaltz_guitar1"]
            melodyAudioFX = {"ReaEQ (Cockos)": [""]}


            CreateLayer (rhythm, "RHYTHM 1", rhythmPresets, "", rhythmAudioFX, .25)
            CreateLayer (rhythm, "RHYTHM 2", rhythmPresets, "", rhythmAudioFX, .25)
            CreateLayer (bass1, "BASS", bassPresets, "", bassAudioFX, .25)
            CreateLayer (melody, "MELODY", melodyPresets, "", melodyAudioFX, .25)
            CreateLayer (pianoLH, "PIANO BASS", rhythmPresets[0], "", "", .25)

            for percLayers in range ( 1, random.randint(2,4) ) :
                CreateLayer (drums, "PERCUSSION " + str (percLayers), percPresets, "", percAudioFX, .25)



        elif mood == "inspire" :

            loStringsPresets = ["Kontakt5_Inspire_loStrings1"]

            hiStringsPresets = ["Kontakt5_Inspire_hiStrings1"]

            arpStringsPresets = ["Kontakt5_Inspire_arpStrings1", "Kontakt5_Inspire_arpStrings2"]

            wwArpPresets = ["Kontakt5_Inspire_wwArp1", "Kontakt5_Inspire_wwArp2"]

            guitarPresets = ["Omnisphere_Inspire_guitar1", "Omnisphere_Inspire_guitar2"]

            bassPresets = ["Kontakt5_Inspire_bass1", "Kontakt5_Inspire_bass2"]
            bassMidiFX = {"midi_arp": "eighthNotes"}

            pianoPresets = ["Kontakt5_Inspire_piano1"]

            bassDrumPresets = ["Kontakt5_Inspire_lowPercussion1"]

            kickDrumPresets = ["Kontakt5_Pop_kickDrum1"]

            cymbalPresets = ["Kontakt5_Inspire_cymbals1"]

            melodyPresets = ["Omnisphere_Inspire_melody1", "Kontakt5_Inspire_stringsMel1", "Kontakt5_Inspire_stringsMel2"]

            CreateLayer (loStrings, "LOW STRINGS", loStringsPresets, "", "", .25)
            CreateLayer (midStrings, "HI STRINGS", hiStringsPresets, "", "", .25)
            CreateLayer (arpStrings, "STRINGS SHORT", arpStringsPresets, "", "", .25)
            StringArpSetParameters ()
            CreateLayer (arpStrings, "WW OSTINATO", wwArpPresets, "", "", .25)
            WoodwindsOstinatoSetParamaters ()
            CreateLayer (melody, "MELODY", melodyPresets, "", "", .25)
            CreateLayer (bass2, "GUITAR", guitarPresets, "", "", .25)
            CreateLayer (bass2, "BASS GUITAR", bassPresets, bassMidiFX, "", .25 ) #add midi arp eighth note to this one
            #CreateLayer (bass1, inspired, "STRUMMED GUITAR")
            CreateLayer (pianoLH, "PIANO", pianoPresets, "", "", .25)
            CreateLayer (bassDrum, "BASS DRUM", bassDrumPresets, "", "", .25)
            CreateLayer (kickDrum, "KICK DRUM", kickDrumPresets, "", "", .25)
            CreateLayer (cymbals, "CYMBALS", cymbalPresets, "", "", .25)



        CreateSubmixTrack ()


        createDemoTracks = False

        if createDemoTracks == True :
            #DEMO TRACKS - Layers created for showcasing the melody
            melodyPresets = ["Kontakt5_Propulsion_piano1"]
            bassPresets = ["Kontakt5_Propulsion_piano1"]
            kitPresets = ["Omnisphere_Pop_bass1"]
            CreateLayer (melody, "MELODY", melodyPresets, "", "", .25)
            CreateLayer (bass1, "BASS", bassPresets, "", "", .175)
            CreateLayer (drums, "DRUMS", kitPresets, "", "", .35)

            CreateLayer ("", "DEMO GROUP", [""], "", "", 1.0)
            GroupNumOfTracksBelowSelectedTrack (0, 3)

            #Solo first track
            #Render output as demo track

        setTempo ()



        #select all tracks except for STRINGS SHORT and nudge 50 ms to the right
        if mood == 'inspire' or mood == 'anthematic' or mood == 'propulsion' :

            numOfTracks = RPR_CountTracks (0)
            RPR_Main_OnCommand (40297, 1)
            for tr in range ( 0, numOfTracks ) :

                trId = RPR_GetTrack (0, tr)
                name = RPR_GetSetMediaTrackInfo_String (trId, "P_NAME", " ", False)


                #RPR_ShowConsoleMsg (name[3] + "\n")#+ ": " + randType "\n")

                if not name[3] == "ARP STRINGS" :
                    #RPR_ShowConsoleMsg ("select")
                    RPR_SetTrackSelected (trId, True)

            RPR_Main_OnCommand (40421, 1) #selects all items on selected tracks
            RPR_ApplyNudge( 0, 0, 0, 0, 75, False, 0 )



        RPR_SetEditCurPos (0, True, True) # set cursor to 0 (or beginning)
        #RPR_Main_OnCommand (40044, 1)     # spacebar - plays track

        touchCmd = "touch " + projectPath + "/"  + projectName + ".startRendering"
        #RPR_ShowConsoleMsg(touchCmd)
        #print ( "Touch Cmd: ", touchCmd )
        os.system(touchCmd)


        RPR_Main_OnCommand (41824, 1)      # renders file with last known settings

        childProc = os.fork()
        if ( childProc == 0 ) :
            #print ( "Inside reascript child process")
            touchCmd = "touch " + projectPath + "/"  + projectName + ".renderComplete"
            #print ( "Touch Cmd: ", touchCmd )
            os.system(touchCmd)


        #touchCmd = "touch " + projectPath + "/" + projectName + ".renderComplete"
        #print ( "Touch Cmd: ", touchCmd )
        #RPR_ShowConsoleMsg(touchCmd)

        #os.system(touchCmd)
#preset = "Play_Kontakt5_blah_blah"
#instrument = preset.split ("_", 1)
#RPR_ShowConsoleMsg (instrument[0])







def FindMIDIRangePerSection (track, startpos, endpos, ) :

    for sect in range ( 1, numSections + 1 ) :

        startPos = (sect, compositionSettings[0][sect][0]['clock'])
        #RPR_Main_OnCommand (40153, 1) #opens MIDI editor
        #loop through all midi notes and store pitches in array
        #find distance between highest/lowest notes
        #RPR_GetTrackMIDINoteRange (0, RPR_GetTrack (0,4), 0, 0 )
        #RPR_MIDI_GetNote(take, noteidx, selectedOut, mutedOut, startppqposOut, endppqposOut, chanOut, pitchOut, velOut)

        #RPR_ShowConsoleMsg (str(sect) + ", ")
        #RPR_ShowConsoleMsg (str(startPos) + ", ")
        #RPR_ShowConsoleMsg ("\n" + str(endPos)   + ", ")

    RPR_SetEditCurPos (0, True, True)
    RPR_Main_OnCommand (40297, 1) # unselects all tracks
    RPR_SetTrackSelected (RPR_GetTrack (0,4), True)
    RPR_Main_OnCommand (40421, 1) #selects item on selected track

    take = RPR_GetMediaItem (0, 5)
    #RPR_ShowConsoleMsg (RPR_CountMediaItems(0))

    mediaItems = RPR_CountMediaItems(0)
    for item in range (0, RPR_CountMediaItems(0)) :
        RPR_ShowConsoleMsg ("itemID: " + str(item) + ", \nselected: ," + str(RPR_IsMediaItemSelected (item)) + "\n")

        if RPR_IsMediaItemSelected (item) == 1 :
            RPR_ShowConsoleMsg (RPR_GetMediaItem (0, item))

      #else :
          #RPR_ShowConsoleMsg ("none")
#ReadCompositionSettings ()
#compositionSettings, movementSettings = ReadCompositionSettings ()
#numSections = len(compositionSettings[0])
#FindMIDIRangePerSection (0,0,0)

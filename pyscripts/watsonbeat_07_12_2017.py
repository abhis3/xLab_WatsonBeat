import os
import sys
import math
import random
import collections



user = "Richard"
startScript = True
user = 'jmukund'

importDirectory = "/Users/" + user + "/Repo/wbRLRBM/src/"

Kontakt5     = "Kontakt 5 (Native Instruments GmbH) (8 out)"
Kontakt5_16  = "Kontakt 5 (Native Instruments GmbH) (16 out)"
Massive      = "Massive (Native Instruments GmbH)"
Battery      = "Battery 4 (Native Instruments GmbH)"
Omnisphere   = "Omnisphere (Spectrasonics)"
GuitarRig    = "Guitar Rig 5 (Native Instruments GmbH)"
Play         = "Play (East West) (2->18ch)"


# set a default volume for all the instruments.
# volume for the different instruments will be set at the preset files
#volume = random.uxniform ( 0.35, 0.5 )
volume = 0.35
Movement = collections.OrderedDict()

desktopApp = True
if desktopApp :
    
    proj, projectNameExt, buf_sz = RPR_GetProjectName(1, 1, 100)
    projectName = projectNameExt.replace ( ".RPP", "",  1)
    # udid = projectName.replace ( "WatsonBeatProject", "",  1)

    projectPath, bufSz = RPR_GetProjectPath("", 512)
    configFile = projectPath + "/config"

    # RPR_ShowConsoleMsg ( projectName + "\n" )
    # RPR_ShowConsoleMsg ( projectPath + "\n" )
    # RPR_ShowConsoleMsg ( configFile + "\n")

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

                elif ( data[item] == 'tempo' ) :
                    tempo = int(data[item+1])
                    Movement[mvNum]['Sections'][secNum]['tempo'] = tempo


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




def RouteToVerb () :

    numOfTracks = RPR_CountTracks (0)
    sendTrack = RPR_GetTrack (0, 0)

    for tr in range ( 1, numOfTracks ) :

        RPR_Main_OnCommand (40297, 1) #unselect all tracks
        curTrack  = RPR_GetTrack (0, tr)
        RPR_CreateTrackSend (curTrack, sendTrack)




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




def StringArpSetParameters () :

    #arpRate = random.choice ([5,8])

    if tempo >= 125 :
        arpRate = 8

    elif tempo < 125 :
        arpRate = 5

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
        #arpRate = random.choice ([5,8])

        if tempo >= 125 :
            arpRate = 8

        elif tempo < 125 :
            arpRate = 5

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


    if startScript == True :

        InitializeReaper ()

        finName = importDirectory + "/CompositionSettings"
        parseCompositionSettings ( finName )

        # to get number of sections in movement 0
        numSections = Movement[0]['numSections']

        # to get number of phrases in section 0 in movement 0
        numPhrases = Movement[0]['Sections'][0]['numPhrases']

        # to get the layers for section 3 in movement 0
        #layers = getLayersForSection ( 0, 3 )

        mood = Movement[0]['mood']
        #RPR_ShowConsoleMsg (mood)

        #sets initial tempo only
        tempo = Movement[0]['Sections'][0]['tempo']
        #RPR_ShowConsoleMsg (tempo)

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
        pianoArp   = []
        pianoLH    = []
        pianoRH    = []
        pianoRH2   = []
        bassDrum   = []
        kickDrum   = []
        cymbals    = []
        snare      = []
        hiHat      = []
        bass1      = []
        bass2      = []
        bass3      = []
        fills      = []
        latinDrums = []
        rhythm     = []
        brass      = []
        melodyA1   = []
        melodyA2   = []
        melodyA3   = []
        melodyB1   = []
        melodyB2   = []
        melodyB3   = []
        reggaeGuitar = []



        #finds existing MIDI files for each layer and adds them to a list per each layer
        for section in range (0, numSections) :

            layers = getLayersForSection (0, section)

            for layer in range (0, len(layers)) :
                #RPR_ShowConsoleMsg (layers[layer] + '\n')

                if section == 0 or 1 :
                    if layers[layer] == 'mel5' :
                        melodyA1.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_mel5High.mid" )
                        melodyA2.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_mel5Med.mid" )
                        melodyA3.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_mel5Low.mid" )

                elif section > 1 :
                    if layers[layer] == 'mel5' :
                        melodyB1.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_mel5High.mid" )
                        melodyB2.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_mel5Med.mid" )
                        melodyB3.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_mel5Low.mid" )

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

                elif layers[layer] == 'piano1' :
                    pianoArp.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_piano1.mid" )

                elif layers[layer] == 'rightPiano' :
                    pianoRH.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_rightPiano.mid" )

                elif layers[layer] == 'rightPiano2' :
                    pianoRH2.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_rightPiano2.mid" )

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

                elif layers[layer] == 'drumsLatinPop' :
                    latinDrums.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_drumsLatinPop.mid" )

                elif layers[layer] == 'bass1' :
                    bass1.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_bass1.mid" )

                elif layers[layer] == 'bass2' :
                    bass2.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_bass2.mid" )

                elif layers[layer] == 'bass3' :
                    bass3.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_bass3.mid" )

                elif layers[layer] == 'brassRhythms' :
                    brass.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_brassRhythms.mid" )

                elif layers[layer] == 'notationRP' :
                    reggaeGuitar.append ( importDirectory + "WB_Mvmt0_Sec" + str(section) + "_notationRP.mid" )

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

            melodyPresets = ["Kontakt5_Pop_melody1", "Omnisphere_Pop_melody2", "Omnisphere_Pop_melody4", "Omnisphere_Pop_melody5"]
            melodyAudioFX = {"ReaEQ (Cockos)": ["HPF_melody"]}

            rhythmPresets = ["Kontakt5_inspiredPiano"]

            CreateLayer (bass2, "BASS", bassPresets, "", bassAudioFX, .25)
            CreateLayer (rhythm, "SYNTH ARP 2", arpPresets, "", arpAudioFX, .18)
            CreateLayer (pianoRH2, "SYNTH ARP 1", arpPresets, "", arpAudioFX, .225)
            CreateLayer (pianoRH, "RHYTHM GUITAR", guitarRhythmPresets, "", guitarAudioFX, .175)
            CreateLayer (hiStrings, "PAD", padPresets, "", padAudioFX, .35)
            CreateLayer (drums, "KIT", kitPresets, kitMidiFX, kitAudioFX, .6)
            #CreateLayer (rhythm, "PIANO", arpPresets, "", "", .2)
            CreateLayer (melody, "MELODY", melodyPresets, "", melodyAudioFX, .4)



        elif mood == "chill" :

            bassPresets = ["Omnisphere_Chill_bass1", "Omnisphere_Chill_bass2", "Omnisphere_Chill_bass3"]
            loPadPresets = ["Omnisphere_Chill_loPad1", "Omnisphere_Chill_loPad2", "Omnisphere_Chill_loPad3", "Omnisphere_Chill_loPad4"]
            bassAudioFX = {'ReaEQ (Cockos)': ["EQ_pop_synth_bass"]}

            arpPresets = ["Omnisphere_Pop_arp1", "Omnisphere_Pop_arp2", "Omnisphere_Pop_arp3", "Omnisphere_Pop_arp4", "Omnisphere_Pop_arp5", "Omnisphere_Pop_arp6"]
            arpAudioFX = {"ReaEQ (Cockos)": ["EQ_arp"]}

            texturePresets = ["Omnisphere_Chill_texture1" "Omnisphere_Chill_texture2", "Omnisphere_Chill_texture3"]
            textureAudioFX = {"ReaEQ (Cockos)": ["EQ_pop_rhythm_guitar"]} #GuitarRig: ["GuitarRig_funkyRhythmGuitar1", "GuitarRig_funkyRhythmGuitar2", "GuitarRig_funkyRhythmGuitar3"]}

            padPresets = ["Omnisphere_Chill_pad1", "Omnisphere_Chill_pad2", "Omnisphere_Chill_pad3", "Omnisphere_Chill_pad4"]
            padAudioFX = {"ReaEQ (Cockos)": ["EQ_pad"]}

            kitPresets = ["Battery4_Chill_kit1"]
            kitMidiFX = {"midi_transpose": "8va"}
            kitAudioFX = {"ReaEQ (Cockos)": ["bass_drum"]}

            melodyPresets = ["Kontakt5_Chill_melody1", "Omnisphere_Chill_melody1", "Omnisphere_Chill_melody2", "Omnisphere_Chill_melody3"]
            melodyAudioFX = {"ReaEQ (Cockos)": ["HPF_melody"]}

            rhythmPresets = ["Kontakt5_inspiredPiano"]

            CreateLayer (bass3, "BASS", bassPresets, "", bassAudioFX, .2225)
            CreateLayer (bass1, "LO PAD", loPadPresets, "", bassAudioFX, .25)
            CreateLayer (rhythm, "SYNTH ARP 2", arpPresets, "", arpAudioFX, .18)
            CreateLayer (pianoRH2, "SYNTH ARP 1", arpPresets, "", arpAudioFX, .225)
            CreateLayer (pianoRH, "TEXTURE", texturePresets, "", textureAudioFX, .1425)
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
            stringsSusMidiFX = {"MIDI_CCRider": "WB_MIDI_LFO_modwheel_dynamics", "midi_CC_mapper": "WB_MIDI_modwheel_limiter"}

            arpStringsPresets = ["Kontakt5_Inspire_arpStrings1", "Kontakt5_Inspire_arpStrings2"]

            wwArpPresets = ["Kontakt5_Inspire_wwArp1", "Kontakt5_Inspire_wwArp2"]

            guitarPresets = ["Omnisphere_Inspire_rhythmGuitar1", "Omnisphere_Inspire_rhythmGuitar2"]
            guitarAudioFX = {GuitarRig: ["GuitarRig_cleanAmpSim1"], "ReaDelay (Cockos)": ["WB_reaDelay_stereo_dotted8th"]}

            bassPresets = ["Kontakt5_Inspire_bass1", "Kontakt5_Inspire_bass2"]
            bassMidiFX = {"midi_arp": "eighth_notes"}

            pianoPresets = ["Kontakt5_Inspire_piano1"]

            bassDrumPresets = ["Kontakt5_Inspire_lowPercussion1"]

            kickDrumPresets = ["Kontakt5_Pop_kickDrum1"]

            cymbalPresets = ["Kontakt5_Inspire_cymbals1"]

            melodyPresets = ["Omnisphere_Inspire_melody1", "Kontakt5_Inspire_stringsMel1", "Kontakt5_Inspire_stringsMel2"]

            CreateLayer (loStrings, "LOW STRINGS", loStringsPresets, stringsSusMidiFX, "", .2)
            CreateLayer (midStrings, "HI STRINGS", hiStringsPresets, stringsSusMidiFX, "", .2)
            CreateLayer (arpStrings, "STRINGS SHORT", arpStringsPresets, "", "", .175)
            StringArpSetParameters ()
            CreateLayer (arpStrings, "WW OSTINATO", wwArpPresets, "", "", .225)
            WoodwindsOstinatoSetParamaters ()
            CreateLayer (melody, "MELODY", melodyPresets, "",  "", .325)
            CreateLayer (bass2, "GUITAR", guitarPresets, "", guitarAudioFX, .115)
            CreateLayer (bass2, "BASS GUITAR", bassPresets, bassMidiFX, "", .5 ) #add midi arp eighth note to this one
            #CreateLayer (bass1, inspired, "STRUMMED GUITAR")
            CreateLayer (pianoLH, "PIANO", pianoPresets, "", "", .2)
            CreateLayer (bassDrum, "BASS DRUM", bassDrumPresets, "", "", .3)
            CreateLayer (kickDrum, "KICK DRUM", kickDrumPresets, "", "", .45)
            CreateLayer (cymbals, "CYMBALS", cymbalPresets, "", "", .25)


        elif mood == "reggaepop" :

            loStringsPresets = ["Kontakt5_ReggaePop_strings1"]
            hiStringsPresets = ["Kontakt5_ReggaePop_strings1"]
            stringsSusMidiFX = {"MIDI_CCRider": "WB_MIDI_LFO_modwheel_dynamics", "midi_CC_mapper": "WB_MIDI_modwheel_limiter"}

            kitPresets = ["Kontakt5_ReggaePop_kit2"]
            percussionPresets = ["Kontakt5_ReggaePop_percussion1", "Kontakt5_ReggaePop_percussion2", "Kontakt5_ReggaePop_percussion3", "Kontakt5_ReggaePop_percussion4"]
            pianoPresets = ["Kontakt5_ReggaePop_piano1"]
            shortPresets = ["Kontakt5_ReggaePop_keys1", "Kontakt5_ReggaePop_keys2", "Omnisphere_ReggaePop_keys1", "Omnisphere_ReggaePop_keys2"]#["Kontakt5_ReggaePop_marimba", "Omnisphere_ReggaePop_musicBox"]
            bassPresets = ["Kontakt5_ReggaePop_bass1", "Kontakt5_ReggaePop_bass2"]
            bassAudioFX = {GuitarRig: ["GuitarRig_bassAmp"], "ReaEQ (Cockos)": ["EQ_bass2"]}

            guitarPresets = ["Omnisphere_ReggaePop_rhythmGuitar2"]
            guitarAudioFX = {GuitarRig: ["GuitarRig_ReggaeGuitar1"]}

            melodyPresets = ["Kontakt5_ReggaePop_horns1"]
            melody2Presets = ["Omnisphere_darkMel1", "Omnisphere_darkMel2", "Omnisphere_darkMel3", "Omnisphere_darkMel4"]
            melody3Presets = ["Omnisphere_ReggaePop_guitarMel1"]
            melody3AudioFX = {GuitarRig: ["GuitarRig_ReggaePop_melAmp2"], "ReaEQ (Cockos)": ["EQ_HPF_60"]}
            verbAudioFX = {GuitarRig: ["GuitarRig_roomVerb1"], "ReaEQ (Cockos)": ["EQ_HPF_60"]}


            #CreateLayer (loStrings, "LOW STRINGS", loStringsPresets, stringsSusMidiFX, "", .165)
            #CreateLayer (hiStrings, "HI STRINGS", hiStringsPresets, stringsSusMidiF, "", .105)
            CreateLayer (drums, "DRUMS", kitPresets, "", "", .585)
            CreateLayer (fills, "FILLS", kitPresets, "", "", .55)
            CreateLayer (latinDrums, "PERCUSSION", percussionPresets, "", "", .7)
            CreateLayer (pianoLH+pianoRH, "PIANO", pianoPresets, "", "", .235)
            CreateLayer (brass, "ARP", shortPresets, "", "", .27)
            #CreateLayer (pianoRH, "PIANO RH", pianoPresets, "", "", .145)
            CreateLayer (bass3, "BASS", bassPresets, "", bassAudioFX, .435)
            CreateLayer (pianoRH, "GUITAR", guitarPresets, "", guitarAudioFX, .435)
            #CreateLayer (violin2, "GUITAR 2", guitarPresets, "", guitarAudioFX, .4)
            #CreateLayer (brass, "BRASS", melodyPresets, "", "", .45)

            melodyInstrumentChoice = random.randint (100, 101)

            if melodyInstrumentChoice <= 99 :

                CreateLayer (melodyA1, "MELODY 1", ["Kontakt5_ReggaePop_hornsFPOctaves", "Kontakt5_ReggaePop_hornsSustainOctaves", "Kontakt5_ReggaePop_hornsMarcatoOctaves"], "", "", .375)
                CreateLayer (melodyA2, "MELODY 2", ["Kontakt5_ReggaePop_hornsMarcatoOctaves"], "", "", .375)
                CreateLayer (melodyA3, "MELODY 3", ["Kontakt5_ReggaePop_hornsStaccatoOctaves"], "", "", .375)

            else :

                CreateLayer (melody, "MELODY", melody3Presets, "", melody3AudioFX, .19)

            CreateLayer ("", "ROOM VERB", ["Kontakt5_empty"], "", verbAudioFX, .225)
            RouteToVerb ()




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

        #setTempo ()
        RPR_SetTempoTimeSigMarker( 0, -1, 0, 0-1, 0, tempo, 4, 4, True )


        #select all tracks except for STRINGS SHORT and nudge 50 ms to the right
        if mood == 'inspire' or mood == 'anthematic' or mood == 'propulsion' :

            numOfTracks = RPR_CountTracks (0)
            RPR_Main_OnCommand (40297, 1)
            for tr in range ( 0, numOfTracks ) :

                trId = RPR_GetTrack (0, tr)
                name = RPR_GetSetMediaTrackInfo_String (trId, "P_NAME", " ", False)

                if not name[3] == "ARP STRINGS" :
                    RPR_SetTrackSelected (trId, True)

                if not name[3] == "STRINGS SHORT" :
                    RPR_SetTrackSelected (trId, True)

                if not name[3] == "WW OSTINATO" :
                    RPR_SetTrackSelected (trId, True)

            RPR_Main_OnCommand (40421, 1) #selects all items on selected tracks
            RPR_ApplyNudge( 0, 0, 0, 0, 75, False, 0 )


        RPR_SetEditCurPos (0, True, True) # set cursor to 0 (or beginning)
        #RPR_Main_OnCommand (40044, 1)     # spacebar - plays track

        if ( desktopApp ) :

            touchCmd = "touch " + projectPath + "/"  + projectName + ".startRendering"
            # RPR_ShowConsoleMsg(touchCmd)
            # print ( "Touch Cmd: ", touchCmd )
            os.system(touchCmd)


            RPR_Main_OnCommand (41824, 1)      # renders file with last known settings

            childProc = os.fork()
            if ( childProc == 0 ) :
                # print ( "Inside reascript child process")
                touchCmd = "touch " + projectPath + "/"  + projectName + ".renderComplete"
                # print ( "Touch Cmd: ", touchCmd )
                os.system(touchCmd)

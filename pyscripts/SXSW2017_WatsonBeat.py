import os
import math
import random

proj, projectNameExt, buf_sz = RPR_GetProjectName(1, 1, 100)
projectName = projectNameExt.replace ( ".RPP", "",  1)
#udid = projectName.replace ( "WatsonBeatProject", "",  1)

projectPath, bufSz = RPR_GetProjectPath("", 512)
configFile = projectPath + "/config"

#RPR_ShowConsoleMsg ( projectName + "\n" )
#RPR_ShowConsoleMsg ( projectPath + "\n" )
#RPR_ShowConsoleMsg ( configFile + "\n")

startScript = True

file = open (configFile, 'r')
newImportDirectory = file.readline ()
file.close ()
newImportDirectory = newImportDirectory.strip() + "/"
#RPR_ShowConsoleMsg ( newImportDirectory)

#newImportDirectory = "/Users/" + user + "/Repo/DJWatsonExperimental/"

importMIDIArp1     = newImportDirectory + "Arp0.mid"
importMIDIArp2     = newImportDirectory + "Arp1.mid"
importMIDIArp3     = newImportDirectory + "Arp2.mid"
importMIDIguitar   = newImportDirectory + "rhyWB.mid"
importMIDIpiano    = newImportDirectory + "pianoWB.mid"

importMIDIKick     = newImportDirectory + "kick.mid"
importMIDISnare    = newImportDirectory + "snare.mid"
importMIDIHiHat    = newImportDirectory + "hihat.mid"
importMIDIFill     = newImportDirectory + "fill.mid"

importMIDIMelody   = newImportDirectory + "melodyWB.mid"
importMIDIBass     = newImportDirectory + "bassWB.mid"



Kontakt5     = "Kontakt 5 (Native Instruments GmbH)"
Massive      = "Massive (Native Instruments GmbH)"


romanticSimple        = "romantic_simple"
romanticSemiComplex   = "romantic_semi_complex"
ampedSimple           = "amped_simple"
ampedSemiComplex      = "amped_semi_complex"
chillSimple           = "dark_simple"
chillSemiComplex      = "dark_semi_complex"
spookySimple          = "spooky_simple"
spookySemiComplex     = "spooky_semi_complex"
worldSimple           = "mideastern_simple"
worldSemiComplex      = "mideastern_semi_complex"
# set a default volume for all the instruments.
# volume for the different instruments will be set at the preset files
volume = random.uniform ( 0.35, 0.5 )


def CreateDrumTracks ( mood ) :


    if mood == romanticSimple or mood == romanticSemiComplex :
        drumPresets = ["romantic_kit1"]

    elif mood == worldSimple or mood == worldSemiComplex :
        drumPresets = ["world_kit1"]

    elif mood == chillSimple or mood == chillSemiComplex :
        drumPresets = ["chill_kit1"]

    elif mood == ampedSimple or mood == ampedSemiComplex :
        drumPresets = ["amped_kit1", "amped_kit2"]

    elif mood == spookySimple or mood == spookySemiComplex :
        drumPresets = ["spooky_kit1", "spooky_kit2"]

    else :
        drumPresets = ["amped_kit1", "amped_kit2"]

    preset = random.choice ( drumPresets )

    instrument = Kontakt5

    #RPR_ShowConsoleMsg ( instrument + "\n" )
    #RPR_ShowConsoleMsg ( preset + "\n" )

    # put clock to 0
    RPR_SetEditCurPos (0, True, True) # sets scroll cursor to the beginning 0 on timeline
    # inserts an empty track with no instrument added to it
    RPR_InsertTrackAtIndex (0, True)  # inserts drum kit VST

    # the first track id will always be 0
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), instrument, True)  # adds instrument=kontakt5 on to the newly created track

    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 0, preset)  # set preset on the instrument

    RPR_SetMediaTrackInfo_Value (RPR_GetTrack (0, 0), "D_VOL", volume) # set volume for the track

    # adding different effect on to the drum tracks
    # learn later from Richard
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "ReaEQ (Cockos)", True)
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 1, "EQ_drums")
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "ReaComp (Cockos)", True)
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 2, "comp_drums")
    ParameterRandomization ( 0, 10, 40, 2, 1 ) #Ratio
    ParameterRandomization ( 0, 8, 30, 2, 2 ) #Attack
    ParameterRandomization ( 0, 0, 8, 2, 3 ) #Release

    RenameTrack (0,"DRUM KIT")
    ImportMidiFile (importMIDIKick)
    ImportMidiFile (importMIDISnare)
    ImportMidiFile (importMIDIHiHat)
    ImportMidiFile (importMIDIFill)

    GroupTracksBelowSelectedTrack (0) #Groups drum MIDI under DRUM KIT vst



def CreateMelodyTrack ( mood, file ) :
    '''
    create melody track
    '''
    if   mood == chillSimple or mood == chillSemiComplex :
        melodyPresets = ["chill_mel1", "chill_mel2", "chill_mel3"]
        instrumentMel = Kontakt5

    elif mood == ampedSimple or mood == ampedSemiComplex :
        melodyPresets = ["amped_mel1", "amped_mel2", "amped_mel3"]
        instrumentMel = Kontakt5

    elif mood == spookySimple or mood == spookySemiComplex :
        melodyPresets = ["spooky_mel1", "spooky_mel2", "spooky_me3"]
        instrumentMel = Kontakt5

    elif mood == worldSimple or mood == worldSemiComplex :
        melodyPresets = ["world_mel1", "world_mel2", "world_mel3", "world_mel4", "world_mel5", "world_mel6"]
        instrumentMel = Massive

    elif mood == romanticSimple or mood == romanticSemiComplex :
        melodyPresets = ["romantic_mel1", "romantic_mel1", "romantic_mel2", "romantic_mel3"]
        instrumentMel = Kontakt5


    preset = random.choice ( melodyPresets )

    # put clock to 0
    RPR_SetEditCurPos (0, True, True) # sets scroll cursor to the beginning 0 on timeline
    # inserts an empty track with no instrument added to it. 0 indicates track is inserted at 0th position
    RPR_InsertTrackAtIndex (0, True)

    RPR_Main_OnCommand (40297, 1) # unselects all tracks
    RPR_Main_OnCommand (40939, 1) # selects first track

    RPR_InsertMedia (file, 0) # inserts MIDI on new track.. Maybe change 1 to 0???




    # the first track id will always be 0
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), instrumentMel, True)  # adds instrument=kontakt5 on to the newly created track
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 0, preset) # set preset on the instrument
    RPR_SetMediaTrackInfo_Value (RPR_GetTrack (0, 0), "D_VOL", volume) # set volume for the track

    # adding different effect on to the drum tracks
    # learn later from Richard
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "ReaEQ (Cockos)", True)
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 1, "HPF_melody")
    ParameterRandomization ( 1, 130, 235, 1, 0 ) #HiPass Filter Frequency

    RenameTrack (0, "MELODY")


def CreateArpeggioTracks ( mood, file, arpName ) :

    if mood == chillSimple or mood == chillSemiComplex :
        arpPresets = ["chill_arp1", "chill_arp2", "chill_arp3", "chill_arp4", "chill_arp5"]
        instrumentArp = Kontakt5

    elif mood == ampedSimple or mood == ampedSemiComplex :
        arpPresets = ["amped_arp1", "amped_arp2", "amped_arp3", "amped_arp4", "amped_arp5", "amped_arp6"]
        instrumentArp = Kontakt5

    elif mood == spookySimple or mood == spookySemiComplex :
        arpPresets = ["spooky_arp1", "spooky_arp2", "spooky_arp3", "spooky_arp4"]
        instrumentArp = Kontakt5

    elif mood == worldSimple or mood == worldSemiComplex :
        arpPresets = ["world_arp1", "world_arp2", "world_arp3", "world_arp4", "world_arp5"]
        instrumentArp = Kontakt5

    elif mood == romanticSimple or mood == romanticSemiComplex :
        arpPresets = ["romantic_arp1", "romantic_arp2", "romantic_arp3", "romantic_arp4"]
        instrumentArp = Massive

    preset = random.choice ( arpPresets )

    # put clock to 0
    RPR_SetEditCurPos (0, True, True) # sets scroll cursor to the beginning 0 on timeline
    # inserts an empty track with no instrument added to it. 0 indicates track is inserted at 0th position
    RPR_InsertTrackAtIndex (0, True)

    RPR_Main_OnCommand (40297, 1) # unselects all tracks
    RPR_Main_OnCommand (40939, 1) # selects first track

    RPR_InsertMedia (file, 0) # inserts MIDI on new track.. Maybe change 1 to 0???




    # the first track id will always be 0
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), instrumentArp, True)  # adds instrument=kontakt5 on to the newly created track
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 0, preset) # set preset on the instrument
    RPR_SetMediaTrackInfo_Value (RPR_GetTrack (0, 0), "D_VOL", volume) # set volume for the track

    # adding different effect on to the drum tracks
    # learn later from Richard
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "ReaEQ (Cockos)", True)
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 1, "HPF_melody")
    ParameterRandomization ( 1, 110, 220, 1, 0 ) #HiPass Filter Frequency

    RenameTrack (0, arpName )



def CreateBassTrack ( mood, file, bassName ) :

    if   mood == chillSimple or mood == chillSemiComplex :
        bassPresets = ["chill_bass1", "chill_bass2", "chill_bass3"]

    elif mood == ampedSimple or mood == ampedSemiComplex :
        bassPresets = ["amped_bass1", "amped_bass2", "amped_bass3"]

    elif mood == spookySimple or mood == spookySemiComplex :
        bassPresets = ["spooky_bass1", "spooky_bass2", "spooky_bass3"]

    elif mood == worldSimple or mood == worldSemiComplex :
        bassPresets = ["world_bass1", "world_bass2", "world_bass3" "world_bass4"]

    elif mood == romanticSimple or mood == romanticSemiComplex :
        bassPresets = ["romantic_bass1", "romantic_bass2", "romantic_bass1", "romantic_bass2", "romantic_bass3"]

    preset = random.choice ( bassPresets )

    # put clock to 0
    RPR_SetEditCurPos (0, True, True) # sets scroll cursor to the beginning 0 on timeline
    # inserts an empty track with no instrument added to it. 0 indicates track is inserted at 0th position
    RPR_InsertTrackAtIndex (0, True)

    RPR_Main_OnCommand (40297, 1) # unselects all tracks
    RPR_Main_OnCommand (40939, 1) # selects first track

    RPR_InsertMedia (file, 0) # inserts MIDI on new track.. Maybe change 1 to 0???

    instrumentBass = Kontakt5


    # the first track id will always be 0
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), instrumentBass, True)  # adds instrument=kontakt5 on to the newly created track
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 0, preset) # set preset on the instrument
    RPR_SetMediaTrackInfo_Value (RPR_GetTrack (0, 0), "D_VOL", volume) # set volume for the track

    # adding different effect on to the drum tracks
    # learn later from Richard
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "ReaEQ (Cockos)", True)
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 1, "bass_eq")

    RenameTrack (0, bassName )


def CreatePadTrack ( mood, file, padName ) :
    if  mood == ampedSimple or mood == ampedSemiComplex :
        padPresets = ["amped_pad1", "amped_pad2","amped_pad3"]
        instrumentPad = Kontakt5

    elif mood == chillSimple or mood == chillSemiComplex :
        padPresets = ["chill_pad1", "chill_pad2","chill_pad3", "chill_pad4", "chill_pad5", "chill_pad6"]
        instrumentPad = Massive

    elif mood == spookySimple or mood == spookySemiComplex :
        padPresets = ["spooky_pad1", "spooky_pad2", "spooky_pad3", "spooky_pad4", "spooky_pad5", "spooky_pad6"]
        instrumentPad = Massive

    elif mood == worldSimple or mood == worldSemiComplex :
        padPresets = ["world_pad1", "world_pad2", "world_pad3"]
        instrumentPad = Massive

    elif mood == romanticSimple or mood == romanticSemiComplex :
        padPresets = ["romantic_pad1", "romantic_pad2", "romantic_pad3"]
        instrumentPad = Kontakt5

    #else :

    #    return

    preset = random.choice ( padPresets )

    # put clock to 0
    RPR_SetEditCurPos (0, True, True) # sets scroll cursor to the beginning 0 on timeline
    # inserts an empty track with no instrument added to it. 0 indicates track is inserted at 0th position
    RPR_InsertTrackAtIndex (0, True)

    RPR_Main_OnCommand (40297, 1) # unselects all tracks
    RPR_Main_OnCommand (40939, 1) # selects first track

    RPR_InsertMedia (file, 0) # inserts MIDI on new track.. Maybe change 1 to 0???



    # the first track id will always be 0
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), instrumentPad, True)  # adds instrument=kontakt5 on to the newly created track
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 0, preset) # set preset on the instrument
    RPR_SetMediaTrackInfo_Value (RPR_GetTrack (0, 0), "D_VOL", volume) # set volume for the track

    # adding different effect on to the drum tracks
    # learn later from Richard
    RPR_TrackFX_GetByName (RPR_GetTrack (0, 0), "ReaEQ (Cockos)", True)
    RPR_TrackFX_SetPreset (RPR_GetTrack (0, 0), 1, "HPF_melody")
    ParameterRandomization ( 1, 120, 235, 1, 0 ) #HiPass Filter Frequency

    RenameTrack (0, padName )



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

    elif mood == worldSimple or mood == worldSemiComplex :
        tempo = random.randint ( 70, 88 )

    elif mood == chillSimple or mood == chillSemiComplex :
        tempo = random.randint ( 84, 96 )

    elif mood == ampedSimple or mood == ampedSemiComplex :
        tempo = random.randint ( 108, 132 )

    elif mood == spookySimple or mood == spookySemiComplex :
        rand        = random.randint ( 1, 100 )
        if rand >= 50 :
            tempo = random.randint ( 48, 62 )
        else :
            tempo = random.randint ( 110, 126 )

    RPR_SetTempoTimeSigMarker( 0, -1, 0, 0-1, 0, tempo, 4, 4, True )



def getMood () :
    '''
    get mood from the thematic knob file
    '''

    file = open (newImportDirectory + "ThematicKnob.txt", 'r')
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



if __name__ == '__main__' :


    if startScript == True :

        InitializeReaper ()

        mood = getMood()
        #mood = romanticSimple
        setTempo ()
        #RPR_ShowConsoleMsg ( mood + "\n" )

        CreateDrumTracks ( mood )

        CreateMelodyTrack ( mood, importMIDIMelody )

        CreateArpeggioTracks ( mood, importMIDIArp1, "ARP 1" )
        CreateArpeggioTracks ( mood, importMIDIArp2, "ARP 2" )
        CreateArpeggioTracks ( mood, importMIDIArp3, "ARP 3" )

        if mood == romanticSimple or mood == romanticSemiComplex :
            CreateBassTrack (mood, importMIDIpiano, "PIANO" )
        else :
            CreateBassTrack ( mood, importMIDIBass, "BASS" )

        CreatePadTrack ( mood, importMIDIBass, "PAD" )
        CreateSubmixTrack ()



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

        RPR_Main_OnCommand ( 40026, 1 )  # save project
        RPR_Main_OnCommand ( 40004, 1 )  # quit reaper

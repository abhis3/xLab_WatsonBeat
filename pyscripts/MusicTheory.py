from __future__ import print_function

Notes = [ "C", "Cs",  "D", "Ds",  "E",  "F", "Fs",  "G", "Gs",  "A", "As",  "B" ] ;

QuarterNote = 0.25
EighthNote = 0.125
SixteenthNote = 0.0625
QuarterNoteAndRest = 0.25
EighthNoteAndRest = 0.125
SixteenthNoteAndRest = 0.0625

NoteDurations = [0.25, 0.125, 0.0625, 0.25, 0.125, 0.0625 ] 
MaxNotes = len(NoteDurations)-1

PitchToNotes = [ "C", "Cs",  "D", "Ds",  "E",  "F", "Fs",  "G", "Gs",  "A", "As",  "B" ] ;
NoteStrs  = [ "C", "Cs",  "D", "Ds",  "E",  "F", "Fs",  "G", "Gs",  "A", "As",  "B" ] ;


BassOctaveRange = [ 4, 4]
MelodyOctaveRange = [5, 5 ]
DefaultOctaveRange = [4, 5 ]

EightNoteInTicks = 240
SixteenthNoteInTicks = 120

NotesToPitch = {
  'C' : 0,
  'Cs': 1,
  'D' : 2, 
  'Ds': 3, 
  'E' : 4, 
  'F' : 5, 
  'Fs': 6, 
  'G' : 7, 
  'Gs': 8, 
  'A' : 9, 
  'As': 10,
  'B' : 11 } ;
  

pitchToNotes = {
  0 :'C'  ,
  1 :'Cs' ,
  2 :'D'  , 
  3 :'Ds' , 
  4 :'E'  , 
  5 :'F'  , 
  6 :'Fs' , 
  7 :'G'  , 
  8 :'Gs' , 
  9 :'A'  , 
  10:'As' ,
  11:'B'  , } ;
  

#Quartal Notes 
Quartal = { 
    'CMajor': [ 'C', 'D', 'E', 'G', 'A', ], 
    'CsMajor': [ 'Cs', 'Ds', 'F', 'Gs', 'As', ], 
    'DMajor': [ 'D', 'E', 'Fs', 'A', 'B', ], 
    'DsMajor': [ 'Ds', 'F', 'G', 'As', 'C', ], 
    'EMajor': [ 'E', 'Fs', 'Gs', 'B', 'Cs', ], 
    'FMajor': [ 'F', 'G', 'A', 'C', 'D', ], 
    'FsMajor': [ 'Fs', 'Gs', 'As', 'Cs', 'Ds', ], 
    'GMajor': [ 'G', 'A', 'B', 'D', 'E', ], 
    'GsMajor': [ 'Gs', 'As', 'C', 'Ds', 'F', ], 
    'AMajor': [ 'A', 'B', 'Cs', 'E', 'Fs', ], 
    'AsMajor': [ 'As', 'C', 'D', 'F', 'G', ], 
    'BMajor': [ 'B', 'Cs', 'Ds', 'Fs', 'Gs', ], 
    'CMinor': [ 'C', 'Ds', 'F', 'G', 'As', ], 
    'CsMinor': [ 'Cs', 'E', 'Fs', 'Gs', 'B', ], 
    'DMinor': [ 'D', 'F', 'G', 'A', 'C', ], 
    'DsMinor': [ 'Ds', 'Fs', 'Gs', 'As', 'Cs', ], 
    'EMinor': [ 'E', 'G', 'A', 'B', 'D', ], 
    'FMinor': [ 'F', 'Gs', 'As', 'C', 'Ds', ], 
    'FsMinor': [ 'Fs', 'A', 'B', 'Cs', 'E', ], 
    'GMinor': [ 'G', 'As', 'C', 'D', 'F', ], 
    'GsMinor': [ 'Gs', 'B', 'Cs', 'Ds', 'Fs', ], 
    'AMinor': [ 'A', 'C', 'D', 'E', 'G', ], 
    'AsMinor': [ 'As', 'Cs', 'Ds', 'F', 'Gs', ], 
    'BMinor': [ 'B', 'D', 'E', 'Fs', 'A', ], 

    'COct': [ 'C', 'Cs', 'Ds', 'E', 'Fs', 'G', 'A', 'As' ],    
    'CsOct': [ 'Cs', 'D', 'E', 'F', 'G', 'Gs', 'As', 'B' ],    
    'DOct': [ 'D', 'Ds', 'F', 'Fs', 'Gs', 'A', 'B', 'C' ],
    'CArabic': [ 'C', 'Cs', 'E', 'F', 'G', 'Gs', 'B' ],    

    'CHMinor': ['C', 'D', 'Ds', 'F', 'G', 'Gs', 'B']
}

#Quintal Notes 
Quintal = { 
    'CMajor': [ 'C', 'D', 'E', 'G', 'A', ], 
    'CsMajor': [ 'Cs', 'Ds', 'F', 'Gs', 'As', ], 
    'DMajor': [ 'D', 'E', 'Fs', 'A', 'B', ], 
    'DsMajor': [ 'Ds', 'F', 'G', 'As', 'C', ], 
    'EMajor': [ 'E', 'Fs', 'Gs', 'B', 'Cs', ], 
    'FMajor': [ 'F', 'G', 'A', 'C', 'D', ], 
    'FsMajor': [ 'Fs', 'Gs', 'As', 'Cs', 'Ds', ], 
    'GMajor': [ 'G', 'A', 'B', 'D', 'E', ], 
    'GsMajor': [ 'Gs', 'As', 'C', 'Ds', 'F', ], 
    'AMajor': [ 'A', 'B', 'Cs', 'E', 'Fs', ], 
    'AsMajor': [ 'As', 'C', 'D', 'F', 'G', ], 
    'BMajor': [ 'B', 'Cs', 'Ds', 'Fs', 'Gs', ], 
    'CMinor': [ 'C', 'Ds', 'F', 'G', 'As', ], 
    'CsMinor': [ 'Cs', 'E', 'Fs', 'Gs', 'B', ], 
    'DMinor': [ 'D', 'F', 'G', 'A', 'C', ], 
    'DsMinor': [ 'Ds', 'Fs', 'Gs', 'As', 'Cs', ], 
    'EMinor': [ 'E', 'G', 'A', 'B', 'D', ], 
    'FMinor': [ 'F', 'Gs', 'As', 'C', 'Ds', ], 
    'FsMinor': [ 'Fs', 'A', 'B', 'Cs', 'E', ], 
    'GMinor': [ 'G', 'As', 'C', 'D', 'F', ], 
    'GsMinor': [ 'Gs', 'B', 'Cs', 'Ds', 'Fs', ], 
    'AMinor': [ 'A', 'C', 'D', 'E', 'G', ], 
    'AsMinor': [ 'As', 'Cs', 'Ds', 'F', 'Gs', ], 
    'BMinor': [ 'B', 'D', 'E', 'Fs', 'A', ], 

    'COct': [ 'C', 'Cs', 'Ds', 'E', 'Fs', 'G', 'A', 'As' ],    
    'CsOct': [ 'Cs', 'D', 'E', 'F', 'G', 'Gs', 'As', 'B' ],    
    'DOct': [ 'D', 'Ds', 'F', 'Fs', 'Gs', 'A', 'B', 'C' ],
    'CArabic': [ 'C', 'Cs', 'E', 'F', 'G', 'Gs', 'B' ],    

    'CHMinor': ['C', 'D', 'Ds', 'F', 'G', 'Gs', 'B']
}


#Pentatonic Notes

PentatonicScale = {
    'CMajor': [ 'C', 'D', 'E', 'G', 'A', ], 
    'CsMajor': [ 'Cs', 'Ds', 'F', 'Gs', 'As', ], 
    'DMajor': [ 'D', 'E', 'Fs', 'A', 'B', ], 
    'DsMajor': [ 'Ds', 'F', 'G', 'As', 'C', ], 
    'EMajor': [ 'E', 'Fs', 'Gs', 'B', 'Cs', ], 
    'FMajor': [ 'F', 'G', 'A', 'C', 'D', ], 
    'FsMajor': [ 'Fs', 'Gs', 'As', 'Cs', 'Ds', ], 
    'GMajor': [ 'G', 'A', 'B', 'D', 'E', ], 
    'GsMajor': [ 'Gs', 'As', 'C', 'Ds', 'F', ], 
    'AMajor': [ 'A', 'B', 'Cs', 'E', 'Fs', ], 
    'AsMajor': [ 'As', 'C', 'D', 'F', 'G', ], 
    'BMajor': [ 'B', 'Cs', 'Ds', 'Fs', 'Gs', ], 
    'CMinor': [ 'C', 'Ds', 'F', 'G', 'As', ], 
    'CsMinor': [ 'Cs', 'E', 'Fs', 'Gs', 'B', ], 
    'DMinor': [ 'D', 'F', 'G', 'A', 'C', ], 
    'DsMinor': [ 'Ds', 'Fs', 'Gs', 'As', 'Cs', ], 
    'EMinor': [ 'E', 'G', 'A', 'B', 'D', ], 
    'FMinor': [ 'F', 'Gs', 'As', 'C', 'Ds', ], 
    'FsMinor': [ 'Fs', 'A', 'B', 'Cs', 'E', ], 
    'GMinor': [ 'G', 'As', 'C', 'D', 'F', ], 
    'GsMinor': [ 'Gs', 'B', 'Cs', 'Ds', 'Fs', ], 
    'AMinor': [ 'A', 'C', 'D', 'E', 'G', ], 
    'AsMinor': [ 'As', 'Cs', 'Ds', 'F', 'Gs', ], 
    'BMinor': [ 'B', 'D', 'E', 'Fs', 'A', ], 

    'COct': [ 'C', 'Cs', 'Ds', 'E', 'Fs', 'G', 'A', 'As' ],    
    'CsOct': [ 'Cs', 'D', 'E', 'F', 'G', 'Gs', 'As', 'B' ],    
    'DOct': [ 'D', 'Ds', 'F', 'Fs', 'Gs', 'A', 'B', 'C' ],
    'CArabic': [ 'C', 'Cs', 'E', 'F', 'G', 'Gs', 'B' ],    

    'CHMinor': ['C', 'D', 'Ds', 'F', 'G', 'Gs', 'B']


    }

#Pentatonic Note Index

Pentatonic = { 
    'CMajor': [1, 2, 3, 5, 6],
    'CsMajor': [1, 2, 3, 5, 6],
    'DMajor': [1, 2, 3, 5, 6],
    'DsMajor': [1, 2, 3, 5, 6],
    'EMajor': [1, 2, 3, 5, 6],
    'FMajor': [1, 2, 3, 5, 6],
    'FsMajor': [1, 2, 3, 5, 6],
    'GMajor': [1, 2, 3, 5, 6],
    'GsMajor': [1, 2, 3, 5, 6],
    'AMajor': [1, 2, 3, 5, 6],
    'AsMajor': [1, 2, 3, 5, 6],
    'BMajor': [1, 2, 3, 5, 6],
    'CMinor': [1, 3, 4, 5, 7],
    'CsMinor': [1, 3, 4, 5, 7],
    'DMinor': [1, 3, 4, 5, 7],
    'DsMinor': [1, 3, 4, 5, 7],
    'EMinor': [1, 3, 4, 5, 7],
    'FMinor': [1, 3, 4, 5, 7],
    'FsMinor': [1, 3, 4, 5, 7],
    'GMinor': [1, 3, 4, 5, 7],
    'GsMinor': [1, 3, 4, 5, 7],
    'AMinor': [1, 3, 4, 5, 7],
    'AsMinor': [1, 3, 4, 5, 7],
    'BMinor': [1, 3, 4, 5, 7],

    'Major':   [ 1,2,3,5,6] ,
    'Minor':   [ 1,3,4,5,7] ,

    'COct': [1, 2, 3, 4, 5, 6, 7, 8],
    'CsOct': [1, 2, 3, 4, 5, 6, 7, 8],
    'DOct': [1, 2, 3, 4, 5, 6, 7, 8],
    'Oct': [1, 2, 3, 4, 5, 6, 7, 8],

    'CArabic': [1, 2, 3, 4, 5, 6, 7],
    'CHMinor': [1, 3, 4, 5, 7],

    }


AcceptableChords = { 1: { 'acceptableNoteA': 3, 'acceptableNoteB': 5}, 
                     2: { 'acceptableNoteA': 4, 'acceptableNoteB': 6} ,
                     3: { 'acceptableNoteA': 5, 'acceptableNoteB': 7} ,
                     4: { 'acceptableNoteA': 6, 'acceptableNoteB': 1} ,
                     5: { 'acceptableNoteA': 7, 'acceptableNoteB': 2} ,
                     6: { 'acceptableNoteA': 1, 'acceptableNoteB': 3} ,
                     7: { 'acceptableNoteA': 2, 'acceptableNoteB': 4} ,
                     8: { 'acceptableNoteA': 3, 'acceptableNoteB': 5} ,
                     }  

AcceptableChordsOctatonic = {
    1: { 'acceptableNoteA': 4, 'acceptableNoteB': 6}, 
    2: { 'acceptableNoteA': 5, 'acceptableNoteB': 7} ,
    3: { 'acceptableNoteA': 6, 'acceptableNoteB': 8} ,
    4: { 'acceptableNoteA': 7, 'acceptableNoteB': 1} ,
    5: { 'acceptableNoteA': 8, 'acceptableNoteB': 2} ,
    6: { 'acceptableNoteA': 1, 'acceptableNoteB': 3} ,
    7: { 'acceptableNoteA': 2, 'acceptableNoteB': 4} ,
    8: { 'acceptableNoteA': 3, 'acceptableNoteB': 5} ,    
}  


#Diminished Chord List
DiminishedChord = {
    'CMajor': 7,
    'CsMajor': 7,
    'DMajor': 7,
    'DsMajor': 7,
    'EMajor': 7,
    'FMajor': 7,
    'FsMajor': 7,
    'GMajor': 7,
    'GsMajor': 7,
    'AMajor': 7,
    'AsMajor': 7,
    'BMajor': 7,
    'CMinor': 2,
    'CsMinor': 2,
    'DMinor': 2,
    'DsMinor': 2,
    'EMinor': 2,
    'FMinor': 2,
    'FsMinor': 2,
    'GMinor': 2,
    'GsMinor': 2,
    'AMinor': 2,
    'AsMinor': 2,
    'BMinor': 2,
    'COct': -1,
    'CsOct': -1,
    'DOct': -1,
    'CArabic': -1,

    'CHMinor': 2,
    }


#Key Dictionary

KeyDict = {
    'CMajor': { 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'A':6, 'B':7 },
    'CsMajor': { 'Cs':1, 'Ds':2, 'F':3, 'Fs':4, 'Gs':5, 'As':6, 'C':7 },
    'DMajor': { 'D':1, 'E':2, 'Fs':3, 'G':4, 'A':5, 'B':6, 'Cs':7 },
    'DsMajor': { 'Ds':1, 'F':2, 'G':3, 'Gs':4, 'As':5, 'C':6, 'D':7 },
    'EMajor': { 'E':1, 'Fs':2, 'Gs':3, 'A':4, 'B':5, 'Cs':6, 'Ds':7 },
    'FMajor': { 'F':1, 'G':2, 'A':3, 'As':4, 'C':5, 'D':6, 'E':7 },
    'FsMajor': { 'Fs':1, 'Gs':2, 'As':3, 'B':4, 'Cs':5, 'Ds':6, 'F':7 },
    'GMajor': { 'G':1, 'A':2, 'B':3, 'C':4, 'D':5, 'E':6, 'Fs':7 },
    'GsMajor': { 'Gs':1, 'As':2, 'C':3, 'Cs':4, 'Ds':5, 'F':6, 'G':7 },
    'AMajor': { 'A':1, 'B':2, 'Cs':3, 'D':4, 'E':5, 'Fs':6, 'Gs':7 },
    'AsMajor': { 'As':1, 'C':2, 'D':3, 'Ds':4, 'F':5, 'G':6, 'A':7 },
    'BMajor': { 'B':1, 'Cs':2, 'Ds':3, 'E':4, 'Fs':5, 'Gs':6, 'As':7 },
    'CMinor': { 'C':1, 'D':2, 'Ds':3, 'F':4, 'G':5, 'Gs':6, 'As':7 },
    'CsMinor': { 'Cs':1, 'Ds':2, 'E':3, 'Fs':4, 'Gs':5, 'A':6, 'B':7 },
    'DMinor': { 'D':1, 'E':2, 'F':3, 'G':4, 'A':5, 'As':6, 'C':7 },
    'DsMinor': { 'Ds':1, 'F':2, 'Fs':3, 'Gs':4, 'As':5, 'B':6, 'Cs':7 },
    'EMinor': { 'E':1, 'Fs':2, 'G':3, 'A':4, 'B':5, 'C':6, 'D':7 },
    'FMinor': { 'F':1, 'G':2, 'Gs':3, 'As':4, 'C':5, 'Cs':6, 'Ds':7 },
    'FsMinor': { 'Fs':1, 'Gs':2, 'A':3, 'B':4, 'Cs':5, 'D':6, 'E':7 },
    'GMinor': { 'G':1, 'A':2, 'As':3, 'C':4, 'D':5, 'Ds':6, 'F':7 },
    'GsMinor': { 'Gs':1, 'As':2, 'B':3, 'Cs':4, 'Ds':5, 'E':6, 'Fs':7 },
    'AMinor': { 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7 },
    'AsMinor': { 'As':1, 'C':2, 'Cs':3, 'Ds':4, 'F':5, 'Fs':6, 'Gs':7 },
    'BMinor': { 'B':1, 'Cs':2, 'D':3, 'E':4, 'Fs':5, 'G':6, 'A':7 },
    'COct': { 'C':1, 'Cs':2, 'Ds':3, 'E':4, 'Fs':5, 'G':6, 'A':7, 'As':8 },
    'CsOct': { 'Cs':1, 'D':2, 'E':3, 'F':4, 'G':5, 'Gs':6, 'As':7, 'B':8 },
    'DOct': { 'D':1, 'Ds':2, 'F':3, 'Fs':4, 'Gs':5, 'A':6, 'B':7, 'C':8 },
    'CArabic': { 'C':1, 'Cs':2, 'E':3, 'F':4, 'G':5, 'Gs':6, 'B':7 },

    'CHMinor': { 'C':1, 'D':2, 'Ds':3, 'F':4, 'G':5, 'Gs':6, 'B':7 },



    }
    #Reverse Key Dictionary

ReverseKeyDict = {
    'CMajor': { 1:'C', 2:'D', 3:'E', 4:'F', 5:'G', 6:'A', 7:'B' },
    'CsMajor': { 1:'Cs', 2:'Ds', 3:'F', 4:'Fs', 5:'Gs', 6:'As', 7:'C' },
    'DMajor': { 1:'D', 2:'E', 3:'Fs', 4:'G', 5:'A', 6:'B', 7:'Cs' },
    'DsMajor': { 1:'Ds', 2:'F', 3:'G', 4:'Gs', 5:'As', 6:'C', 7:'D' },
    'EMajor': { 1:'E', 2:'Fs', 3:'Gs', 4:'A', 5:'B', 6:'Cs', 7:'Ds' },
    'FMajor': { 1:'F', 2:'G', 3:'A', 4:'As', 5:'C', 6:'D', 7:'E' },
    'FsMajor': { 1:'Fs', 2:'Gs', 3:'As', 4:'B', 5:'Cs', 6:'Ds', 7:'F' },
    'GMajor': { 1:'G', 2:'A', 3:'B', 4:'C', 5:'D', 6:'E', 7:'Fs' },
    'GsMajor': { 1:'Gs', 2:'As', 3:'C', 4:'Cs', 5:'Ds', 6:'F', 7:'G' },
    'AMajor': { 1:'A', 2:'B', 3:'Cs', 4:'D', 5:'E', 6:'Fs', 7:'Gs' },
    'AsMajor': { 1:'As', 2:'C', 3:'D', 4:'Ds', 5:'F', 6:'G', 7:'A' },
    'BMajor': { 1:'B', 2:'Cs', 3:'Ds', 4:'E', 5:'Fs', 6:'Gs', 7:'As' },
    'CMinor': { 1:'C', 2:'D', 3:'Ds', 4:'F', 5:'G', 6:'Gs', 7:'As' },
    'CsMinor': { 1:'Cs', 2:'Ds', 3:'E', 4:'Fs', 5:'Gs', 6:'A', 7:'B' },
    'DMinor': { 1:'D', 2:'E', 3:'F', 4:'G', 5:'A', 6:'As', 7:'C' },
    'DsMinor': { 1:'Ds', 2:'F', 3:'Fs', 4:'Gs', 5:'As', 6:'B', 7:'Cs' },
    'EMinor': { 1:'E', 2:'Fs', 3:'G', 4:'A', 5:'B', 6:'C', 7:'D' },
    'FMinor': { 1:'F', 2:'G', 3:'Gs', 4:'As', 5:'C', 6:'Cs', 7:'Ds' },
    'FsMinor': { 1:'Fs', 2:'Gs', 3:'A', 4:'B', 5:'Cs', 6:'D', 7:'E' },
    'GMinor': { 1:'G', 2:'A', 3:'As', 4:'C', 5:'D', 6:'Ds', 7:'F' },
    'GsMinor': { 1:'Gs', 2:'As', 3:'B', 4:'Cs', 5:'Ds', 6:'E', 7:'Fs' },
    'AMinor': { 1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G' },
    'AsMinor': { 1:'As', 2:'C', 3:'Cs', 4:'Ds', 5:'F', 6:'Fs', 7:'Gs' },
    'BMinor': { 1:'B', 2:'Cs', 3:'D', 4:'E', 5:'Fs', 6:'G', 7:'A' },
    'COct': { 1:'C', 2:'Cs', 3:'Ds', 4:'E', 5:'Fs', 6:'G', 7:'A', 8:'As' },
    'CsOct': { 1:'Cs', 2:'D', 3:'E', 4:'F', 5:'G', 6:'Gs', 7:'As', 8:'B' },
    'DOct': { 1:'D', 2:'Ds', 3:'F', 4:'Fs', 5:'Gs', 6:'A', 7:'B', 8:'C' },
    'CArabic': { 1:'C', 2:'Cs', 3:'E', 4:'F', 5:'G', 6:'Gs', 7:'B' },

    'CHMinor': { 1:'C', 2:'D', 3:'Ds', 4:'F', 5:'G', 6:'Gs', 7:'B' },


    }


#Notes in Scale

NotesInScale = {
    'CMajor': [ 'C', 'D', 'E', 'F', 'G', 'A', 'B' ],
    'CsMajor': [ 'Cs', 'Ds', 'F', 'Fs', 'Gs', 'As', 'C' ],
    'DMajor': [ 'D', 'E', 'Fs', 'G', 'A', 'B', 'Cs' ],
    'DsMajor': [ 'Ds', 'F', 'G', 'Gs', 'As', 'C', 'D' ],
    'EMajor': [ 'E', 'Fs', 'Gs', 'A', 'B', 'Cs', 'Ds' ],
    'FMajor': [ 'F', 'G', 'A', 'As', 'C', 'D', 'E' ],
    'FsMajor': [ 'Fs', 'Gs', 'As', 'B', 'Cs', 'Ds', 'F' ],
    'GMajor': [ 'G', 'A', 'B', 'C', 'D', 'E', 'Fs' ],
    'GsMajor': [ 'Gs', 'As', 'C', 'Cs', 'Ds', 'F', 'G' ],
    'AMajor': [ 'A', 'B', 'Cs', 'D', 'E', 'Fs', 'Gs' ],
    'AsMajor': [ 'As', 'C', 'D', 'Ds', 'F', 'G', 'A' ],
    'BMajor': [ 'B', 'Cs', 'Ds', 'E', 'Fs', 'Gs', 'As' ],
    'CMinor': [ 'C', 'D', 'Ds', 'F', 'G', 'Gs', 'As' ],
    'CsMinor': [ 'Cs', 'Ds', 'E', 'Fs', 'Gs', 'A', 'B' ],
    'DMinor': [ 'D', 'E', 'F', 'G', 'A', 'As', 'C' ],
    'DsMinor': [ 'Ds', 'F', 'Fs', 'Gs', 'As', 'B', 'Cs' ],
    'EMinor': [ 'E', 'Fs', 'G', 'A', 'B', 'C', 'D' ],
    'FMinor': [ 'F', 'G', 'Gs', 'As', 'C', 'Cs', 'Ds' ],
    'FsMinor': [ 'Fs', 'Gs', 'A', 'B', 'Cs', 'D', 'E' ],
    'GMinor': [ 'G', 'A', 'As', 'C', 'D', 'Ds', 'F' ],
    'GsMinor': [ 'Gs', 'As', 'B', 'Cs', 'Ds', 'E', 'Fs' ],
    'AMinor': [ 'A', 'B', 'C', 'D', 'E', 'F', 'G' ],
    'AsMinor': [ 'As', 'C', 'Cs', 'Ds', 'F', 'Fs', 'Gs' ],
    'BMinor': [ 'B', 'Cs', 'D', 'E', 'Fs', 'G', 'A' ],
    'COct': [ 'C', 'Cs', 'Ds', 'E', 'Fs', 'G', 'A', 'As' ],
    'CsOct': [ 'Cs', 'D', 'E', 'F', 'G', 'Gs', 'As', 'B' ],
    'DOct': [ 'D', 'Ds', 'F', 'Fs', 'Gs', 'A', 'B', 'C' ],
    'CArabic': [ 'C', 'Cs', 'E', 'F', 'G', 'Gs', 'B' ],
    
    'CHMinor': ['C', 'D', 'Ds', 'F', 'G', 'Gs', 'B'],


    }

#Note Intensity

NoteIntensity = {
    'CMajor': { 'C':'Major', 'D':'Minor', 'E':'Minor', 'F':'Major', 'G':'Major', 'A':'Minor', 'B':'Dim' },
    'CsMajor': { 'Cs':'Major', 'Ds':'Minor', 'F':'Minor', 'Fs':'Major', 'Gs':'Major', 'As':'Minor', 'C':'Dim' },
    'DMajor': { 'D':'Major', 'E':'Minor', 'Fs':'Minor', 'G':'Major', 'A':'Major', 'B':'Minor', 'Cs':'Dim' },
    'DsMajor': { 'Ds':'Major', 'F':'Minor', 'G':'Minor', 'Gs':'Major', 'As':'Major', 'C':'Minor', 'D':'Dim' },
    'EMajor': { 'E':'Major', 'Fs':'Minor', 'Gs':'Minor', 'A':'Major', 'B':'Major', 'Cs':'Minor', 'Ds':'Dim' },
    'FMajor': { 'F':'Major', 'G':'Minor', 'A':'Minor', 'As':'Major', 'C':'Major', 'D':'Minor', 'E':'Dim' },
    'FsMajor': { 'Fs':'Major', 'Gs':'Minor', 'As':'Minor', 'B':'Major', 'Cs':'Major', 'Ds':'Minor', 'F':'Dim' },
    'GMajor': { 'G':'Major', 'A':'Minor', 'B':'Minor', 'C':'Major', 'D':'Major', 'E':'Minor', 'Fs':'Dim' },
    'GsMajor': { 'Gs':'Major', 'As':'Minor', 'C':'Minor', 'Cs':'Major', 'Ds':'Major', 'F':'Minor', 'G':'Dim' },
    'AMajor': { 'A':'Major', 'B':'Minor', 'Cs':'Minor', 'D':'Major', 'E':'Major', 'Fs':'Minor', 'Gs':'Dim' },
    'AsMajor': { 'As':'Major', 'C':'Minor', 'D':'Minor', 'Ds':'Major', 'F':'Major', 'G':'Minor', 'A':'Dim' },
    'BMajor': { 'B':'Major', 'Cs':'Minor', 'Ds':'Minor', 'E':'Major', 'Fs':'Major', 'Gs':'Minor', 'As':'Dim' },
    'CMinor': { 'C':'Minor', 'D':'Dim', 'Ds':'Major', 'F':'Minor', 'G':'Minor', 'Gs':'Major', 'As':'Major' },
    'CsMinor': { 'Cs':'Minor', 'Ds':'Dim', 'E':'Major', 'Fs':'Minor', 'Gs':'Minor', 'A':'Major', 'B':'Major' },
    'DMinor': { 'D':'Minor', 'E':'Dim', 'F':'Major', 'G':'Minor', 'A':'Minor', 'As':'Major', 'C':'Major' },
    'DsMinor': { 'Ds':'Minor', 'F':'Dim', 'Fs':'Major', 'Gs':'Minor', 'As':'Minor', 'B':'Major', 'Cs':'Major' },
    'EMinor': { 'E':'Minor', 'Fs':'Dim', 'G':'Major', 'A':'Minor', 'B':'Minor', 'C':'Major', 'D':'Major' },
    'FMinor': { 'F':'Minor', 'G':'Dim', 'Gs':'Major', 'As':'Minor', 'C':'Minor', 'Cs':'Major', 'Ds':'Major' },
    'FsMinor': { 'Fs':'Minor', 'Gs':'Dim', 'A':'Major', 'B':'Minor', 'Cs':'Minor', 'D':'Major', 'E':'Major' },
    'GMinor': { 'G':'Minor', 'A':'Dim', 'As':'Major', 'C':'Minor', 'D':'Minor', 'Ds':'Major', 'F':'Major' },
    'GsMinor': { 'Gs':'Minor', 'As':'Dim', 'B':'Major', 'Cs':'Minor', 'Ds':'Minor', 'E':'Major', 'Fs':'Major' },
    'AMinor': { 'A':'Minor', 'B':'Dim', 'C':'Major', 'D':'Minor', 'E':'Minor', 'F':'Major', 'G':'Major' },
    'AsMinor': { 'As':'Minor', 'C':'Dim', 'Cs':'Major', 'Ds':'Minor', 'F':'Minor', 'Fs':'Major', 'Gs':'Major' },
    'BMinor': { 'B':'Minor', 'Cs':'Dim', 'D':'Major', 'E':'Minor', 'Fs':'Minor', 'G':'Major', 'A':'Major' },
    'COct': { 'C':'Major', 'Cs':'Major', 'Ds':'Major', 'E':'Major', 'Fs':'Major', 'G':'Major', 'A':'Major', 'As':'Major' },
    'CsOct': { 'Cs':'Major', 'D':'Major', 'E':'Major', 'F':'Major', 'G':'Major', 'Gs':'Major', 'As':'Major', 'B':'Major' },
    'DOct': { 'D':'Major', 'Ds':'Major', 'F':'Major', 'Fs':'Major', 'Gs':'Major', 'A':'Major', 'B':'Major', 'C':'Major' },
    'CArabic': { 'C':'Minor', 'Cs':'Minor', 'E':'Minor', 'F':'Minor', 'G':'Minor', 'Gs':'Minor', 'B':'Minor' },

    'CHMinor': { 'C':'Minor', 'D':'Dim', 'Ds':'Major', 'F':'Minor', 'G':'Minor', 'Gs':'Major', 'B':'Dim' },

    }


tsInfo = {'resolution': 0, 'tsNumerator': 0, 'tsDenominator': 0, 'lenOfMeasure': 0, 'totalMeasures': 0 }


#Chord Progression List
ChordProgressions = {

    'CMajor': { 
        'C': ['D', 'E', 'F', 'G', 'A', 'B', ], 
        'D': ['C', 'G', 'B', ], 
        'E': ['A', 'F', ], 
        'F': ['C', 'D', 'G', 'B', ], 
        'G': ['C', 'E', 'A', ], 
        'A': ['D', 'F', 'G', ], 
        'B': ['C', 'E', 'G', ],  
        },

    'CsMajor': { 
        'Cs': ['Ds', 'F', 'Fs', 'Gs', 'As', 'C', ], 
        'Ds': ['Cs', 'Gs', 'C', ], 
        'F': ['As', 'Fs', ], 
        'Fs': ['Cs', 'Ds', 'Gs', 'C', ], 
        'Gs': ['Cs', 'F', 'As', ], 
        'As': ['Ds', 'Fs', 'Gs', ], 
        'C': ['Cs', 'F', 'Gs', ],  
        },

    'DMajor': { 
        'D': ['E', 'Fs', 'G', 'A', 'B', 'Cs', ], 
        'E': ['D', 'A', 'Cs', ], 
        'Fs': ['B', 'G', ], 
        'G': ['D', 'E', 'A', 'Cs', ], 
        'A': ['D', 'Fs', 'B', ], 
        'B': ['E', 'G', 'A', ], 
        'Cs': ['D', 'Fs', 'A', ],  
        },

    'DsMajor': { 
        'Ds': ['F', 'G', 'Gs', 'As', 'C', 'D', ], 
        'F': ['Ds', 'As', 'D', ], 
        'G': ['C', 'Gs', ], 
        'Gs': ['Ds', 'F', 'As', 'D', ], 
        'As': ['Ds', 'G', 'C', ], 
        'C': ['F', 'Gs', 'As', ], 
        'D': ['Ds', 'G', 'As', ],  
        },

    'EMajor': { 
        'E': ['Fs', 'Gs', 'A', 'B', 'Cs', 'Ds', ], 
        'Fs': ['E', 'B', 'Ds', ], 
        'Gs': ['Cs', 'A', ], 
        'A': ['E', 'Fs', 'B', 'Ds', ], 
        'B': ['E', 'Gs', 'Cs', ], 
        'Cs': ['Fs', 'A', 'B', ], 
        'Ds': ['E', 'Gs', 'B', ],  
        },
    'FMajor': { 
        'F': ['G', 'A', 'As', 'C', 'D', 'E', ], 
        'G': ['F', 'C', 'E', ], 
        'A': ['D', 'As', ], 
        'As': ['F', 'G', 'C', 'E', ], 
        'C': ['F', 'A', 'D', ], 
        'D': ['G', 'As', 'C', ], 
        'E': ['F', 'A', 'C', ],  
        },
    'FsMajor': { 
        'Fs': ['Gs', 'As', 'B', 'Cs', 'Ds', 'F', ], 
        'Gs': ['Fs', 'Cs', 'F', ], 
        'As': ['Ds', 'B', ], 
        'B': ['Fs', 'Gs', 'Cs', 'F', ], 
        'Cs': ['Fs', 'As', 'Ds', ], 
        'Ds': ['Gs', 'B', 'Cs', ], 
        'F': ['Fs', 'As', 'Cs', ],  
        },
    'GMajor': { 
        'G': ['A', 'B', 'C', 'D', 'E', 'Fs', ], 
        'A': ['G', 'D', 'Fs', ], 
        'B': ['E', 'C', ], 
        'C': ['G', 'A', 'D', 'Fs', ], 
        'D': ['G', 'B', 'E', ], 
        'E': ['A', 'C', 'D', ], 
        'Fs': ['G', 'B', 'D', ],  
        },
    'GsMajor': { 
        'Gs': ['As', 'C', 'Cs', 'Ds', 'F', 'G', ], 
        'As': ['Gs', 'Ds', 'G', ], 
        'C': ['F', 'Cs', ], 
        'Cs': ['Gs', 'As', 'Ds', 'G', ], 
        'Ds': ['Gs', 'C', 'F', ], 
        'F': ['As', 'Cs', 'Ds', ], 
        'G': ['Gs', 'C', 'Ds', ],  
        },
    'AMajor': { 
        'A': ['B', 'Cs', 'D', 'E', 'Fs', 'Gs', ], 
        'B': ['A', 'E', 'Gs', ], 
        'Cs': ['Fs', 'D', ], 
        'D': ['A', 'B', 'E', 'Gs', ], 
        'E': ['A', 'Cs', 'Fs', ], 
        'Fs': ['B', 'D', 'E', ], 
        'Gs': ['A', 'Cs', 'E', ],  
        },
    'AsMajor': { 
        'As': ['C', 'D', 'Ds', 'F', 'G', 'A', ], 
        'C': ['As', 'F', 'A', ], 
        'D': ['G', 'Ds', ], 
        'Ds': ['As', 'C', 'F', 'A', ], 
        'F': ['As', 'D', 'G', ], 
        'G': ['C', 'Ds', 'F', ], 
        'A': ['As', 'D', 'F', ],  
        },
    'BMajor': { 
        'B': ['Cs', 'Ds', 'E', 'Fs', 'Gs', 'As', ], 
        'Cs': ['B', 'Fs', 'As', ], 
        'Ds': ['Gs', 'E', ], 
        'E': ['B', 'Cs', 'Fs', 'As', ], 
        'Fs': ['B', 'Ds', 'Gs', ], 
        'Gs': ['Cs', 'E', 'Fs', ], 
        'As': ['B', 'Ds', 'Fs', ],  
        },
    'CMinor': { 
        'C': ['D', 'Ds', 'F', 'G', 'Gs', 'As', ], 
        'D': ['C', 'G', 'As', ], 
        'Ds': ['Gs', 'F', ], 
        'F': ['C', 'D', 'G', 'As', ], 
        'G': ['C', 'Ds', 'Gs', ], 
        'Gs': ['D', 'F', 'G', ], 
        'As': ['C', 'Ds', 'G', ],  
},
    'CsMinor': { 
        'Cs': ['Ds', 'E', 'Fs', 'Gs', 'A', 'B', ], 
        'Ds': ['Cs', 'Gs', 'B', ], 
        'E': ['A', 'Fs', ], 
        'Fs': ['Cs', 'Ds', 'Gs', 'B', ], 
        'Gs': ['Cs', 'E', 'A', ], 
        'A': ['Ds', 'Fs', 'Gs', ], 
        'B': ['Cs', 'E', 'Gs', ],  
        },
    'DMinor': { 
        'D': ['E', 'F', 'G', 'A', 'As', 'C', ], 
        'E': ['D', 'A', 'C', ], 
        'F': ['As', 'G', ], 
        'G': ['D', 'E', 'A', 'C', ], 
        'A': ['D', 'F', 'As', ], 
        'As': ['E', 'G', 'A', ], 
        'C': ['D', 'F', 'A', ],  
        },
    'DsMinor': { 
        'Ds': ['F', 'Fs', 'Gs', 'As', 'B', 'Cs', ], 
        'F': ['Ds', 'As', 'Cs', ], 
        'Fs': ['B', 'Gs', ], 
        'Gs': ['Ds', 'F', 'As', 'Cs', ], 
        'As': ['Ds', 'Fs', 'B', ], 
        'B': ['F', 'Gs', 'As', ], 
        'Cs': ['Ds', 'Fs', 'As', ],  
        },
    'EMinor': { 
        'E': ['Fs', 'G', 'A', 'B', 'C', 'D', ], 
        'Fs': ['E', 'B', 'D', ], 
        'G': ['C', 'A', ], 
        'A': ['E', 'Fs', 'B', 'D', ], 
        'B': ['E', 'G', 'C', ], 
        'C': ['Fs', 'A', 'B', ], 
        'D': ['E', 'G', 'B', ],  
        },
    'FMinor': { 
        'F': ['G', 'Gs', 'As', 'C', 'Cs', 'Ds', ], 
        'G': ['F', 'C', 'Ds', ], 
        'Gs': ['Cs', 'As', ], 
        'As': ['F', 'G', 'C', 'Ds', ], 
        'C': ['F', 'Gs', 'Cs', ], 
        'Cs': ['G', 'As', 'C', ], 
        'Ds': ['F', 'Gs', 'C', ],  
        },
    'FsMinor': { 
        'Fs': ['Gs', 'A', 'B', 'Cs', 'D', 'E', ], 
        'Gs': ['Fs', 'Cs', 'E', ], 
        'A': ['D', 'B', ], 
        'B': ['Fs', 'Gs', 'Cs', 'E', ], 
        'Cs': ['Fs', 'A', 'D', ], 
        'D': ['Gs', 'B', 'Cs', ], 
        'E': ['Fs', 'A', 'Cs', ],  
        },
    'GMinor': { 
        'G': ['A', 'As', 'C', 'D', 'Ds', 'F', ], 
        'A': ['G', 'D', 'F', ], 
        'As': ['Ds', 'C', ], 
        'C': ['G', 'A', 'D', 'F', ], 
        'D': ['G', 'As', 'Ds', ], 
        'Ds': ['A', 'C', 'D', ], 
        'F': ['G', 'As', 'D', ],  
        },
    'GsMinor': { 
        'Gs': ['As', 'B', 'Cs', 'Ds', 'E', 'Fs', ], 
        'As': ['Gs', 'Ds', 'Fs', ], 
        'B': ['E', 'Cs', ], 
        'Cs': ['Gs', 'As', 'Ds', 'Fs', ], 
        'Ds': ['Gs', 'B', 'E', ], 
        'E': ['As', 'Cs', 'Ds', ], 
        'Fs': ['Gs', 'B', 'Ds', ],  
        },
    'AMinor': { 
        'A': ['B', 'C', 'D', 'E', 'F', 'G', ], 
        'B': ['A', 'E', 'G', ], 
        'C': ['F', 'D', ], 
        'D': ['A', 'B', 'E', 'G', ], 
        'E': ['A', 'C', 'F', ], 
        'F': ['B', 'D', 'E', ], 
        'G': ['A', 'C', 'E', ],  
        },
    'AsMinor': { 
        'As': ['C', 'Cs', 'Ds', 'F', 'Fs', 'Gs', ], 
        'C': ['As', 'F', 'Gs', ], 
        'Cs': ['Fs', 'Ds', ], 
        'Ds': ['As', 'C', 'F', 'Gs', ], 
        'F': ['As', 'Cs', 'Fs', ], 
        'Fs': ['C', 'Ds', 'F', ], 
        'Gs': ['As', 'Cs', 'F', ],  
        },
    'BMinor': { 
        'B': ['Cs', 'D', 'E', 'Fs', 'G', 'A', ], 
        'Cs': ['B', 'Fs', 'A', ], 
        'D': ['G', 'E', ], 
        'E': ['B', 'Cs', 'Fs', 'A', ], 
        'Fs': ['B', 'D', 'G', ], 
        'G': ['Cs', 'E', 'Fs', ], 
        'A': ['B', 'D', 'Fs', ],  
        },
    'COct': { 
        'C': ['Cs', 'Ds', 'E', 'Fs', 'G', 'A', 'As', ], 
        'Cs': ['C', 'Ds', 'E', 'Fs', 'G', 'A', 'As', ], 
        'Ds': ['C', 'Cs', 'E', 'Fs', 'G', 'A', 'As', ], 
        'E': ['C', 'Cs', 'Ds', 'Fs', 'G', 'A', 'As', ], 
        'Fs': ['C', 'Cs', 'Ds', 'E', 'G', 'A', 'As', ], 
        'G': ['C', 'Cs', 'Ds', 'E', 'Fs', 'A', 'As', ], 
        'A': ['C', 'Cs', 'Ds', 'E', 'Fs', 'G', 'As', ], 
        'As': ['C', 'Cs', 'Ds', 'E', 'Fs', 'G', 'A', ],  
        },
    'CsOct': { 
        'Cs': ['D', 'E', 'F', 'G', 'Gs', 'As', 'B', ], 
        'D': ['Cs', 'E', 'F', 'G', 'Gs', 'As', 'B', ], 
        'E': ['Cs', 'D', 'F', 'G', 'Gs', 'As', 'B', ], 
        'F': ['Cs', 'D', 'E', 'G', 'Gs', 'As', 'B', ], 
        'G': ['Cs', 'D', 'E', 'F', 'Gs', 'As', 'B', ], 
        'Gs': ['Cs', 'D', 'E', 'F', 'G', 'As', 'B', ], 
        'As': ['Cs', 'D', 'E', 'F', 'G', 'Gs', 'B', ], 
        'B': ['Cs', 'D', 'E', 'F', 'G', 'Gs', 'As', ],  
        },
    'DOct': { 
        'D': ['Ds', 'F', 'Fs', 'Gs', 'A', 'B', 'C', ], 
        'Ds': ['D', 'F', 'Fs', 'Gs', 'A', 'B', 'C', ], 
        'F': ['D', 'Ds', 'Fs', 'Gs', 'A', 'B', 'C', ], 
        'Fs': ['D', 'Ds', 'F', 'Gs', 'A', 'B', 'C', ], 
        'Gs': ['D', 'Ds', 'F', 'Fs', 'A', 'B', 'C', ], 
        'A': ['D', 'Ds', 'F', 'Fs', 'Gs', 'B', 'C', ], 
        'B': ['D', 'Ds', 'F', 'Fs', 'Gs', 'A', 'C', ], 
        'C': ['D', 'Ds', 'F', 'Fs', 'Gs', 'A', 'B', ],  
        },

    'CArabic': { 
        'C': ['Cs', 'E', 'F', 'G', 'Gs', 'B', ], 
        'Cs': ['C', 'E', 'F', 'G', 'Gs', 'B', ], 
        'E': ['C', 'Cs', 'F', 'G', 'Gs', 'B', ], 
        'F': ['C', 'Cs', 'E', 'G', 'Gs', 'B', ], 
        'G': ['C', 'Cs', 'E', 'F', 'Gs', 'B', ], 
        'Gs': ['C', 'Cs', 'E', 'F', 'G', 'B', ], 
        'B': ['C', 'Cs', 'E', 'F', 'G', 'Gs', ],  
        },


    'CHMinor': { 
        'C': ['D', 'Ds', 'F', 'G', 'Gs', 'B', ], 
        'D': ['C', 'G', 'B', ], 
        'Ds': ['Gs', 'F', ], 
        'F': ['C', 'D', 'G', 'B', ], 
        'G': ['C', 'Ds', 'Gs', ], 
        'Gs': ['D', 'F', 'G', ], 
        'B': ['C', 'Ds', 'G', ],  
        },

    

    }

#First Measure Note List


FirstMeasureNotes = { 

    'CMajor': [ 'C', 'F', 'G', ], 
    'CsMajor': [ 'Cs', 'Fs', 'Gs', ], 
    'DMajor': [ 'D', 'G', 'A', ], 
    'DsMajor': [ 'Ds', 'Gs', 'As', ], 
    'EMajor': [ 'E', 'A', 'B', ], 
    'FMajor': [ 'F', 'As', 'C', ], 
    'FsMajor': [ 'Fs', 'B', 'Cs', ], 
    'GMajor': [ 'G', 'C', 'D', ], 
    'GsMajor': [ 'Gs', 'Cs', 'Ds', ], 
    'AMajor': [ 'A', 'D', 'E', ], 
    'AsMajor': [ 'As', 'Ds', 'F', ], 
    'BMajor': [ 'B', 'E', 'Fs', ], 
    'CMinor': [ 'C', 'F', 'G', ], 
    'CsMinor': [ 'Cs', 'Fs', 'Gs', ], 
    'DMinor': [ 'D', 'G', 'A', ], 
    'DsMinor': [ 'Ds', 'Gs', 'As', ], 
    'EMinor': [ 'E', 'A', 'B', ], 
    'FMinor': [ 'F', 'As', 'C', ], 
    'FsMinor': [ 'Fs', 'B', 'Cs', ], 
    'GMinor': [ 'G', 'C', 'D', ], 
    'GsMinor': [ 'Gs', 'Cs', 'Ds', ], 
    'AMinor': [ 'A', 'D', 'E', ], 
    'AsMinor': [ 'As', 'Ds', 'F', ], 
    'BMinor': [ 'B', 'E', 'Fs', ], 
    'COct': [ 'C', 'Ds', 'Fs', 'A', ], 
    'CsOct': [ 'Cs', 'E', 'G', 'As', ], 
    'DOct': [ 'D', 'F', 'Gs', 'B', ], 
    'CArabic': [ 'C', 'F', 'G', ], 

    'CHMinor': [ 'C', 'F', 'G', ], 

}

Chords = { 
    'CMajor': { 
        'C': ['C', 'E', 'G'],
        'D': ['D', 'F', 'A'],
        'E': ['E', 'G', 'B'],
        'F': ['F', 'A', 'C'],
        'G': ['G', 'B', 'D'],
        'A': ['A', 'C', 'E'],
        'B': ['B', 'D', 'F'],
        },
    
    'CsMajor': { 
        'Cs': ['Cs', 'F', 'Gs'],
        'Ds': ['Ds', 'Fs', 'As'],
        'F': ['F', 'Gs', 'C'],
        'Fs': ['Fs', 'As', 'Cs'],
        'Gs': ['Gs', 'C', 'Ds'],
        'As': ['As', 'Cs', 'F'],
        'C': ['C', 'Ds', 'Fs'],
        },
    
    'DMajor': { 
        'D': ['D', 'Fs', 'A'],
        'E': ['E', 'G', 'B'],
        'Fs': ['Fs', 'A', 'Cs'],
        'G': ['G', 'B', 'D'],
        'A': ['A', 'Cs', 'E'],
        'B': ['B', 'D', 'Fs'],
        'Cs': ['Cs', 'E', 'G'],
        },
    
    'DsMajor': { 
        'Ds': ['Ds', 'G', 'As'],
        'F': ['F', 'Gs', 'C'],
        'G': ['G', 'As', 'D'],
        'Gs': ['Gs', 'C', 'Ds'],
        'As': ['As', 'D', 'F'],
        'C': ['C', 'Ds', 'G'],
        'D': ['D', 'F', 'Gs'],
        },
    
    'EMajor': { 
        'E': ['E', 'Gs', 'B'],
        'Fs': ['Fs', 'A', 'Cs'],
        'Gs': ['Gs', 'B', 'Ds'],
        'A': ['A', 'Cs', 'E'],
        'B': ['B', 'Ds', 'Fs'],
        'Cs': ['Cs', 'E', 'Gs'],
        'Ds': ['Ds', 'Fs', 'A'],
        },
    
    'FMajor': { 
        'F': ['F', 'A', 'C'],
        'G': ['G', 'As', 'D'],
        'A': ['A', 'C', 'E'],
        'As': ['As', 'D', 'F'],
        'C': ['C', 'E', 'G'],
        'D': ['D', 'F', 'A'],
        'E': ['E', 'G', 'As'],
        },
    
    'FsMajor': { 
        'Fs': ['Fs', 'As', 'Cs'],
        'Gs': ['Gs', 'B', 'Ds'],
        'As': ['As', 'Cs', 'F'],
        'B': ['B', 'Ds', 'Fs'],
        'Cs': ['Cs', 'F', 'Gs'],
        'Ds': ['Ds', 'Fs', 'As'],
        'F': ['F', 'Gs', 'B'],
        },
    
    'GMajor': { 
        'G': ['G', 'B', 'D'],
        'A': ['A', 'C', 'E'],
        'B': ['B', 'D', 'Fs'],
        'C': ['C', 'E', 'G'],
        'D': ['D', 'Fs', 'A'],
        'E': ['E', 'G', 'B'],
        'Fs': ['Fs', 'A', 'C'],
        },
    
    'GsMajor': { 
        'Gs': ['Gs', 'C', 'Ds'],
        'As': ['As', 'Cs', 'F'],
        'C': ['C', 'Ds', 'G'],
        'Cs': ['Cs', 'F', 'Gs'],
        'Ds': ['Ds', 'G', 'As'],
        'F': ['F', 'Gs', 'C'],
        'G': ['G', 'As', 'Cs'],
        },
    
    'AMajor': { 
        'A': ['A', 'Cs', 'E'],
        'B': ['B', 'D', 'Fs'],
        'Cs': ['Cs', 'E', 'Gs'],
        'D': ['D', 'Fs', 'A'],
        'E': ['E', 'Gs', 'B'],
        'Fs': ['Fs', 'A', 'Cs'],
        'Gs': ['Gs', 'B', 'D'],
        },
    
    'AsMajor': { 
        'As': ['As', 'D', 'F'],
        'C': ['C', 'Ds', 'G'],
        'D': ['D', 'F', 'A'],
        'Ds': ['Ds', 'G', 'As'],
        'F': ['F', 'A', 'C'],
        'G': ['G', 'As', 'D'],
        'A': ['A', 'C', 'Ds'],
        },
    
    'BMajor': { 
        'B': ['B', 'Ds', 'Fs'],
        'Cs': ['Cs', 'E', 'Gs'],
        'Ds': ['Ds', 'Fs', 'As'],
        'E': ['E', 'Gs', 'B'],
        'Fs': ['Fs', 'As', 'Cs'],
        'Gs': ['Gs', 'B', 'Ds'],
        'As': ['As', 'Cs', 'E'],
        },
    
    'CMinor': { 
        'C': ['C', 'Ds', 'G'],
        'D': ['D', 'F', 'Gs'],
        'Ds': ['Ds', 'G', 'As'],
        'F': ['F', 'Gs', 'C'],
        'G': ['G', 'As', 'D'],
        'Gs': ['Gs', 'C', 'Ds'],
        'As': ['As', 'D', 'F'],
        },
    
    'CsMinor': { 
        'Cs': ['Cs', 'E', 'Gs'],
        'Ds': ['Ds', 'Fs', 'A'],
        'E': ['E', 'Gs', 'B'],
        'Fs': ['Fs', 'A', 'Cs'],
        'Gs': ['Gs', 'B', 'Ds'],
        'A': ['A', 'Cs', 'E'],
        'B': ['B', 'Ds', 'Fs'],
        },
    
    'DMinor': { 
        'D': ['D', 'F', 'A'],
        'E': ['E', 'G', 'As'],
        'F': ['F', 'A', 'C'],
        'G': ['G', 'As', 'D'],
        'A': ['A', 'C', 'E'],
        'As': ['As', 'D', 'F'],
        'C': ['C', 'E', 'G'],
        },
    
    'DsMinor': { 
        'Ds': ['Ds', 'Fs', 'As'],
        'F': ['F', 'Gs', 'B'],
        'Fs': ['Fs', 'As', 'Cs'],
        'Gs': ['Gs', 'B', 'Ds'],
        'As': ['As', 'Cs', 'F'],
        'B': ['B', 'Ds', 'Fs'],
        'Cs': ['Cs', 'F', 'Gs'],
        },
    
    'EMinor': { 
        'E': ['E', 'G', 'B'],
        'Fs': ['Fs', 'A', 'C'],
        'G': ['G', 'B', 'D'],
        'A': ['A', 'C', 'E'],
        'B': ['B', 'D', 'Fs'],
        'C': ['C', 'E', 'G'],
        'D': ['D', 'Fs', 'A'],
        },
    
    'FMinor': { 
        'F': ['F', 'Gs', 'C'],
        'G': ['G', 'As', 'Cs'],
        'Gs': ['Gs', 'C', 'Ds'],
        'As': ['As', 'Cs', 'F'],
        'C': ['C', 'Ds', 'G'],
        'Cs': ['Cs', 'F', 'Gs'],
        'Ds': ['Ds', 'G', 'As'],
        },
    
    'FsMinor': { 
        'Fs': ['Fs', 'A', 'Cs'],
        'Gs': ['Gs', 'B', 'D'],
        'A': ['A', 'Cs', 'E'],
        'B': ['B', 'D', 'Fs'],
        'Cs': ['Cs', 'E', 'Gs'],
        'D': ['D', 'Fs', 'A'],
        'E': ['E', 'Gs', 'B'],
        },
    
    'GMinor': { 
        'G': ['G', 'As', 'D'],
        'A': ['A', 'C', 'Ds'],
        'As': ['As', 'D', 'F'],
        'C': ['C', 'Ds', 'G'],
        'D': ['D', 'F', 'A'],
        'Ds': ['Ds', 'G', 'As'],
        'F': ['F', 'A', 'C'],
        },
    
    'GsMinor': { 
        'Gs': ['Gs', 'B', 'Ds'],
        'As': ['As', 'Cs', 'E'],
        'B': ['B', 'Ds', 'Fs'],
        'Cs': ['Cs', 'E', 'Gs'],
        'Ds': ['Ds', 'Fs', 'As'],
        'E': ['E', 'Gs', 'B'],
        'Fs': ['Fs', 'As', 'Cs'],
        },
    
    'AMinor': { 
        'A': ['A', 'C', 'E'],
        'B': ['B', 'D', 'F'],
        'C': ['C', 'E', 'G'],
        'D': ['D', 'F', 'A'],
        'E': ['E', 'G', 'B'],
        'F': ['F', 'A', 'C'],
        'G': ['G', 'B', 'D'],
        },
    
    'AsMinor': { 
        'As': ['As', 'Cs', 'F'],
        'C': ['C', 'Ds', 'Fs'],
        'Cs': ['Cs', 'F', 'Gs'],
        'Ds': ['Ds', 'Fs', 'As'],
        'F': ['F', 'Gs', 'C'],
        'Fs': ['Fs', 'As', 'Cs'],
        'Gs': ['Gs', 'C', 'Ds'],
        },
    
    'BMinor': { 
        'B': ['B', 'D', 'Fs'],
        'Cs': ['Cs', 'E', 'G'],
        'D': ['D', 'Fs', 'A'],
        'E': ['E', 'G', 'B'],
        'Fs': ['Fs', 'A', 'Cs'],
        'G': ['G', 'B', 'D'],
        'A': ['A', 'Cs', 'E'],
        },
    }

StartingPieceNotes = {    # start piece with either Tonic or Dominant note for that scale
    'CMajor': [ 'C', 'G' ], 

    }





ChordTones = { 
    'CMajor':  { 'C': [ 'E', 'G' ],
                 'D': [ 'F', 'A' ], 
                 'E': [ 'G', 'B' ], 
                 'F': [ 'A', 'C' ], 
                 'G': [ 'B', 'D' ], 
                 'A': [ 'C', 'E' ], 
                 'B': [ 'D', 'F' ], 
                 },
    
    }

NeighborTones = { 
    'CMajor':  { 'C': [ 'D', 'B' ],
                 'D': [ 'E', 'C' ], 
                 'E': [ 'F', 'D' ], 
                 'F': [ 'G', 'E' ], 
                 'G': [ 'A', 'F' ], 
                 'A': [ 'B', 'G' ], 
                 'B': [ 'C', 'A' ], 
                 },   
    }


PassingTones = {
    'CMajor':  { 'C': [ [ 'D', 'E' ], ['B', 'A', 'G' ] ],
                 'D': [ [ 'E', 'F' ], ['C', 'B', 'A' ] ], 
                 'E': [ [ 'F', 'G' ], ['D', 'C', 'B' ] ], 
                 'F': [ [ 'G', 'A' ], ['E', 'D', 'C' ] ], 
                 'G': [ [ 'A', 'B' ], ['F', 'E', 'D' ] ], 
                 'A': [ [ 'B', 'C' ], ['G', 'F', 'E' ] ], 
                 'B': [ [ 'C', 'D' ], ['A', 'G', 'F' ] ], 
                 },   
    }

OtherTones = {
    'CMajor':  { 'C': [ 'F' ],
                 'D': [ 'G' ], 
                 'E': [ 'A' ], 
                 'F': [ 'B' ], 
                 'G': [ 'C' ], 
                 'A': [ 'D' ], 
                 'B': [ 'E' ], 
                 },   
    }

PosChromatics = {
    'C':  'Cs' ,
    'Cs':  'D' ,

    'D':  'Ds' ,
    'Ds':  'E' ,

    'E':  'F',  

    'F':  'Fs' ,
    'Fs':  'G' ,

    'G':  'Gs' ,
    'Gs': 'A' , 

    'A':  'As' ,
    'As':  'B' ,

    'B':  'C' ,
}


NegChromatics = {
    'C':  'B' ,
    'Cs':  'C' ,

    'D':  'Cs' ,
    'Ds':  'D' ,

    'E':  'Ds', 

    'F':  'E' ,
    'Fs':  'F' ,

    'G':  'Fs' ,
    'Gs': 'G' , 

    'A':  'Gs' ,
    'As':  'A' ,

    'B':  'As' ,

}



NextChordProgressions = { 'CMajor': { 'C': ['F', 'E', 'G', 'A', ],
                                      'D': ['E', 'G', 'C' ],
                                      'E': ['F', 'A' ],
                                      'F': ['G', 'D', 'C'],
                                      'G': ['C', 'E', 'A'],
                                      'A': ['D', 'F' ],
                                      'B': ['C' ]
                                      },
                          }

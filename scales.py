# -*- coding: utf-8 -*-


from notes import Note


CHROMATIC_SCALE_ASC = [
    Note('C'),
    Note('C', '#'),
    Note('D'),
    Note('D', '#'),
    Note('E'),
    Note('F'),
    Note('F', '#'),
    Note('G'),
    Note('G', '#'),
    Note('A'),
    Note('A', '#'),
    Note('B')
]

CHROMATIC_SCALE_DESC = [
    Note('B'),
    Note('B', 'b'),
    Note('A'),
    Note('A', 'b'),
    Note('G'),
    Note('G', 'b'),
    Note('F'),
    Note('E'),
    Note('E', 'b'),
    Note('D'),
    Note('D', 'b'),
    Note('C')
]


class DiatonicScale(object):

    INTERVAL_AMOUNT = 7
    MODES_INTERVALS = {
        'ionian': [2, 2, 1, 2, 2, 2, 1], # major scale
        'dorian': [2, 1, 2, 2, 2, 1, 2],
        'phrygian': [1, 2, 2, 2, 1, 2, 2],
        'lydian': [2, 2, 2, 1, 2, 2, 1],
        'mixolydian': [2, 2, 1, 2, 2, 1, 2],
        'aeolian': [2, 1, 2, 2, 1, 2, 2], # natural minor scale
        'locrian': [1, 2, 2, 1, 2, 2, 2]
    }

    def __init__(self, intervals):
        if len(intervals) != DiatonicScale.INTERVAL_AMOUNT:
            raise Exception('The scale must contain %d intervals' % DiatonicScale.INTERVAL_AMOUNT)

        tones_num = len(list(filter(lambda i: i == 2, intervals)))
        semitones_num = len(list(filter(lambda i: i == 1, intervals)))

        if tones_num != 5 or semitones_num != 2:
            raise Exception('Diatonic scales contain 5 tones and 2 semitones intervals')

        self.intervals = intervals

    @staticmethod
    def mode_scale(mode):
        return DiatonicScale(DiatonicScale.MODES_INTERVALS[mode])

    @staticmethod
    def major_scale():
        return DiatonicScale.mode_scale('ionian')

    @staticmethod
    def minor_scale():
        return DiatonicScale.mode_scale('aeolian')

    # TODO check when accidental is flat
    def note_scale_with_octave(self, name, accidental='', octave=4):
        scale = list()
        tonic = None
        c = 0 # counter for chromatic scale

        while not tonic:
            note = CHROMATIC_SCALE_ASC[c]
            if note.name == name and note.accidental == accidental:
                tonic = note.change_octave(octave)
                scale.append(tonic)

            c = c + 1

        i = 0
        c = c - 1
        while len(scale) < (DiatonicScale.INTERVAL_AMOUNT + 1):
            c = c + self.intervals[i]

            if c >= len(CHROMATIC_SCALE_ASC):
                c = c % len(CHROMATIC_SCALE_ASC)
                octave = octave + 1

            note = CHROMATIC_SCALE_ASC[c]
            scale.append(note.change_octave(octave))

            i = i + 1

        return scale

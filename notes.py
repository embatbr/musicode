# -*- coding: utf-8 -*-


class Note(object):

    FREQUENCY_FACTOR = {
        'C': 1,
        'D': 9/8,
        'E': 5/4,
        'F': 4/3,
        'G': 3/2,
        'A': 5/3,
        'B': 15/8
    }
    ACCIDENTALS = ('b', '', '#')
    FIRST_OCTAVE_RANGE = (33, 61.875)

    def __init__(self, name, accidental='', octave=4):
        if name not in Note.FREQUENCY_FACTOR.keys():
            raise Exception("Note name doesn't exist")
        self.name = name

        if accidental not in Note.ACCIDENTALS:
            raise Exception("Note accidental doesn't exist")
        self.accidental = accidental

        if octave < 1 or octave > 8:
            raise Exception('Octave out of range')
        self.octave = octave

    def __str__(self):
        return '%s%s' % (self.name, self.accidental)

    def __repr__(self):
        options = {
            'b': 'flat',
            '': 'natural',
            '#': 'sharp'
        }
        accidental_name = options[self.accidental]

        return '%s %s in octave %d' % (self.name, accidental_name, self.octave)

    @property
    def frequency(self):
        factor = Note.FREQUENCY_FACTOR[self.name]

        first_octave_C = Note.FIRST_OCTAVE_RANGE[0]
        frequency = first_octave_C * factor * 2**(self.octave - 1)

        if self.accidental == 'b':
            frequency = (frequency * 15) / 16

        if self.accidental == '#':
            frequency = (frequency * 16) / 15

        return round(frequency, 2)

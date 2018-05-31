# -*- coding: utf-8 -*-


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
ZEROTH_OCTAVE_RANGE = (16.5, 30.9375)


class Note(object):

    def __init__(self, name, accidental='', octave=4):
        if name not in FREQUENCY_FACTOR.keys():
            raise Exception("Note name doesn't exist")
        self.name = name

        if accidental not in ACCIDENTALS:
            raise Exception("Note accidental doesn't exist")
        self.accidental = accidental

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

    def change_octave(self, octave):
        return Note(self.name, self.accidental, octave)

    def shift_octave(self, offset):
        return change_octave(self.octave + offset)

    def octave_up(self):
        return shift_octave(1)

    def octave_down(self):
        return shift_octave(-1)

    @property
    def frequency(self):
        factor = FREQUENCY_FACTOR[self.name]

        first_octave_C = ZEROTH_OCTAVE_RANGE[0]
        frequency = first_octave_C * factor * 2**self.octave

        if self.accidental == 'b':
            frequency = (frequency * 15) / 16

        if self.accidental == '#':
            frequency = (frequency * 16) / 15

        return round(frequency, 2)

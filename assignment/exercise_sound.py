#!/usr/bin/env python3
"""
PWM Tone Generator - Chatgpt assistance with getting the song to play

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))

# Define the note frequencies in Hz
NOTES = {
    'D6': 1175, 'DS6': 1245, 'E6': 1319, 'F6': 1397, 'FS6': 1480, 'G6': 1568, 'GS6': 1661,
    'A6': 1760, 'AS6': 1865, 'B6': 1976, 'C7': 2093, 'CS7': 2217, 'D7': 2349, 'DS7': 2489, 'E7': 2637, 'F7': 2794, 'FS7': 2960, 'G7': 3136, 'GS7': 3322,
    'A7': 3520, 'AS7': 3729, 'B7': 3951
}

# Define the Mario Theme (first few seconds)
# Each tuple represents (note, duration in seconds)
mario_theme = [
    ('E7', 0.15), ('E7', 0.15), ('E7', 0.15),       # E E E
    ('C7', 0.1), ('E7', 0.15), ('G7', 0.4),         # C E G
    ('G6', 0.4),                                    # G (lower)
    
    ('C7', 0.2), ('G6', 0.2), ('E6', 0.2),          # C G E
    ('A6', 0.2), ('B6', 0.2), ('A#6', 0.2),         # A B A#
    ('A6', 0.15),                                   # A
    
    ('G6', 0.1), ('E7', 0.15), ('G7', 0.15),        # G E G
    ('A7', 0.2), ('F7', 0.2), ('G7', 0.2),          # A F G
    ('E7', 0.15), ('C7', 0.15), ('D7', 0.15),       # E C D
    ('B6', 0.2)                                     # B
]



def playtone(frequency: float, duration: float) -> None:
    if frequency:
        speaker.duty_u16(1000)
        speaker.freq(frequency)
    else:
        speaker.duty_u16(0)  # No sound for rests
    utime.sleep(duration)

def quiet():
    speaker.duty_u16(0)

print("Playing frequency (Hz):")

for note, duration in mario_theme:
    freq = NOTES.get(note, None)
    print(freq)
    playtone(freq, duration)

# Turn off the PWM
quiet()


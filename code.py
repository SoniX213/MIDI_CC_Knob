import time
import board

import usb_midi
import adafruit_midi

from analogio import AnalogIn
from adafruit_midi.control_change import ControlChange

# MIDI CC knob controller example for Seeduino XIAO
# Prerequisites
#
# Requires CircuitPython: https://circuitpython.org/board/seeeduino_xiao/
# Also requires the following CircuitPython libs: adafruit_midi (drop it into the lib folder)
#
# Save this code in code.py on your Seeeduino XIAO CIRCUITPY drive


# Read analog pin voltage
def get_voltage(pin):
    return (pin.value * 3.3) / 65536


# The potentiometers' middle pins are connected to analog pins 0-9 the
# outer pins to GND and 3v3.
knob_1 = AnalogIn(board.A0)
knob_2 = AnalogIn(board.A1)
knob_3 = AnalogIn(board.A2)
knob_4 = AnalogIn(board.A3)
knob_5 = AnalogIn(board.A4)
knob_6 = AnalogIn(board.A5)
knob_7 = AnalogIn(board.A6)
knob_8 = AnalogIn(board.A7)
knob_9 = AnalogIn(board.A8)
knob_10 = AnalogIn(board.A9)

# Set up MIDI
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

# Use these variables to only update when the value changes
last_knob_1_val = 0
last_knob_2_val = 0
last_knob_3_val = 0
last_knob_4_val = 0
last_knob_5_val = 0
last_knob_6_val = 0
last_knob_7_val = 0
last_knob_8_val = 0
last_knob_9_val = 0
last_knob_10_val = 0

while True:
    # Read voltages and convert to 0-127 (MIDI note range)
    knob_1_val = min(max(int(get_voltage(knob_1) / 3.3 * 128), 0), 127)
    knob_2_val = min(max(int(get_voltage(knob_2) / 3.3 * 128), 0), 127)
    knob_3_val = min(max(int(get_voltage(knob_3) / 3.3 * 128), 0), 127)
    knob_4_val = min(max(int(get_voltage(knob_4) / 3.3 * 128), 0), 127)
    knob_5_val = min(max(int(get_voltage(knob_5) / 3.3 * 128), 0), 127)
    knob_6_val = min(max(int(get_voltage(knob_6) / 3.3 * 128), 0), 127)
    knob_7_val = min(max(int(get_voltage(knob_7) / 3.3 * 128), 0), 127)
    knob_8_val = min(max(int(get_voltage(knob_8) / 3.3 * 128), 0), 127)
    knob_9_val = min(max(int(get_voltage(knob_9) / 3.3 * 128), 0), 127)
    knob_10_val = min(max(int(get_voltage(knob_10) / 3.3 * 128), 0), 127)
    

    # If value has changed by more than 2 since last value, send MIDI CC message
    if abs(knob_1_val - last_knob_1_val) > 2:
        midi.send(ControlChange(1, knob_1_val))
        last_knob_1_val = knob_1_val
    if abs(knob_2_val - last_knob_2_val) > 2:
        midi.send(ControlChange(2, knob_2_val))
        last_knob_2_val = knob_2_val
    if abs(knob_2_val - last_knob_2_val) > 2:
        midi.send(ControlChange(3, knob_3_val))
        last_knob_3_val = knob_3_val
    if abs(knob_4_val - last_knob_4_val) > 2:
        midi.send(ControlChange(4, knob_4_val))
        last_knob_4_val = knob_4_val
    if abs(knob_2_val - last_knob_2_val) > 2:
        midi.send(ControlChange(5, knob_5_val))
        last_knob_5_val = knob_5_val
    if abs(knob_6_val - last_knob_6_val) > 2:
        midi.send(ControlChange(6, knob_6_val))
        last_knob_6_val = knob_6_val
    if abs(knob_7_val - last_knob_7_val) > 2:
        midi.send(ControlChange(7, knob_7_val))
        last_knob_7_val = knob_7_val
    if abs(knob_8_val - last_knob_8_val) > 2:
        midi.send(ControlChange(2, knob_2_val))
        last_knob_8_val = knob_8_val
    if abs(knob_8_val - last_knob_8_val) > 2:
        midi.send(ControlChange(8, knob_8_val))
        last_knob_8_val = knob_8_val
    if abs(knob_9_val - last_knob_9_val) > 2:
        midi.send(ControlChange(9, knob_9_val))
        last_knob_9_val = knob_9_val
    if abs(knob_10_val - last_knob_10_val) > 2:
        midi.send(ControlChange(10, knob_10_val))
        last_knob_10_val = knob_10_val
# -*- coding: utf-8 -*-
# Copyright (C) 2023-2025 pawan kumar <pawanpianoartist@gmail.com>
# This file is covered by the GNU General Public License.

# importing required modules
import globalPluginHandler
import tones
import ui
import addonHandler
import config
from globalCommands import GlobalCommands as commands
from scriptHandler import script

# main class
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    # Tracks whether musical mode is enabled
    musicalMode = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Automatically toggle mode when the plugin is initialized
        self.script_toggleMode(None)

    @script(description="Toggle the musical keyboard mode.")
    def script_toggleMode(self, gesture):
        self.musicalMode = not self.musicalMode
        self.script_toggleGestures()
        if self.musicalMode:
            ui.message("Musical keyboard on")
        else:
            ui.message("Musical keyboard off")

    def script_toggleGestures(self):
        """Enable or disable all gesture bindings based on current mode."""
        if self.musicalMode:
            for key in self.__gestures:
                self.bindGesture(key, self.__gestures[key])
        else:
            for key in self.__gestures:
                try:
                    self.removeGestureBinding(key)
                except KeyError:
                    pass
            # Keep the toggle gesture active when mode is off
            self.bindGesture("kb:NVDA+Shift+L", "toggleMode")

    # --- Lower Octave Keys (z to , row) ---
    def script_beepZ(self, gesture): tones.beep(261, 300)     # C
    def script_beepS(self, gesture): tones.beep(277, 300)     # C#
    def script_beepX(self, gesture): tones.beep(293, 300)     # D
    def script_beepD(self, gesture): tones.beep(311, 300)     # D#
    def script_beepC(self, gesture): tones.beep(329, 300)     # E
    def script_beepV(self, gesture): tones.beep(349, 300)     # F
    def script_beepG(self, gesture): tones.beep(370, 300)     # F#
    def script_beepB(self, gesture): tones.beep(392, 300)     # G
    def script_beepH(self, gesture): tones.beep(415, 300)     # G#
    def script_beepN(self, gesture): tones.beep(440, 300)     # A
    def script_beepJ(self, gesture): tones.beep(466, 300)     # A#
    def script_beepM(self, gesture): tones.beep(493, 300)     # B
    def script_beepComma(self, gesture): tones.beep(523, 300) # C (next octave)

    # --- Higher Octave Keys (q to p row and others) ---
    def script_beepQ(self, gesture): tones.beep(523, 300)     # C
    def script_beep2(self, gesture): tones.beep(554, 300)     # C#
    def script_beepW(self, gesture): tones.beep(587, 300)     # D
    def script_beep3(self, gesture): tones.beep(622, 300)     # D#
    def script_beepE(self, gesture): tones.beep(659, 300)     # E
    def script_beepR(self, gesture): tones.beep(698, 300)     # F
    def script_beep5(self, gesture): tones.beep(740, 300)     # F#
    def script_beepT(self, gesture): tones.beep(784, 300)     # G
    def script_beep6(self, gesture): tones.beep(831, 300)     # G#
    def script_beepY(self, gesture): tones.beep(880, 300)     # A
    def script_beep7(self, gesture): tones.beep(932, 300)     # A#
    def script_beepU(self, gesture): tones.beep(987, 300)     # B
    def script_beepI(self, gesture): tones.beep(1046, 300)    # C
    def script_beep9(self, gesture): tones.beep(1108, 300)    # C#
    def script_beepO(self, gesture): tones.beep(1174, 300)    # D
    def script_beep0(self, gesture): tones.beep(1244, 300)    # D#
    def script_beepP(self, gesture): tones.beep(1318, 300)    # E

    # Extra keys for musical notes (l, ;, ., /)
    def script_beep2(self, gesture): tones.beep(554, 300)     # C# (mapped to 'l')
    def script_beepW(self, gesture): tones.beep(587, 300)     # D (mapped to '.')
    def script_beep3(self, gesture): tones.beep(622, 300)     # D# (mapped to ';')
    def script_beepE(self, gesture): tones.beep(659, 300)     # E (mapped to '/')

    # Non-sounding keys to suppress unused or mis-hit keys
    def script_beepNon(self, gesture): return

    # --- Key gesture mappings ---
    __gestures = {
        "kb:NVDA+Shift+L": "toggleMode",

        # Lower octave
        "kb:z": "beepZ",
        "kb:s": "beepS",
        "kb:x": "beepX",
        "kb:d": "beepD",
        "kb:c": "beepC",
        "kb:v": "beepV",
        "kb:g": "beepG",
        "kb:b": "beepB",
        "kb:h": "beepH",
        "kb:n": "beepN",
        "kb:j": "beepJ",
        "kb:m": "beepM",
        "kb:,": "beepComma",

        # Middle keys remapped to higher octave notes
        "kb:l": "beep2",
        "kb:.": "beepW",
        "kb:;": "beep3",
        "kb:/": "beepE",

        # Higher octave
        "kb:q": "beepQ",
        "kb:2": "beep2",
        "kb:w": "beepW",
        "kb:3": "beep3",
        "kb:e": "beepE",
        "kb:r": "beepR",
        "kb:5": "beep5",
        "kb:t": "beepT",
        "kb:6": "beep6",
        "kb:y": "beepY",
        "kb:7": "beep7",
        "kb:u": "beepU",
        "kb:i": "beepI",
        "kb:9": "beep9",
        "kb:o": "beepO",
        "kb:0": "beep0",
        "kb:p": "beepP",
    }

    # Keys that should do nothing (ignored when pressed)
    for key in ["kb:a", "kb:f", "kb:k", "kb:'", "kb:1", "kb:4", "kb:8", "kb:-"]:
        __gestures[key] = "beepNon"

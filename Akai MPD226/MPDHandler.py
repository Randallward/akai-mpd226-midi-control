"""
IMPORTANT:
 All event handling goes in this file.
 Pretty much all of your tweaks and changes can go here.
 https://media0.giphy.com/media/NsIwMll0rhfgpdQlzn/200.gif
"""


import time

import arrangement
import channels
import mixer
import general
import patterns
import playlist
import screen
import transport
import ui

import device
import launchMapPages
import midi
import utils

from classes.MPD226 import MPD226

class MPDHandler(MPD226):

    port = None
    init_time = None
    last_pad_press_time = None
    last_stop_press_time = None
    button_map = 0
    mode_change_unlocked = True

    """
    Initialization
    """
    def set_port_number(self):
        self.port = self.get_port_number()

    def set_init_time(self):
        self.init_time = self.get_timestamp()

    """
    External accessors
    """

    def get_port_number(self):
        return  device.getPortNumber()

    def get_timestamp(self):
        return time.perf_counter()

    """
    Utility methods
    """

    def check_buffer(self, button, time_pressed):
        if button.type == 'transport' and self.last_stop_press_time:
            return time_pressed - self.last_stop_press_time > self.STOP_BUFFER
        elif button.type == 'pad' and self.last_pad_press_time:
            return time_pressed - self.last_pad_press_time > self.PAD_BUFFER
        else:
            print(f"{button.type.upper()} {button.number} has no associated buffer.")

    def change_button_mapping(self, map=1):
        """ Update the global button mapping mode id. """
        if isinstance(map, str):
            if map in self.INPUT_MODES: map = self.INPUT_MODES.index(map)
        self.button_map = (self.button_map + map) % len(self.INPUT_MODES)

    def check_for_remap(self, pad):
        """ Change the button mapping if certain conditions are met. """
        if self.mode_change_unlocked:
            if self.pad_13.held and self.pad_16.held:
                if pad  == self.pad_1:
                    self.change_button_mapping(-1)
                elif pad == self.pad_4:
                    self.change_button_mapping(1)

    """
    Input handlers
    """

    def handle_pad_press(self, event, pad):
        """
        Put pad press code here.
        """
        print(f"Pressed pad {pad.number}.")

        self.check_for_remap(pad)
        print(self.button_map)

        event.handled = True

    def handle_pad_release(self, event, pad):
        """
        Put pad release code here.
        """
        # print(f"Released pad {pad.number}.")

        event.handled = True

    def handle_pad_pressure_change(self, event, pad, value):
        """
        Put pad pressure change code here.
        """
        # print(f"Changed pad {pad.number} pressure to {value}.")

        event.handled = True

    def handle_knob_change(self, event, knob, value):
        """
        Put knob change code here.
        """
        print(f"Changed knob {knob.number} to {value}.")

        event.handled = True

    def handle_slider_change(self, event, slider, value):
        """
        Put slider change code here.
        """
        print(f"Changed slider {slider.number} to {value}.")

        event.handled = True

    def handle_switch_press(self, event, switch):
        """
        Put switch press code here.
        """
        print(f"Pressed switch {switch.number}.")

        event.handled = True

    def handle_stop_press(self, event, stop):
        """
        Put stop press code here.
        """
        print(f"Pressed stop button.")

        event.handled = True

    def handle_play_press(self, event, play):
        """
        Put play press code here.
        """
        print(f"Pressed play button.")

        event.handled = True

    def handle_rec_press(self, event, rec):
        """
        Put rec press code here.
        """
        print(f"Pressed rec button.")

        event.handled = True
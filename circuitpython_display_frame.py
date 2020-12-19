# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2020 Tim C
#
# SPDX-License-Identifier: MIT
"""
`circuitpython_display_frame`
================================================================================

CircuitPython displayio widget to create a rounded rectangle frame with text label at the top center.


* Author(s): Tim C

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

* Adafruit CircuitPython Display Text:
  https://github.com/adafruit/Adafruit_CircuitPython_Display_Text
  
* Adafruit CircuitPython Display Shapes:
  https://github.com/adafruit/Adafruit_CircuitPython_Display_Shapes

"""

# imports

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/foamyguy/Circuitpython_CircuitPython_Display_Frame.git"

import displayio
import terminalio
from adafruit_display_text import bitmap_label
from adafruit_display_shapes.roundrect import RoundRect

class Frame(displayio.Group):
    
    
    def __init__(
        self,
        width,
        height,
        x,
        y,
        corner_radius=10,
        text="Frame",
        font=terminalio.FONT,
        outline=0xFFFFFF,
        text_color=None,
        stroke=2
    ):
        super().__init__(x=x, y=y)
        
        roundrect = RoundRect(0, 0, width, height, corner_radius, fill=None, outline=outline, stroke=stroke)
        self.append(roundrect)
        
        if outline and not text_color:
            text_color = outline
        
        self.label = bitmap_label.Label(font, text=text, color=text_color, background_color=0x0, padding_left=2, padding_right=1)
        self.label.anchor_point = (0.5, 0.5)
        self.label.anchored_position = (width//2, 0)
        if self.label.bounding_box[2] * 2 < width - (corner_radius*2):
            self.label.scale = 2
        self.append(self.label)


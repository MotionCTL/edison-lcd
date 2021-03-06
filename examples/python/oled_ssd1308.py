#!/usr/bin/python
# Author: Zion Orent <zorent@ics.com>
# Copyright (c) 2015 Intel Corporation.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Load i2clcd display module
import time, signal, sys
import pyupm_i2clcd as upmLCD

myLCD = upmLCD.SSD1308(6, 0x3C);

logoArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 128, 128, 128, 192, 192, 192, 224,
224, 224, 224, 240, 240, 248, 248, 120, 120, 120, 120, 60, 60, 60, 60, 60,
62, 30, 30, 30, 30, 30, 30, 30, 31, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 31, 31, 31, 31, 31,
30, 62, 62, 62, 62, 126, 126, 124, 124, 252, 252, 248, 248, 240, 240, 240,
224, 224, 224, 192, 128, 128, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 128, 128, 128, 128, 128, 128,
128, 0, 56, 56, 28, 30, 14, 15, 15, 7, 7, 7, 7, 3, 3, 1, 1, 1, 1, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
192, 192, 192, 192, 192, 192, 192, 192, 0, 0, 0, 0, 192, 193, 195, 195,
195, 7, 15, 15, 63, 127, 255, 255, 255, 254, 252, 252, 240, 192, 0, 0, 0,
0, 0, 0, 0, 0, 128, 192, 192, 240, 248, 124, 124, 60, 0, 0, 0, 0, 159, 159,
159, 159, 159, 159, 159, 159, 0, 0, 0, 0, 128, 128, 128, 128, 128, 128,
128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 0, 0,
0, 0, 0, 0, 254, 254, 254, 254, 254, 254, 254, 254, 128, 128, 128, 128,
128, 0, 0, 0, 0, 0, 0, 0, 128, 128, 128, 192, 192, 192, 192, 192, 192, 128,
128, 128, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255,
0, 0, 0, 0, 3, 7, 3, 3, 3, 0, 0, 0, 0, 0, 1, 1, 255, 255, 255, 255, 255,
255, 255, 0, 0, 224, 248, 252, 252, 255, 127, 15, 15, 3, 1, 0, 0, 0, 0, 0,
0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 255, 255, 255,
255, 255, 255, 255, 255, 15, 15, 15, 15, 15, 15, 255, 255, 255, 255, 255,
255, 255, 252, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 15, 15,
15, 15, 15, 224, 224, 252, 254, 255, 255, 255, 255, 159, 159, 143, 143,
135, 135, 143, 159, 255, 255, 255, 255, 255, 255, 252, 248, 0, 0, 0, 255,
255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128,
224, 248, 248, 255, 255, 255, 255, 255, 127, 15, 255, 255, 255, 255, 255,
255, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255,
255, 255, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0,
0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 255, 255, 255,
255, 255, 255, 255, 255, 192, 192, 192, 192, 192, 31, 31, 255, 255, 255,
255, 255, 255, 231, 231, 199, 199, 199, 199, 199, 199, 199, 199, 231, 231,
231, 231, 199, 135, 0, 0, 0, 63, 255, 255, 255, 255, 255, 255, 255, 0, 0,
0, 0, 224, 240, 248, 248, 252, 254, 255, 255, 255, 127, 63, 63, 31, 15, 7,
7, 1, 0, 0, 63, 63, 255, 255, 255, 255, 255, 240, 192, 192, 128, 0, 0, 0,
0, 0, 0, 0, 0, 1, 3, 3, 7, 7, 7, 7, 7, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7,
0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 3, 3, 7, 7, 7,
7, 7, 7, 7, 7, 7, 0, 0, 0, 1, 3, 3, 3, 7, 7, 7, 7, 15, 15, 15, 15, 7, 7, 7,
7, 7, 3, 3, 3, 1, 0, 0, 0, 0, 1, 3, 3, 7, 135, 135, 135, 192, 192, 0, 0, 7,
7, 3, 3, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 7, 15, 15,
31, 127, 127, 127, 255, 255, 252, 252, 252, 248, 240, 240, 240, 224, 224,
224, 192, 192, 192, 192, 128, 128, 128, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 128, 128, 128, 128, 128, 128, 128, 192, 192, 192, 192, 192,
224, 224, 224, 224, 240, 240, 240, 240, 248, 248, 248, 248, 252, 252, 252,
254, 254, 255, 255, 255, 255, 255, 255, 127, 127, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
3, 3, 3, 7, 7, 7, 15, 15, 31, 31, 31, 63, 63, 63, 63, 63, 127, 127, 127,
127, 127, 255, 255, 255, 255, 254, 254, 254, 254, 254, 254, 254, 254, 254,
254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254,
255, 255, 255, 255, 255, 255, 255, 127, 127, 127, 127, 127, 127, 127, 127,
63, 63, 63, 63, 63, 31, 31, 31, 31, 31, 15, 15, 15, 15, 7, 7, 7, 7, 3, 3,
3, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0]

intelLogo = upmLCD.uint8Array(len(logoArr))

for x in range(len(logoArr)):
	intelLogo.__setitem__(x, logoArr[x])
myLCD.clear()
myLCD.draw(intelLogo, 1024)

del intelLogo
del myLCD
print "Exiting"

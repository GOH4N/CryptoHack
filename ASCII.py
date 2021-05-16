#!/usr/bin/env python3

import telnetlib
import json

asciiValues = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

characters = [chr(ascii) for ascii in asciiValues]

print(''.join(characters))

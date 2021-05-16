#!/usr/bin/env python3
import Cryptodome
from Cryptodome.Util.number import bytes_to_long
from Cryptodome.Util.number import long_to_bytes

# Python's PyCryptodome library implements this with the methods:
# Crypto.Util.number.bytes_to_long
# Crypto.Util.number.long_to_bytes.

# characters to convert back into a message (seems base10)
long = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
bytes = long_to_bytes(long)
print(bytes)

"""Calculates the 'CRC' checksum needed as the last bit in data transmission. 

The checksum needed is like a CRC-8 checksum. I could not get the other checksum
libraries to work so this is a one-off module for calculating the checksum.

Credit to http://www.hifi-remote.com/forums/viewtopic.php?t=14541 for guidance in the CRC implementation.
"""

# Module imports

# Constants
CRC_8_GENERATOR_POLYNOMIAL = 0x8C

# Checksum
def crc(data):
    """Calculates the 'CRC' checksum value needed as the last bit in data transmission"""
    # Variable to hold the output checksum
    checksum_value = 0
    
    # Iterate the data
    for item in data:
        checksum_value ^= item 
        for x in range(1,9):
            if (checksum_value & 1):
                checksum_value = (checksum_value >> 1) ^ CRC_8_GENERATOR_POLYNOMIAL
            else:
                checksum_value = (checksum_value >> 1)
    return checksum_value

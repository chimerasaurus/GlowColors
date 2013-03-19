# Module imports

# Constants
CRC_8_GENERATOR_POLYNOMIAL = 0x8C

# Checksum
def checksum(data):
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


values = [0x90, 0x60]
print checksum(values)
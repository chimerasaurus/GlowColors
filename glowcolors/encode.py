"""Encodes a GWtS message in the IR protocol for transmittal to a pair of ears via infared.

Implements the protocol necessary to convert a message of data in the IR protocol used by the GWtS ears.
This protocol is based on a 2400 baud UART transmission scheme.
"""

# Module imports
import settings

# Constants
MESSAGE_BIT_WIDTH = settings.IR['WIDTH']

def ir_encode(message, absolute_values=False):
    """Encodes the given message in the IR protocol for transmission; optional boolean to return absolute timings"""
    # Variable to hold the encoded message
    encoded_message = []
    
    # Save the padding for message width
    
    # Iterate the message
    true_time = 0
    
    for item in message:
        for bit in range(0,10):
            # Variable to hold the timing for this bit
            time = 0
            
            # Determine the timing based on the bit
            if (bit == 0):
                time = MESSAGE_BIT_WIDTH
            elif (bit == 9):
                time = (MESSAGE_BIT_WIDTH * -1)
            else:
                if (item & (1 << (bit - 1))):
                    time = (MESSAGE_BIT_WIDTH * -1)
                else:
                    time = MESSAGE_BIT_WIDTH
            
            if (time < 0):
                if (true_time <= 0):
                    true_time += time
                else:
                    encoded_message.append(true_time)
                    true_time = time
            else:
                if (true_time >= 0):
                    true_time += time
                else:
                    encoded_message.append(true_time)
                    true_time = time
    
    encoded_message.append(true_time)
            
    # Return the encoded message
    if (absolute_values == True):
        abs_values = [abs(encoded_message[n]) for n in range(0,len(encoded_message))]
        return abs_values
    else:
        return encoded_message
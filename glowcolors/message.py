"""Represents a message of data using the GWtS protocol.

Implements what is known about the GWtS protocol to construct a message of data which can be sent to a
device to change its state.
"""

# Module imports
import glowcolors.checksum
import glowcolors.settings

# Constants
# NONE

def generate(color, ear='BOTH', message_type='SHOW'):
    """Create a new message with the specified color for the (optional) ear of the (optional) given type."""
    
    # Uppercase arguments
    color = color.upper()
    ear = ear.upper()
    message_type = message_type.upper()
    
    # Check argument for color is valid
    if glowcolors.settings.COLORS['BOTH'].has_key(color) == False:
        raise ValueError("color does not have a value")

    # Check that the ear is valid
    if (ear != 'BOTH' and ear != 'RIGHT'):
        raise ValueError("ear has an improper value")
        
    # Check that the type is valid
    if (message_type != 'SHOW' and message_type != 'SYSTEM'):
        raise ValueError("message type has an improper value")
        
    # Generate the message
    message_data = []
    
    # Add the given data
    message_data.append(glowcolors.settings.PREFIXES[message_type])
    message_data.append(glowcolors.settings.COLORS[ear][color])
    
    # Add the CRC
    message_data.append(glowcolors.checksum.crc(message_data))
    
    return message_data
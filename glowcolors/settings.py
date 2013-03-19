"""Settings file with protocol-specific settings and variables.

This module holds the settings needed to construct messages based on the GWtS protocol.
"""

# Module imports
# NONE

# Constants
PREFIXES = {
    'SHOW': 0x90,
    'SYSTEM': 0x55,
}

COLORS = {
    'BOTH': {
        'INACTIVE': 0x60,
        'BLUE': 0x61,
        'GREEN': 0x62,
        'CYAN': 0x63,
        'RED': 0x64,
        'MAGENTA': 0x65,
        'YELLOW': 0x66,
        'WHITE': 0x67,
    },
    'RIGHT': {
        'INACTIVE': 0x68,
        'BLUE': 0x69,
        'GREEN': 0x6A,
        'CYAN': 0x6B,
        'RED': 0x6C,
        'MAGENTA': 0x6D,
        'YELLOW': 0x6E,
        'WHITE': 0x6F,
    },
}
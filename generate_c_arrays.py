"""Generates color arrays for use in a C project.

This scipt generates a dump of array/color data for use in a A project. This simplifies the need
to hand-create and edit the data in many projects. This is useful, for instance, with Arduino projects.
"""

# Module imports
import glowcolors.encode
import glowcolors.message
import glowcolors.settings

# Constants
## NONE

# Functions
def main():
    print "--> Generating arrays fror Arduino use <--\n"

    # Generare both color arrays
    generate_color_arrays('BOTH')
    
    # Generate right color arrays
    generate_color_arrays('RIGHT')
    
# Translate a python array into a string for Arduino
def array_to_string(array):
    array_string = ','.join(str(x) for x in array)
    return '{' + array_string + '}'

# Generate arrays for a given side
def generate_color_arrays(side):
    # Array to hold encoded data
    encoded_data = []
    
    for color in glowcolors.settings.COLORS[side]:
        message = glowcolors.message.generate(color)
        encoded_data = glowcolors.encode.ir_encode(message, True)
        print "int %s_%s[%s] = %s" % (side, color, len(encoded_data), array_to_string(encoded_data))
    
# Helpers
## Run the main() function on execution
if __name__ == "__main__":
    main()
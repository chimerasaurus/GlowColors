#GlowColors#

The **GlowColors** package creates well-formatted messages for interacting with fashionable headwear. This package implements what is known about the *Glow Color Protocol* and the capabilities of receiving headwear.

The data generated by **GlowColors** can be transmitted via UART/IRDA SIR at 2400 baud.

##Usage##

There are two important modules in this package:

* The `message` module is used for creating the raw state-changing message
* The `encode` module takes message data and encodes it for transmission via infrared

The other modules support the operation of these two classes.

###Creating a message###
Messages are created with the `message` module. For example, this creates a message to change *both* antennae to *red*.

`message_data = glowcolors.message.generate('red', 'BOTH', 'SHOW')`

The data returned (`message_data`) from the message module is an array of values which will instruct a node to change states. This message needs to be encoded for IR transmission.

`ir_data = glowcolors.ir_encode(message)`

The data rerurned (`ir_data`) from encode will be an array of IR times in microseconds. The widths correspond to IR pulses sent to the headwear to change its state.

##Credits##
This work is based on contributions from users in the following forum threads.

* [hifi-remote](http://www.hifi-remote.com/forums/viewtopic.php?t=14541)
* [Do It Yourself Christmas](http://doityourselfchristmas.com/forums/showthread.php?20818-Ear-to-Ear-Networking)

##Legal information##
All original work, intellectual property, and copyrights are property of their respective holders.

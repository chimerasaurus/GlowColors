import glowcolors.checksum
import unittest

class TestChecksum(unittest.TestCase):
    """Tests the Checksum module of the glowcolors package"""

    def setUp(self):
        """Sets up the unit tests"""
        # Values to test with the CRC function
        self.values = {166: [0x90, 0x60], 231: [0x90, 0x6F]}
        
    def test_crc(self):
        """Testing the crc function of the checksum module"""
        for k,v in self.values.iteritems():
            crc_8 = glowcolors.checksum.crc(v)
            self.assertEqual(crc_8, k)
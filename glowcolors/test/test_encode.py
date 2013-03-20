# Imports needed for this unit test
import glowcolors.encode
import unittest

class TestSettings(unittest.TestCase):
    """Tests the settings module of the glowcolors package"""

    def setUp(self):
        """Sets up the unit tests"""
        self.unencoded_off_message_both_ears = [144,96,166]
        self.encoded_off_message_both_ears = [2085, -417, 834, -834, 2502, -834, 417, -417, 834, -834, 834, -417, 417, -834]
        
    def test_encode_both_ears_off_messahe(self):
        """Testing encode of off message for both ears"""
        self.assertEqual(glowcolors.encode.ir_encode(self.unencoded_off_message_both_ears), self.encoded_off_message_both_ears)
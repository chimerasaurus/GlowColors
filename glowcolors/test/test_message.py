# Imports needed for this unit test
import glowcolors.message
import unittest

class TestMessage(unittest.TestCase):
    """Tests the message module of the glowcolors package"""

    def setUp(self):
        """Sets up the unit tests"""
        self.inactive_message = [144,96,166]
        
    def test_generate_no_color_error(self):
        """Testing the message will not accept no color"""
        self.assertRaises(ValueError, glowcolors.message.generate, '')
        
    def test_generate_requires_one_argument(self):
        """Testing the message will not accept zero arguments"""
        self.assertRaises(TypeError, glowcolors.message.generate)
        
    def test_generate_requires_one_argument(self):
        """Testing the message will not accept invalid colors"""
        self.assertRaises(ValueError, glowcolors.message.generate, 'pink')
        
    def test_generate_well_formatted_short_message(self):
        """Testing the creation of a short message with only the color"""
        self.assertEqual(glowcolors.message.generate('INACTIVE'), self.inactive_message)
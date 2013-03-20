# Imports needed for this unit test
import glowcolors.settings
import unittest

class TestSettings(unittest.TestCase):
    """Tests the settings module of the glowcolors package"""

    def setUp(self):
        """Sets up the unit tests"""
        self.prefixes = glowcolors.settings.PREFIXES
        self.colors = glowcolors.settings.COLORS
        self.ir = glowcolors.settings.IR
        
    def test_prefix_count(self):
        """Testing the number of prefixes for GWtS messages"""
        self.assertEqual(len(self.prefixes), 2)
        
    def test_prefix_length(self):
        """Testing the prefixes are greater than one"""
        for k,v in self.prefixes.iteritems():
            self.assertTrue(v > 1)
    
    def test_two_color_sets_exist(self):
        """Testing two color sets exist"""
        self.assertEqual(len(self.colors), 2)
        
    def test_pair_color_set_complete(self):
        """Testing paired color set has eight elements"""
        self.assertEqual(len(self.colors['BOTH']), 8)
        
    def test_right_color_set_complete(self):
        """Testing paired color set has eight elements"""
        self.assertEqual(len(self.colors['RIGHT']), 8)
        
    # Test the IR settings
    def test_ir_padding_set(self):
        """Testing ir padding is not null"""
        self.assertTrue(self.ir['WIDTH'] > 0)
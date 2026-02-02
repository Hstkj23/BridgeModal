# test_bridgemodal.py
"""
Tests for BridgeModal module.
"""

import unittest
from bridgemodal import BridgeModal

class TestBridgeModal(unittest.TestCase):
    """Test cases for BridgeModal class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BridgeModal()
        self.assertIsInstance(instance, BridgeModal)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BridgeModal()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

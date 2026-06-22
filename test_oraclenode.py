# test_oraclenode.py
"""
Tests for OracleNode module.
"""

import unittest
from oraclenode import OracleNode

class TestOracleNode(unittest.TestCase):
    """Test cases for OracleNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OracleNode()
        self.assertIsInstance(instance, OracleNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OracleNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

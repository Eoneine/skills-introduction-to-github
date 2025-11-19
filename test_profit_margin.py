"""
Unit tests for the profit margin calculator module.

This module contains comprehensive tests for the calculate_profit_margin function,
including normal cases, edge cases, and error conditions.
"""

import unittest
from profit_margin import calculate_profit_margin


class TestProfitMarginCalculator(unittest.TestCase):
    """Test cases for the profit margin calculator."""
    
    def test_basic_profit_margin(self):
        """Test basic profit margin calculation."""
        result = calculate_profit_margin(1000, 600)
        self.assertEqual(result, 40.0)
    
    def test_high_profit_margin(self):
        """Test calculation with high profit margin."""
        result = calculate_profit_margin(1000, 100)
        self.assertEqual(result, 90.0)
    
    def test_low_profit_margin(self):
        """Test calculation with low profit margin."""
        result = calculate_profit_margin(1000, 950)
        self.assertEqual(result, 5.0)
    
    def test_break_even(self):
        """Test break-even scenario where cost equals revenue."""
        result = calculate_profit_margin(1000, 1000)
        self.assertEqual(result, 0.0)
    
    def test_decimal_values(self):
        """Test with decimal values."""
        result = calculate_profit_margin(1234.56, 789.01)
        expected = ((1234.56 - 789.01) / 1234.56) * 100
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_small_values(self):
        """Test with small values."""
        result = calculate_profit_margin(10, 5)
        self.assertEqual(result, 50.0)
    
    def test_large_values(self):
        """Test with large values."""
        result = calculate_profit_margin(1000000, 750000)
        self.assertEqual(result, 25.0)
    
    def test_zero_cost(self):
        """Test with zero cost (100% profit margin)."""
        result = calculate_profit_margin(1000, 0)
        self.assertEqual(result, 100.0)
    
    def test_zero_revenue_error(self):
        """Test that zero revenue raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate_profit_margin(0, 100)
        self.assertIn("Revenue must be positive", str(context.exception))
    
    def test_negative_revenue_error(self):
        """Test that negative revenue raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate_profit_margin(-1000, 500)
        self.assertIn("Revenue must be positive", str(context.exception))
    
    def test_negative_cost_error(self):
        """Test that negative cost raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate_profit_margin(1000, -500)
        self.assertIn("Cost cannot be negative", str(context.exception))
    
    def test_cost_exceeds_revenue_error(self):
        """Test that cost exceeding revenue raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate_profit_margin(1000, 1500)
        self.assertIn("Cost cannot exceed revenue", str(context.exception))
    
    def test_float_precision(self):
        """Test that calculation maintains float precision."""
        result = calculate_profit_margin(333.33, 166.67)
        expected = ((333.33 - 166.67) / 333.33) * 100
        self.assertAlmostEqual(result, expected, places=10)
    
    def test_typical_business_scenarios(self):
        """Test typical business profit margin scenarios."""
        # Retail (typically 20-40%)
        retail_margin = calculate_profit_margin(100, 70)
        self.assertEqual(retail_margin, 30.0)
        
        # Software (typically 70-90%)
        software_margin = calculate_profit_margin(100, 20)
        self.assertEqual(software_margin, 80.0)
        
        # Grocery (typically 1-3%)
        grocery_margin = calculate_profit_margin(100, 98)
        self.assertEqual(grocery_margin, 2.0)


if __name__ == "__main__":
    unittest.main()

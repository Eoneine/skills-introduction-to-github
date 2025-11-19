"""
Profit Margin Calculator Module

This module provides a mathematical function to calculate profit margin.
Profit margin is a key financial metric that shows the percentage of revenue
that remains as profit after deducting costs.

Formula: Profit Margin = ((Revenue - Cost) / Revenue) × 100
"""


def calculate_profit_margin(revenue, cost):
    """
    Calculate the profit margin as a percentage.
    
    The profit margin represents the percentage of revenue that becomes profit
    after subtracting all costs. A higher profit margin indicates better
    profitability.
    
    Args:
        revenue (float): The total revenue or sales amount (must be positive)
        cost (float): The total cost of goods/services sold (must be non-negative)
    
    Returns:
        float: The profit margin as a percentage
    
    Raises:
        ValueError: If revenue is zero or negative, or if cost is negative,
                   or if cost exceeds revenue
    
    Examples:
        >>> calculate_profit_margin(1000, 600)
        40.0
        
        >>> calculate_profit_margin(500, 300)
        40.0
        
        >>> calculate_profit_margin(1000, 1000)
        0.0
    """
    # Validate inputs
    if revenue <= 0:
        raise ValueError("Revenue must be positive and greater than zero")
    
    if cost < 0:
        raise ValueError("Cost cannot be negative")
    
    if cost > revenue:
        raise ValueError("Cost cannot exceed revenue")
    
    # Calculate profit margin
    profit = revenue - cost
    profit_margin = (profit / revenue) * 100
    
    return profit_margin


if __name__ == "__main__":
    # Example usage
    print("Profit Margin Calculator")
    print("=" * 50)
    
    # Example 1: Basic calculation
    revenue1 = 1000
    cost1 = 600
    margin1 = calculate_profit_margin(revenue1, cost1)
    print(f"Revenue: ${revenue1}, Cost: ${cost1}")
    print(f"Profit Margin: {margin1:.2f}%")
    print()
    
    # Example 2: Higher margin
    revenue2 = 5000
    cost2 = 2000
    margin2 = calculate_profit_margin(revenue2, cost2)
    print(f"Revenue: ${revenue2}, Cost: ${cost2}")
    print(f"Profit Margin: {margin2:.2f}%")
    print()
    
    # Example 3: Break-even
    revenue3 = 800
    cost3 = 800
    margin3 = calculate_profit_margin(revenue3, cost3)
    print(f"Revenue: ${revenue3}, Cost: ${cost3}")
    print(f"Profit Margin: {margin3:.2f}%")

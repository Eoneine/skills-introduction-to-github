# Profit Margin Calculator

A simple Python module to calculate profit margin - a key financial metric that indicates the profitability of a business or product.

## What is Profit Margin?

Profit margin is a financial ratio that measures the percentage of revenue that remains as profit after deducting costs. It's one of the most important metrics for assessing business profitability.

## Formula

```
Profit Margin = ((Revenue - Cost) / Revenue) × 100
```

Where:
- **Revenue** = Total sales or income
- **Cost** = Total expenses or cost of goods sold
- **Result** = Percentage representing profit margin

## Usage

### Basic Example

```python
from profit_margin import calculate_profit_margin

# Calculate profit margin
revenue = 1000  # $1000 in sales
cost = 600      # $600 in costs
margin = calculate_profit_margin(revenue, cost)

print(f"Profit Margin: {margin}%")  # Output: Profit Margin: 40.0%
```

### More Examples

```python
# High profit margin (software/SaaS business)
margin = calculate_profit_margin(1000, 200)
# Returns: 80.0%

# Low profit margin (retail/grocery)
margin = calculate_profit_margin(1000, 950)
# Returns: 5.0%

# Break-even scenario
margin = calculate_profit_margin(1000, 1000)
# Returns: 0.0%

# Maximum profit margin (no costs)
margin = calculate_profit_margin(1000, 0)
# Returns: 100.0%
```

## Function Signature

```python
def calculate_profit_margin(revenue, cost):
    """
    Calculate the profit margin as a percentage.
    
    Args:
        revenue (float): The total revenue or sales amount (must be positive)
        cost (float): The total cost of goods/services sold (must be non-negative)
    
    Returns:
        float: The profit margin as a percentage
    
    Raises:
        ValueError: If revenue is zero or negative, or if cost is negative,
                   or if cost exceeds revenue
    """
```

## Error Handling

The function validates input and raises `ValueError` for invalid cases:

- **Zero or negative revenue**: Revenue must be positive
- **Negative cost**: Cost cannot be negative
- **Cost exceeds revenue**: This would result in a loss (negative profit margin)

```python
# This will raise ValueError
calculate_profit_margin(0, 100)      # Zero revenue
calculate_profit_margin(-100, 50)    # Negative revenue
calculate_profit_margin(100, -50)    # Negative cost
calculate_profit_margin(100, 150)    # Cost exceeds revenue
```

## Running the Module

You can run the module directly to see example calculations:

```bash
python3 profit_margin.py
```

## Running Tests

The module includes comprehensive unit tests:

```bash
python3 -m unittest test_profit_margin -v
```

## Interpreting Profit Margins

Different industries have different typical profit margins:

- **Software/SaaS**: 70-90%
- **Financial Services**: 20-30%
- **Retail**: 20-40%
- **Food Services**: 10-15%
- **Grocery Stores**: 1-3%

A higher profit margin generally indicates:
- Better pricing power
- Lower costs relative to revenue
- Higher business efficiency
- More competitive advantage

## Real-World Applications

- **Business Analysis**: Evaluate company profitability
- **Pricing Strategy**: Determine optimal pricing for products
- **Competitive Analysis**: Compare margins across competitors
- **Financial Planning**: Project future profitability
- **Investment Decisions**: Assess investment opportunities

## License

MIT License - See LICENSE file for details

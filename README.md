# Greedy Yogurt Algorithm

A Python project that uses greedy algorithms to optimize yogurt selection based on probiotic content and calorie constraints.

## Overview

This project implements two greedy algorithm approaches for selecting yogurt combinations:

1. **Standard Greedy Algorithm** - Allocates a maximum calorie budget using different optimization strategies
2. **Goal-First Greedy Algorithm** - Selects yogurts until reaching a target probiotic value

## Features

- Multiple greedy strategies (by value, by cost, by density)
- Support for per-food selection limits
- Calorie budget constraints
- CSV data logging with timestamps
- Probiotic tracking in billions of CFU
- **Macronutrient tracking** (protein, sugar, fat)

## Project Structure

```
greedy/
├── def testGreedys(foods, maxUnits):.py.py    # Main greedy algorithm implementation
├── goal first/
│   └── goal-first.py                           # Goal-first greedy approach
├── save_results.py                             # CSV saving utilities
├── yogurt_results.csv                          # Results log with timestamps
└── README.md                                   # This file
```

## Files

### `def testGreedys(foods, maxUnits):.py.py`
Main script containing:
- **Food class** - Represents each yogurt item with value and calorie information
- **buildMenu()** - Creates Food objects from lists
- **testGreedy()** - Applies greedy algorithm with different key functions
- **testGreedys()** - Runs all three strategies and optionally saves to CSV
- **printResult()** - Displays selected items and totals

#### Greedy Strategies:
- **By Value** - Prioritizes highest probiotic content per serving
- **By Cost** - Favors items with lowest calories
- **By Density** - Maximizes probiotic value per calorie

### `goal first/goal-first.py`
Goal-first greedy algorithm with:
- Target-based selection (stops when reaching probiotic goal)
- Per-item serving limits
- Optional calorie and total serving constraints
- Better for reaching specific nutritional targets

### `save_results.py`
Utility functions to save algorithm results:
- `saveResultsToCSV()` - Logs standard greedy results
- `saveGoalResultsToCSV()` - Logs goal-first results
- Automatic timestamp generation (YYYY-MM-DD HH:MM:SS)

### `yogurt_results.csv`
CSV log file tracking:
- Date/Time created
- Strategy used
- Selected yogurt items
- Item count
- Total calories consumed
- Total probiotic value achieved
- **Total protein, sugar, and fat consumed**

## Usage

### Run Standard Greedy Algorithm

```python
python3 "def testGreedys(foods, maxUnits):.py.py"
```

This will:
1. Run all three greedy strategies (value, cost, density)
2. Display selected items for each strategy
3. Save results to `yogurt_results.csv` with timestamp

### Customize Data

Edit the test section at the bottom of `def testGreedys(foods, maxUnits):.py.py`:

```python
if __name__ == '__main__':
    names = ['yogurt strawberry', 'yogurt vanilla', 'yogurt blueberry', 'yogurt greek', 'yogurt honey', 'yogurt vanilla']
    values = [3, 3, 3, 3, 3, 3]  # probiotic score in billions
    calories = [90, 90, 90, 90, 90, 90]
    proteins = [8, 10, 9, 15, 7, 10]  # grams of protein
    sugars = [12, 14, 11, 5, 16, 14]  # grams of sugar
    fats = [2, 3, 2, 1, 1, 3]  # grams of fat
    foods = buildMenu(names, values, calories, proteins, sugars, fats)
    testGreedys(foods, 750, saveToCSV=True)
```

**Editable parameters:**
- `names` - List of food item names
- `values` - Probiotic score (in billions CFU)
- `calories` - Calories per serving
- `proteins` - Grams of protein per serving
- `sugars` - Grams of sugar per serving
- `fats` - Grams of fat per serving
- `750` - Calorie budget (change to any number)
- `saveToCSV=True` - Set to `False` to disable CSV logging

### Use Goal-First Algorithm

```python
from goal_first import goalFirstGreedy, printGoalResult

foods = buildMenu(names, values, calories)
foodList, cals, value, servings, reached, counts = goalFirstGreedy(
    foods, 
    targetValue=15,  # Target 15 billion probiotics
    maxCalories=750
)
printGoalResult(foodList, cals, value, servings, reached, counts, 15)
```

## Example Output

```
Use greedy by value to allocate 750 calories
Selected foods:
  yogurt greek: value=3, calories=90, protein=15g, sugar=5g, fat=1g
  yogurt blueberry: value=3, calories=90, protein=9g, sugar=11g, fat=2g
  yogurt vanilla: value=3, calories=90, protein=10g, sugar=14g, fat=3g
  yogurt honey: value=3, calories=90, protein=7g, sugar=16g, fat=1g
  yogurt strawberry: value=3, calories=90, protein=8g, sugar=12g, fat=2g
  yogurt vanilla: value=3, calories=90, protein=10g, sugar=14g, fat=3g
Total calories: 540.0
Total value: 18.0
Total protein: 59.0g
Total sugar: 72.0g
Total fat: 12.0g
Results saved to yogurt_results.csv
```

## CSV Log Format

| Date Created | Strategy | Food Items | Item Count | Total Calories | Total Value | Total Protein (g) | Total Sugar (g) | Total Fat (g) |
|---|---|---|---|---|---|---|---|---|
| 2026-01-22 14:47:45 | by value | yogurt strawberry, yogurt vanilla, ... | 6 | 540.0 | 18.0 | 59.0 | 72.0 | 12.0 |

## Requirements

- Python 3.6+
- Standard library only (csv, os, datetime)

## Future Enhancements

- Database integration instead of CSV
- Web interface for easy configuration
- Comparison of algorithm efficiency
- Cost tracking (price per item)

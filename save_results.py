import csv
import os
from datetime import datetime


def saveResultsToCSV(foodList, totalCals, totalValue, totalProtein, totalSugar, totalFat, 
                     strategy, filename='yogurt_results.csv'):
    """
    Save greedy algorithm results to a CSV file with timestamp and macronutrients.
    
    Args:
        foodList: List of Food objects selected
        totalCals: Total calories used
        totalValue: Total value achieved
        totalProtein: Total protein in grams
        totalSugar: Total sugar in grams
        totalFat: Total fat in grams
        strategy: Name of the greedy strategy used (e.g., 'value', 'cost', 'density')
        filename: CSV filename to save to
    """
    
    # Create CSV file if it doesn't exist with headers
    file_exists = os.path.isfile(filename)
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Date Created', 'Strategy', 'Food Items', 'Item Count', 'Total Calories', 
                     'Total Value', 'Total Protein (g)', 'Total Sugar (g)', 'Total Fat (g)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header if file is new
        if not file_exists:
            writer.writeheader()
        
        # Format food items as string
        food_items = ', '.join([f"{food.name}" for food in foodList])
        
        # Write data row
        writer.writerow({
            'Date Created': timestamp,
            'Strategy': strategy,
            'Food Items': food_items,
            'Item Count': len(foodList),
            'Total Calories': totalCals,
            'Total Value': totalValue,
            'Total Protein (g)': totalProtein,
            'Total Sugar (g)': totalSugar,
            'Total Fat (g)': totalFat
        })
    
    print(f"Results saved to {filename}")


def saveGoalResultsToCSV(foodList, totalCals, totalValue, servings, reached, targetValue, 
                         strategy='goal-first', filename='yogurt_results.csv'):
    """
    Save goal-first greedy algorithm results to a CSV file with timestamp.
    
    Args:
        foodList: List of Food objects selected
        totalCals: Total calories used
        totalValue: Total value achieved
        servings: Total number of servings
        reached: Boolean indicating if target was reached
        targetValue: Target value goal
        strategy: Name of the greedy strategy used
        filename: CSV filename to save to
    """
    
    # Create CSV file if it doesn't exist with headers
    file_exists = os.path.isfile(filename)
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Date Created', 'Strategy', 'Target Value', 'Reached Target', 
                     'Food Items', 'Total Servings', 'Total Calories', 'Total Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header if file is new
        if not file_exists:
            writer.writeheader()
        
        # Format food items as string
        food_items = ', '.join([f"{food.name}" for food in foodList])
        
        # Write data row
        writer.writerow({
            'Date Created': timestamp,
            'Strategy': strategy,
            'Target Value': targetValue,
            'Reached Target': reached,
            'Food Items': food_items,
            'Total Servings': servings,
            'Total Calories': totalCals,
            'Total Value': totalValue
        })
    
    print(f"Results saved to {filename}")

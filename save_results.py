import csv
import os
from datetime import datetime


def saveResultsToCSV(foodList, totalCals, totalValue, strategy, filename='yogurt_results.csv'):
    """
    Save greedy algorithm results to a CSV file with timestamp.
    
    Args:
        foodList: List of Food objects selected
        totalCals: Total calories used
        totalValue: Total value achieved
        strategy: Name of the greedy strategy used (e.g., 'value', 'cost', 'density')
        filename: CSV filename to save to
    """
    
    # Create CSV file if it doesn't exist with headers
    file_exists = os.path.isfile(filename)
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Date Created', 'Strategy', 'Food Items', 'Item Count', 'Total Calories', 'Total Value']
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
            'Total Value': totalValue
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

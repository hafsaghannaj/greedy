class Food:
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories
    
    @staticmethod
    def getValue(food):
        return food.value
    
    @staticmethod
    def getCost(food):
        return food.calories
    
    @staticmethod
    def density(food):
        return food.value / food.calories
    
    def __repr__(self):
        return f"{self.name}: <value={self.value}, calories={self.calories}>"


def buildMenu(names, values, calories):
    """Build a list of Food objects from names, values, and calories."""
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def testGreedy(foods, maxUnits, keyFunction):
    """Apply greedy algorithm to select foods."""
    # Sort foods by the key function in descending order
    sortedFoods = sorted(foods, key=keyFunction, reverse=True)
    
    usedCals = 0.0
    usedValue = 0.0
    foodList = []
    
    for food in sortedFoods:
        if (usedCals + food.calories) <= maxUnits:
            foodList.append(food)
            usedCals += food.calories
            usedValue += food.value
    
    return foodList, usedCals, usedValue


def testGreedys(foods, maxUnits, saveToCSV=False):
    from save_results import saveResultsToCSV
    
    print('Use greedy by value to allocate', maxUnits,
'calories')
    foodList, cals, value = testGreedy(foods, maxUnits, Food.getValue)
    printResult(foodList, cals, value)
    if saveToCSV:
        saveResultsToCSV(foodList, cals, value, 'by value')
    
    print('\nUse greedy by cost to allocate', maxUnits,
'calories')
    foodList, cals, value = testGreedy(foods, maxUnits,
lambda x: 1/Food.getCost(x))
    printResult(foodList, cals, value)
    if saveToCSV:
        saveResultsToCSV(foodList, cals, value, 'by cost')
    
    print('\nUse greedy by density to allocate', maxUnits,
'calories')
    foodList, cals, value = testGreedy(foods, maxUnits, Food.density)
    printResult(foodList, cals, value)
    if saveToCSV:
        saveResultsToCSV(foodList, cals, value, 'by density')


def printResult(foodList, totalCals, totalValue):
    """Print the result of the greedy selection."""
    print('Selected foods:')
    for food in foodList:
        print(f"  {food.name}: value={food.value}, calories={food.calories}")
    print(f'Total calories: {totalCals}')
    print(f'Total value: {totalValue}')


# Test with yogurt and other foods
if __name__ == '__main__':
    names = ['yogurt strawberry', 'yogurt vanilla', 'yogurt blueberry', 'yogurt greek', 'yogurt honey', 'yogurt vanilla']
    values = [3, 3, 3, 3, 3, 3]  # probiotic score in billions
    calories = [90, 90, 90, 90, 90, 90]
    foods = buildMenu(names, values, calories)
    testGreedys(foods, 750, saveToCSV=True)
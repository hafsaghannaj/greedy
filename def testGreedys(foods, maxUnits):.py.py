class Food:
    def __init__(self, name, value, calories, protein=0, sugar=0, fat=0):
        self.name = name
        self.value = value  # probiotic score
        self.calories = calories
        self.protein = protein  # in grams
        self.sugar = sugar  # in grams
        self.fat = fat  # in grams
    
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
        return f"{self.name}: <value={self.value}, calories={self.calories}, protein={self.protein}g, sugar={self.sugar}g, fat={self.fat}g>"


def buildMenu(names, values, calories, proteins=None, sugars=None, fats=None):
    """Build a list of Food objects from names, values, calories, and macronutrients."""
    menu = []
    
    # Default macronutrients to 0 if not provided
    if proteins is None:
        proteins = [0] * len(names)
    if sugars is None:
        sugars = [0] * len(names)
    if fats is None:
        fats = [0] * len(names)
    
    for i in range(len(names)):
        menu.append(Food(names[i], values[i], calories[i], proteins[i], sugars[i], fats[i]))
    return menu


def testGreedy(foods, maxUnits, keyFunction):
    """Apply greedy algorithm to select foods."""
    # Sort foods by the key function in descending order
    sortedFoods = sorted(foods, key=keyFunction, reverse=True)
    
    usedCals = 0.0
    usedValue = 0.0
    usedProtein = 0.0
    usedSugar = 0.0
    usedFat = 0.0
    foodList = []
    
    for food in sortedFoods:
        if (usedCals + food.calories) <= maxUnits:
            foodList.append(food)
            usedCals += food.calories
            usedValue += food.value
            usedProtein += food.protein
            usedSugar += food.sugar
            usedFat += food.fat
    
    return foodList, usedCals, usedValue, usedProtein, usedSugar, usedFat


def testGreedys(foods, maxUnits, saveToCSV=False):
    from save_results import saveResultsToCSV
    
    print('Use greedy by value to allocate', maxUnits,
'calories')
    foodList, cals, value, protein, sugar, fat = testGreedy(foods, maxUnits, Food.getValue)
    printResult(foodList, cals, value, protein, sugar, fat)
    if saveToCSV:
        saveResultsToCSV(foodList, cals, value, protein, sugar, fat, 'by value')
    
    print('\nUse greedy by cost to allocate', maxUnits,
'calories')
    foodList, cals, value, protein, sugar, fat = testGreedy(foods, maxUnits,
lambda x: 1/Food.getCost(x))
    printResult(foodList, cals, value, protein, sugar, fat)
    if saveToCSV:
        saveResultsToCSV(foodList, cals, value, protein, sugar, fat, 'by cost')
    
    print('\nUse greedy by density to allocate', maxUnits,
'calories')
    foodList, cals, value, protein, sugar, fat = testGreedy(foods, maxUnits, Food.density)
    printResult(foodList, cals, value, protein, sugar, fat)
    if saveToCSV:
        saveResultsToCSV(foodList, cals, value, protein, sugar, fat, 'by density')


def printResult(foodList, totalCals, totalValue, totalProtein, totalSugar, totalFat):
    """Print the result of the greedy selection."""
    print('Selected foods:')
    for food in foodList:
        print(f"  {food.name}: value={food.value}, calories={food.calories}, protein={food.protein}g, sugar={food.sugar}g, fat={food.fat}g")
    print(f'Total calories: {totalCals}')
    print(f'Total value: {totalValue}')
    print(f'Total protein: {totalProtein}g')
    print(f'Total sugar: {totalSugar}g')
    print(f'Total fat: {totalFat}g')


# Test with yogurt and other foods
if __name__ == '__main__':
    names = ['yogurt strawberry', 'yogurt vanilla', 'yogurt blueberry', 'yogurt greek', 'yogurt honey', 'yogurt vanilla']
    values = [3, 3, 3, 3, 3, 3]  # probiotic score in billions
    calories = [90, 90, 90, 90, 90, 90]
    proteins = [8, 10, 9, 15, 7, 10]  # grams of protein
    sugars = [12, 14, 11, 5, 16, 14]  # grams of sugar
    fats = [2, 3, 2, 1, 1, 3]  # grams of fat
    foods = buildMenu(names, values, calories, proteins, sugars, fats)
    testGreedys(foods, 750, saveToCSV=True)
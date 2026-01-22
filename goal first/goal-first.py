class Food:
    def __init__(self, name, value, calories, maxPerFood=10):
        self.name = name
        self.value = value          # probiotic units (billions, etc.)
        self.calories = calories    # calories per serving
        self.maxPerFood = maxPerFood # how many times you can pick this item

    @staticmethod
    def getValue(food):
        return food.value

    @staticmethod
    def getCost(food):
        return food.calories

    @staticmethod
    def density(food):
        return food.value / food.calories if food.calories else float("inf")

    def __repr__(self):
        return f"{self.name}: <value={self.value}, calories={self.calories}, maxPerFood={self.maxPerFood}>"


def buildMenu(names, values, calories, maxPerFood=None):
    """Build a list of Food objects from names, values, and calories."""
    menu = []
    if maxPerFood is None:
        maxPerFood = [10] * len(names)

    for i in range(len(names)):
        menu.append(Food(names[i], values[i], calories[i], maxPerFood[i]))
    return menu


def goalFirstGreedy(foods, targetValue, maxCalories=None, maxServings=None, keyFunction=Food.getValue):
    """
    A) Goal-first greedy:
    - Keep selecting items until totalValue >= targetValue
    - Greedy choice uses keyFunction (default: highest value per serving)
    - Allows repeats up to each food.maxPerFood
    - Optional constraints:
        maxCalories: stop if calories would exceed this
        maxServings: stop if servings would exceed this
    """
    sortedFoods = sorted(foods, key=keyFunction, reverse=True)

    usedCals = 0.0
    usedValue = 0.0
    servings = 0
    foodList = []

    # Track how many times each food is used
    usedCounts = {food.name: 0 for food in sortedFoods}

    madeProgress = True
    while usedValue < targetValue and madeProgress:
        madeProgress = False

        for food in sortedFoods:
            if usedValue >= targetValue:
                break

            # per-food cap
            if usedCounts[food.name] >= food.maxPerFood:
                continue

            # max servings constraint
            if maxServings is not None and (servings + 1) > maxServings:
                continue

            # max calories constraint
            if maxCalories is not None and (usedCals + food.calories) > maxCalories:
                continue

            # take it
            foodList.append(food)
            usedCounts[food.name] += 1
            servings += 1
            usedCals += food.calories
            usedValue += food.value

            madeProgress = True

            # restart from best item again (helps keep servings minimal in greedy sense)
            break

    reached = usedValue >= targetValue
    return foodList, usedCals, usedValue, servings, reached, {k: v for k, v in usedCounts.items() if v > 0}


def printGoalResult(foodList, totalCals, totalValue, servings, reached, counts, targetValue):
    print('Selected foods (goal-first):')
    for food in foodList:
        print(f"  {food.name}: value={food.value}, calories={food.calories}")
    print(f'\nTarget value: {targetValue}')
    print(f'Reached target? {reached}')
    print(f'Total servings: {servings}')
    print(f'Total calories: {totalCals}')
    print(f'Total value: {totalValue}')
    print(f'Counts: {counts}')


def testGoalFirstGreedys(foods, targetValue, maxCalories=None, maxServings=None):
    print(f'Goal-first greedy to reach {targetValue} probiotic units')

    print('\nUse greedy by VALUE (max probiotic per serving)')
    foodList, cals, value, servings, reached, counts = goalFirstGreedy(
        foods, targetValue, maxCalories=maxCalories, maxServings=maxServings, keyFunction=Food.getValue
    )
    printGoalResult(foodList, cals, value, servings, reached, counts, targetValue)

    print('\nUse greedy by DENSITY (probiotic per calorie)')
    foodList, cals, value, servings, reached, counts = goalFirstGreedy(
        foods, targetValue, maxCalories=maxCalories, maxServings=maxServings, keyFunction=Food.density
    )
    printGoalResult(foodList, cals, value, servings, reached, counts, targetValue)

    print('\nUse greedy by LOWEST COST (lowest calories first)')
    foodList, cals, value, servings, reached, counts = goalFirstGreedy(
        foods, targetValue, maxCalories=maxCalories, maxServings=maxServings, keyFunction=lambda x: 1/Food.getCost(x)
    )
    printGoalResult(foodList, cals, value, servings, reached, counts, targetValue)


# Test with yogurt and other foods
if __name__ == '__main__':
    names = [
        'yogurt strawberry', 'yogurt vanilla', 'yogurt blueberry',
        'yogurt greek', 'yogurt honey', 'probiotic capsule'
    ]

    # value = probiotic units (billions / score)
    values = [8, 6, 7, 10, 5, 25]

    calories = [130, 120, 125, 100, 140, 0]

    # optional: cap how many times each item can be used
    maxPerFood = [2, 2, 2, 3, 1, 2]

    foods = buildMenu(names, values, calories, maxPerFood=maxPerFood)

    targetValue = 40          # goal: reach 40 units
    maxCalories = 750         # optional constraint (set to None to ignore)
    maxServings = 6           # optional constraint (set to None to ignore)

    testGoalFirstGreedys(foods, targetValue, maxCalories=maxCalories, maxServings=maxServings)

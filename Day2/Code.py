#get the meal cost from stdIn
mealCost = float(input())

#get the tip percent from stdIn
tipPercent = float(input())

#get the tax percent from taxPercent
taxPercent = float(input())

#calculating the totalCost
totalCost = mealCost + mealCost * tipPercent/100 + mealCost * taxPercent/100

#rounding the answer
totalCost  = round(totalCost)

#printing the answer
print("The total meal cost is " + str(totalCost) + " dollars.")

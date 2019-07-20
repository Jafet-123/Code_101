'''
Much app MVP
Vo.1
By applause
the purpose is to produce a dinner menu from favorites dishes,
and produce a shopping list if required
'''
# -------- Imports ---------
from random import choice 
# -------- A. Functions --------

# A1. Choose dishes

def chooseDishes(days):
    while len(myMenu) < int(days):
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Done! Here's your menu...")
    print()
    for dish in myMenu:
        print(dish)
    print()
    print("out of all the dishes, my favorite has to be..." + choice(myMenu) )
            

# A2. Build shopping list

def buildShoppingList():
    myShoppingList = []
    if "pizza" in myMenu:
        myShoppingList.append(pizza)
    if "burgers" in myMenu:
        myShoppingList.append(burgers)
    if "pork stir fry" in myMenu:
        myShoppingList.append(porkStirFry)
    if "fajitas" in myMenu:
        myShoppingList.append(fajitas)
    if "tacos" in myMenu:
        myShoppingList.append(tacos)
    if "fried chicken" in myMenu:
        myShoppingList.append(friedChicken)
    if "omelete" in myMenu:
        myShoppingList.append(omelete)
    print()
    for dish in myShoppingList:
        for ingredient in dish:
            print(ingredient)
    print()
    print("Voila! Bon apetit")

# -------- B. Lists ----------

foodWeLike = ["pizza", "burgers", "pork stir fry", "fajitas", "tacos", "fried chicken", "omelete" ]

pizza = ["pizza Base", "Tomato sauce", "cheese", "pepperoni"]
burgers = ["beef", "buns", "lettuce", "tomato", "onion", "ketchup"]
porkStirFry = ["pork", "peppers", "onions", "sauce"]
fajitas = ["chicken", "onions", "peppers", "salsa"]
tacos = ["beef", "shells", "sour cream", "lettuce", "peppers"]
friedChicken = ["mustard","mayo", "chicken"]
omelete = ["eggs", "cheese", "bacon", "veggies"]

myMenu = []
myShoppingList = []

# 1. How many days to plan?

print("hello, I'm much i will help you plan your dinner menu ")

answer = input("How many days would you like me to plan? ")

print("Ok, I'm going to plan " + answer + " dinner(s) from your favorite meals list" )

# 2. choose dishes

chooseDishes(answer)


# 3. Build shopping list

answer = input("would you like a shopping list menu? ")

if answer == 'y':
    buildShoppingList()
else:
    print(" You got it! Bye for now :)")


#Author: Shane Kramer
#Date: 10/7/2017
#Descpt: Keychains for Sale
#       A simple textbased system for ordering keychains. The user will input
#       a number corresponding to an option in the menu. User can either add
#       or subtract keychains from the order and view the total order cost.

keychainsTotal = 0
keychainPrice = 10
salesTax = 0.0825
shipCost = 5
addCostPer = 1

def addKeychain():
    global keychainsTotal
    print("You have " + str(keychainsTotal) + " keychains.")
    add = int(input("How many to add?: "))
    keychainsTotal += add
    print("You now have " + str(keychainsTotal) + " keychains.")
    print()
    return

def removeKeychain():
    global keychainsTotal
    print("You have " + str(keychainsTotal) + " keychains.")
    remove = int(input("How many to remove?: "))
    if(keychainsTotal - remove < 0):
        print("You cannot remove that many!")
        removeKeychain()
        return
    keychainsTotal -= remove
    print("You now have " + str(keychainsTotal) + " keychains.")
    print()
    return

def viewOrder():
    print("You have " + str(keychainsTotal) + " keychains.")
    print("Keychains cost $10 each.")
    totalShipping = shipCost + keychainsTotal*addCostPer
    subtotalCost = keychainsTotal*10 + totalShipping
    print("Shipping cost for order plus keychains is $" + str(totalShipping))
    print("Your subtotal is " + str(subtotalCost))
    salesCost = salesTax * subtotalCost
    print("Tax is 8.25% or $" + str(salesCost))
    totalCost = subtotalCost + salesCost
    print("The total cost is " + str(totalCost) + ".")
    print()
    return

def checkout():
    print()
    print("CHECKOUT")
    print()
    name = str(input("What is your name?: "))
    viewOrder()
    print("Thanks for your order, " + name)
    print()
    return
    
               
def chooseOption():
    if(choice == 1):
        addKeychain()
    elif(choice == 2):
        removeKeychain()
    elif(choice == 3):
        viewOrder()
    else:
        print("Error try again!")
        chooseOption()

print("Ye Olde Keychain Shoppe")

print("1. Add Keychains to Order")
print("2. Remove Keychains from Order")
print("3. View Current Order")
print("4. Checkout")

choice = int(input("Please enter your choice: "))
while choice != 4:
    chooseOption()
    print("1. Add Keychains to Order")
    print("2. Remove Keychains from Order")
    print("3. View Current Order")
    print("4. Checkout")
    print()
    choice = int(input("Please enter your choice: "))
if(choice == 4):
    checkout()

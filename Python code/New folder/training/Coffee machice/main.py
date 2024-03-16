
from menu import MENU


tank_water = 300
tank_milk = 200
tank_coffee = 100

penny = 0.01
nickel = 0.05
dime = 0.10
quarter = .25

money_in_machine = 0.00

def payment():
  number_of_quarters = int(input("How many quarters would you like to insert?"))
  number_of_dimes = int(input("How many dimes would you like to insert?"))
  number_of_nickels = int(input("How many nickels would you like to insert?"))
  number_of_pennies = int(input("How many pennies would you like to insert?"))
  money_inserted = (number_of_quarters * 0.25) + (number_of_dimes * 0.10) + (number_of_nickels * 0.05) + (number_of_pennies * 0.01)
  return money_inserted
  

#Return false if there is not enough of any resource, otherwise deduct the amount of resources
def check_resources(choice):
  global tank_water
  global tank_milk
  global tank_coffee
  if choice in MENU:
    drink_ingredients = MENU[choice]["ingredients"]
    for i in drink_ingredients:
      
      # check if enough water
      if i == "water":
        water = drink_ingredients["water"]
        if water > tank_water:
          print("Sorry, not enough water, please refill")
          return False
      
      #check if enough milk
      if i == "milk":
        milk = drink_ingredients["milk"]
        print(milk)
        if milk > tank_milk:
          print("Sorry, not enough milk, please refill")
          return False
      
      #check if enough coffee
      if i == "coffee":
        coffee = drink_ingredients["coffee"]
        if coffee > tank_coffee:
          print("Sorry, not enough coffee, please refill")
          return False
      
      # if water is > tank, reduce tank by total
    if "water" in drink_ingredients:
      water = drink_ingredients["water"]
      tank_water -= water
      
      #if milk is > tank, reduce tank by total
    if "milk" in drink_ingredients:
      milk = drink_ingredients["milk"]
      tank_milk -= milk
      
      #if coffee is > tank, reduce tank by total
    if "coffee" in drink_ingredients:
      coffee = drink_ingredients["coffee"]
      tank_coffee -= coffee
    

def get_order():
  
  choices = ["espresso", "latte", "cappuccino"]
  choice = input("Would you like Espresso, Latte, or Cappuccino\n").lower()
  if choice == "off":
    return "off"
  elif choice == "report":
      print(f"Water: {tank_water}\n Milk: {tank_milk}\n Coffee: {tank_coffee}\n Money: {money_in_machine:.2f}\n")
      return "report"
  elif choice not in choices:
    print("You have not chosen a real coffee stupid")
    return "off"
  else:
    return choice
    
  
  
def make_coffee():
  can_make = True
  while can_make:
    choice = get_order()
    if choice == "report":
      continue
    if choice == "off":
      break
    check = check_resources(choice)
    if check == False:
      break
    money_inserted = payment()
    if money_inserted < MENU[choice]["cost"]:
      print("Sorry, that was not enough money")
      break
    if money_inserted >= MENU[choice]["cost"]:
      global money_in_machine
      money_in_machine += money_inserted
      change = money_inserted - MENU[choice]["cost"]
      money_in_machine -= change
      change = "{:.2f}".format(change)
      print(f"Thank you for your purchase, your change is {change}")
      
      print(f"Here is your {choice}, enjoy!")
      
    
    
  
  
make_coffee()
  


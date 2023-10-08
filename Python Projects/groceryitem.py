import datetime
print("\tWelcome To The Grocery List App.")
print("\tCurrent Date and Time: {}".format(datetime.datetime.now()))
print("\tYou have currently Meat and Cheese in your list.")

#Adding New Items to The List
grocery_list = list()
grocery_list.append("meat")
grocery_list.append("cheese")
groc_item = input("\n\tType of food to add to the grocery list: ")
grocery_list.append(groc_item)
groc_item = input("\tType of food to add to the grocery list: ")
grocery_list.append(groc_item)
groc_item = input("\tType of food to add to the grocery list: ")
grocery_list.append(groc_item)




#Logic Of Program and Display of Values
print("\n\tHere is your grocery list:")
print("\t{}".format(grocery_list))
print("\tHere is your grocery List sorted:")
grocery_list.sort()
print("\t{}".format(grocery_list))

print("\n\tSimulating Grocery Shopping.......")

print("\n\tCurrent Grocery list: {} items".format(len(grocery_list)))
print("\t{}".format(grocery_list))
remv_item = input("\tWhat food item did you just buy: ")
grocery_list.remove(remv_item)
print("\tRemoving {} from list....".format(remv_item))

print("\n\tCurrent Grocery list: {} items".format(len(grocery_list)))
print("\t{}".format(grocery_list))
remv_item = input("\tWhat food item did you just buy: ")
grocery_list.remove(remv_item)
print("\tRemoving {} from list....".format(remv_item))

print("\n\tCurrent Grocery list: {} items".format(len(grocery_list)))
print("\t{}".format(grocery_list))
remv_item = input("\tWhat food item did you just buy: ")
grocery_list.remove(remv_item)
print("\tRemoving {} from list....".format(remv_item))

print("\n\tCurrent grocery list: {} items".format(len(grocery_list)))
print("\t{}".format(grocery_list))

print("\n\tSorry, the store is out of Meat.")
empt_item = input("\tWhat food would you like instead: ")
grocery_list.insert(0,empt_item)

print("\n\tHere is what remains on your grocery list:")
print("\t{}".format(grocery_list))

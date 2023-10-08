print("\tWelcome to the Favorite Teachers Program")

#Input Teachers Name
teach_lst = []
val = input("\n\tWho is your first favorite teacher: ")
teach_lst.append(val)
val = input("\tWho is your second favorite teacher: ")
teach_lst.append(val)
val = input("\tWho is your third favorite teacher: ")
teach_lst.append(val)
val = input("\tWho is your fourth favorite teacher: ")
teach_lst.append(val)

#Display Tecahers Data as per logic
print("\n\tYour favorite teachers ranked are: {}".format(teach_lst))
teach_lst.sort()
print("\tYour favorite teachers alphabetically ranked are: {}".format(teach_lst))
teach_lst.reverse()
print("\tYour favorite teachers in reverse alphabetical order are: {}".format(teach_lst))

print("\n\tOops, {} is no longer your first favorite teacher.Who is your new favorite teacher".format(teach_lst[0]))
teach_lst.insert(0,input())

print("\n\tYour favorite teachers ranked are: {}".format(teach_lst))
teach_lst.sort()
print("\tYour favorite teachers alphabetically ranked are: {}".format(teach_lst))
teach_lst.reverse()
print("\tYour favorite teachers in reverse alphabetical order are: {}".format(teach_lst))

print("\n\tYour top two teacher are: {} and {}".format(teach_lst[0],teach_lst[1]))
print("\tYour next two favorite teachers are: {} and {}".format(teach_lst[2],teach_lst[3]))
print("\tYour last favorite teacher is: {}".format(teach_lst[-1]))
print("\tYou have a total of 5 favorite teachers.")

#Removing a Teacher from the list and Displaying The Data
while True:
    print("\n\tYou have decided you no longer like a teacher.Which teacher would you like to remove from your list: ")
    rmv_teach = input()
    if rmv_teach == teach_lst[0] or rmv_teach == teach_lst[1] or rmv_teach == teach_lst[2] or rmv_teach == teach_lst[3]:
        break
    else:
        print("\tPlease Enter a name from the specified list")


for i in teach_lst:
    if i == rmv_teach:
        teach_lst.remove(i)

print("\n\tYour favorite teachers ranked are: {}".format(teach_lst))
teach_lst.sort()
print("\tYour favorite teachers alphabetically ranked are: {}".format(teach_lst))
teach_lst.reverse()
print("\tYour favorite teachers in reverse alphabetical order are: {}".format(teach_lst))

print("\n\tYour top two teacher are: {} and {}".format(teach_lst[0],teach_lst[1]))
print("\tYour next two favorite teachers are: {} and {}".format(teach_lst[2],teach_lst[3]))
print("\tYour last favorite teacher is: {}".format(teach_lst[-1]))
print("\tYou have a total of 5 favorite teachers.")

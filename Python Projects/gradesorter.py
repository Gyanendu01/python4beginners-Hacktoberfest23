print("\tWelcome to the Grade Sorter App")

#Input Marks
while True:
    mrk1 = int(input("\n\tWhat is your grade (0-100): "))
    mrk2 = int(input("\tWhat is your grade (0-100): "))
    mrk3 = int(input("\tWhat is your grade (0-100): "))
    mrk4 = int(input("\tWhat is your grade (0-100): "))
    if mrk1>=0 and mrk1<=100 and mrk2>=0 and mrk2<=100 and mrk3>=0 and mrk3<=100 and mrk4>=0 and mrk4<=100:
        break
    else:
        print("\tINVALID INPUT:")

#Program Logic and Output Display
lst_mrk = [mrk1,mrk2,mrk3,mrk4]
print("\n\tYour grades are: {}".format(lst_mrk))

lst_mrk.sort(reverse=True)
print("\n\tYour grades from highest to lowest are: {}".format(lst_mrk))

print("\n\tYour lowest two grades will be dropped now.")
print("\tRemoved grade: {}".format(lst_mrk[len(lst_mrk)-1]))
print("\tRemoved grade: {}".format(lst_mrk[len(lst_mrk)-2]))
lst_mrk.pop(len(lst_mrk)-1)
lst_mrk.pop(len(lst_mrk)-1)

print("\tYour remaining grades are: {}".format(lst_mrk))
print("\tNice work! Your highest grade is {}".format(lst_mrk[0]))

list1 = [12,-7,5,64,-14]
list2 = []
#list2 = [12,14,-95,3] in order to check for list2 just comment out list1 and change list1 to list2 in for loop
for number in list1:
    if number > 0:
        list2.append(str(number))    

print(",".join(list2))
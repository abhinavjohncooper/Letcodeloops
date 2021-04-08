list1 = [12,-7,5,64,-14]
list2 = []
for number in list1:
    if number > 0:
        list2.append(str(number))    

print(",".join(list2))

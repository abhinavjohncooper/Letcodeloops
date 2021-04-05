terms = int(input("Enter the number of terms you want to get displayed : \n"))
n1, n2 = 0, 1
count = 0
if terms<=0:
    print("Invalid value")
elif terms==1:
    print("Fibonacci numbers upto",terms,":")
    print(n1)
else:
    print("Fibonacci numbers : ")
while count<terms-1:
    print(n1,end = ',')
    nth= n1+n2
    n1=n2
    n2=nth
    count += 1 
print(n1)            
#Explain your work

#Question 1
my_list = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
my_list[0:4],my_list[4:8] = my_list[4:8],my_list[0:4]
print("New list is: ",my_list)


#Question 2
x = int(input("Enter a single digit integer: "))
num = 0


while x < 0 or x >= 10:
    print("Invalid entry! "+"\n")
    x = int(input("Enter a single digit integer: "))
    if x >= 0 and x <10:
     break
   
    
while True:
    if num <= x:
     print(num)
    else:
        break
    num = num + 2

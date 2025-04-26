#finding the average height of a tree
t1 = 42
t2 = 56
t3 = 91
t4 = 98
t5 = 64

sum = t1+t2+t3+t4+t5
print("the sum of all tree heights are", sum)

average_height_tree = sum/5
print("The average height of a tree is", average_height_tree)

#Finding the denominations
amount = int(input("Enter the amount to be withdrawn "))
notes_100 = amount//100
notes_50 = (amount%100)//50
notes_10 = ((amount%100)%50)//10
print("The notes of $100", notes_100)
print("The notes of $50 is", notes_50)
print("The notes of $10 is", notes_10)

#taking marks as input from the user
print("Enter the marks obtained in 4 subjects ")
math = int(input("Enter maths percentage "))
language = int(input("Enter language percentage "))
science = int(input("Enter sciences percentage "))
french = int(input("Enter French percentage "))

sum1 = math+language+science+french
print("The sum marks in all subjects is", sum1)

per = (sum1/400)*100
print("The total percentage secured by the student is", per)
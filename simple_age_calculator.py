#building age calculator. 
name = input("enter you name:")
print("hello", name , "i can help you calculate your age")
input()
print("please enter your birth year:")
birth_year = int(input())
current_year = int(input("please enter current year:"))
age = current_year - birth_year
print("congratulations", name, "you are", age, "years old")


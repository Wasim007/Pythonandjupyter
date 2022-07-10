# If , else , elif functions example


# khurram_age=input("How old is Khurram")
# type(khurram_age)
# print(type(khurram_age))
# khurram_age=int(khurram_age)
# age_at_school=4
# if khurram_age>=age_at_school:
#     print("Yes! You can admitt your brother at school")
# elif khurram_age<=age_at_school:
#     print(khurram_age,"Sorry! Your brother is still baby")


university_required_age=18
my_age=input("What is your age")
my_age=int(my_age)
if my_age==university_required_age:
    print("Yes You can join University")
elif my_age>=25:
    print("Yes You can get your PHD degree")
elif my_age<=18:
    print(my_age,"Sorry! you have to pass 2nd year degree to admitt in University")
# else:
#     print(my_age,"Sorry You are still not young to join university")
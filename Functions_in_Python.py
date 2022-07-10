# Method of defining Functions

# Ist Method of defining Function
from typing import Text


def print_name():
    print("My name is @Ahmad Wasim Khan")
    print("My name is @Ahmad Wasim Khan")
    print("My name is @Ahmad Wasim Khan")
    print("My name is @Ahmad Wasim Khan")

print_name()


# 2nd Method of defining Function

def my_university_name():
    text="University of Science and Technology (Bannu)"
    print(text)
    print(text)
    print(text)
    print(text)
    print(text)
    print(text)

my_university_name()


# 3rd Method of definig Function

def my_address(text2):
    print(text2)
    print(text2)
    print(text2)
    print(text2)
    print(text2)

my_address("Nizam Bazar Bannu")


# 4th Method of defining Function including if, else, elif functions inside.


def student_age_calculator(age):
    if age==5:
        print("Khurram can join school")
    elif age>=15:
        print("Khurram can join College")
    else:
        print("Khurram are still baby")


student_age_calculator(1)



# def my_age(age):
#     future_age=age+20
#     return future_age

# print(my_age(18))

#  OR the my age (age) is also written as below

def future_age(age):
    new_age=age+20
    return new_age
    print(new_age)

future_predicted_age=future_age(50)
print(future_predicted_age)

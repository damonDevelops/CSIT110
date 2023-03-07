# Assignment 1, CSIT110

# Question 1

# steps = int(input("Enter the number of steps from egg to frog: "))
# arrow = "-->"
# print("Here is the expected life cycle:")
# print("egg" + (steps * arrow) + "frog")

# Question 2

# book = input("Enter your favourite book name: ")
# author = input("Enter the author's name: ")
# print()
# print("Your favourite book is \"" + book + "\" written by \"" + author + "\"" + ".")


# Question 3
# puppies = int(input("Enter the number of puppies: "))
# kitties = int(input("Enter the number of kitties: "))

# p_cost = 40
# k_cost = 30

# print("You have adopted " + str(puppies) + " puppies and " + str(kitties) + " kitties.")
# print("The insurance fee is " + "$" + str(((puppies * p_cost) + (kitties * k_cost))) + ".")

# Question 4
# first_int = int(input("Enter the 1st positive integer: "))
# second_int = int(input("Enter the 2nd positive integer: "))
# third_int = int(input("Enter the 3rd positive integer: "))

# answer = (
#             (first_int * second_int)+
#             (first_int * third_int)+
#             (second_int * third_int)
#         )


# print("Here is the equation:")
# print("{0} X {1} + {0} X {2} + {1} X {2}".format(first_int, second_int, third_int) + " = " + str(answer))

# Question 5
# f_code = input("Enter the first subject code: ")
# f_name = input("Enter the first subject name: ")
# f_cp = int(input("Enter the first credit point: "))

# s_code = input("Enter the second subject code: ")
# s_name = input("Enter the second subject name: ")
# s_cp = int(input("Enter the second credit point: "))

# print("Your enrolment details are as follows:")
# print("{0:<10}{1:<40}{2:^15}".format("Code", "Name", "Credit"))
# print("{0:<10}{1:<40}{2:^15}".format(f_code, f_name, f_cp))
# print("{0:<10}{1:<40}{2:^15}".format(s_code, s_name, s_cp))
# print("{0:<10}{1:<40}{2:^15}".format("Total", "", str(f_cp+s_cp)))

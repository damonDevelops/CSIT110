#Assignment 2

###########
#QUESTION 1
###########

# dogs = int(input("Enter the number of dogs: "))
# cats = int(input("Enter the number of cats: "))

# #if there are multiple dogs
# if dogs > 1:
#     #if there are multiple cats
#     if cats > 1:
#         print("You have adopted {0} dogs and {1} cats.".format(dogs, cats))
#     #if there is one cat and multiple dogs
#     elif cats == 1:
#         print("You have adopted {0} dogs and {1} cat.".format(dogs, cats))
# #if there is one cat
# elif dogs == 1:
#     #if there are multiple cats and one dog
#     if cats > 1:
#         print("You have adopted {0} dog and {1} cats.".format(dogs, cats))
#     #if there is one cat and one dog
#     elif cats == 1:
#         print("You have adopted {0} dog and {1} cat.".format(dogs, cats))

###########
#QUESTION 2
###########
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# dob = input("Enter your dob (DD-MM-YYYY): ")
# format_type = input("Choose a format:  (A)bbreviated  (N)ormal: ")

# date_list = dob.split("-")
# day = date_list[0]
# month = int(date_list[1])
# year = date_list[2]
# month_string = ""

# if month == 1:
#     month_string = "Jan"
# elif month == 2:
#     month_string = "Feb"
# elif month == 3:
#     month_string = "Mar"
# elif month == 4:
#     month_string = "Apr"
# elif month == 5:
#     month_string = "May"
# elif month == 6:
#     month_string = "Jun"
# elif month == 7:
#     month_string = "Jul"
# elif month == 8:
#     month_string = "Aug"
# elif month == 9:
#     month_string = "Sep"
# elif month == 10:
#     month_string = "Oct"
# elif month == 11:
#     month_string = "Nov"
# elif month == 12:
#     month_string = "Dec"
# else:
#     print("Month not found")
#     exit(-1)

# #printing information
# print("{:<15}{:<15}{:<15}".format("First Name", "Last Name", "Date of Birth"))


# #Normal format
# if format_type == "N":
#     print("{:^15}{:^15}{:^15}".format(first_name, last_name, dob))
# elif format_type == "A":
#     print("{:<15}{:<15}{:<15}".format(first_name, last_name, "{0}/{1}/{2}".format(day, month_string, year)))
# else:
#     print("{:<15}{:<15}{:^15}".format(first_name, last_name, "{0}-{1}-{2}".format(year, month, day)))


###########
#QUESTION 3
###########
# pear_type = input("Which kind of pears would you like: (N)ashi 4.99/kilo (C)orella 5.99/kilo: ")

# if pear_type == "N":
#     pear_weight = float(input("How many kilograms of pears would you like: "))
#     pear_price = 4.99
#     pear_type = "Nashi"
# elif pear_type == "C":
#     pear_weight = float(input("How many kilograms of pears would you like: "))
#     pear_price = 5.99
#     pear_type = "Corella"
# else:
#     pear_weight = 0
#     pear_price = 0
#     pear_type = "-"


# orange_type = input("Which kind of oranges would you like: (H)amlin 2.99/kilo (M)oro 3.99/kilo: ")

# if orange_type == "H":
#     orange_weight = float(input("How many kilograms of oranges would you like: "))
#     orange_price = 2.99
#     orange_type = "Hamlin"
# elif orange_type == "M":
#     orangeKilo = float(input("How many kilograms of oranges would you like: "))
#     orange_price = 3.99
#     orange_type = "Moro"    
# else:
#     orangeKilo = 0
#     orange_price = 0
#     orange_type = "-"
    
# total_orange_price = orangeKilo * orange_price
# total_pear_price = pear_weight * pear_price
# total_price = total_orange_price+total_pear_price

# print("{0:>15}{1:>15}{2:>15}{3:>15}".format("Item","Weight","Unit Price","Price"))
# print("{0:>15}{1:>15}{2:>15}{3:>15.2f}".format(pear_type,pear_weight,pear_price,total_pear_price))
# print("{0:>15}{1:>15}{2:>15}{3:>15.2f}".format(orange_type,orangeKilo,orange_price,total_orange_price))
# print("{0:>15}{1:>15}{2:>15}{3:>15.2f}".format("Total","","",total_price))


###########
#QUESTION 4
###########
# adult = int(input("How many adult passengers ($100 each): "))
# child = int(input("How many child passengers ($60 each): "))
# total = (adult * 100) + (child * 60)
# baggage = input("Add baggage (Y)es (N)o: ")
# bag_count = 0
# if baggage == "Y":
#     bag_count =  int(input("How many bags do you have (1) 15kg for $53.13 (2) 30 kg for $99.24: "))
#     if bag_count == 1:
#         total += 53.13
#     elif bag_count == 2:
#         total += 99.24
#     else:
#         print("The heaviest baggage you can add is 30 kg for $99.24")
#         total +=99.24

# total += 50
# print("Your ticket costs ${} (including Fuel Surcharge $50)".format(round(total, 2)))

###########
#QUESTION 5
###########
# counter = int(input("Enter an integer: "))
# start_value = 3
# number_string = "3"
# for i in range(0, counter-1):
#     if (start_value) % 12 == 0:
#         number_string += ":" + str(start_value + 3)
#     else:
#         number_string += "," + str(start_value + 3)
    
#     start_value +=3

# print(number_string + ".")

###########
#QUESTION 6
###########
# start = int(input("Enter the starting integer: "))
# end = int(input("Enter the ending integer: "))

# if start <= end:
#     print("{:<10}{:<10}{:>10}".format("Num", "Triple", "Quadruple"))
#     for i in range(start, end + 1):
#         print("{:<10}{:<10}{:>10}".format(i, i*3, i*4))
# else:
#     print("Your starting integer is larger than the ending integer.")
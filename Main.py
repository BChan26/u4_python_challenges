# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?

 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# ---------------------------------
#      Solution Goes Here ->

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
def minutes_to_seconds(value):
    conversion = value * 60
    # print(conversion)
    return conversion
minutes_to_seconds(2)

# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
def hours_to_seconds(value):
    conversion = value * 60 * 60
    # print(conversion)
    return conversion
hours_to_seconds(1)

# -  We're on the right track here, how many seconds are in a day
def days_to_seconds(value): 
    conversion = value * 24 * 60 * 60
    # print(conversion)
    return conversion
days_to_seconds(2)

# - How many Hours are in the month of June? 
def hours_in_june(value):
    conversion = value * 30 * 24 
    # print(conversion)
    return conversion
hours_in_june(1)

# - How many Minutes are in the month of August?
def minutes_in_august(value):
    conversion = value * 31 * 24 * 60
    # print(conversion)
    return conversion
minutes_in_august(1)

# ---------------------------------


#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->
def mid(value): 
    if len(value) % 2 == 0:
        print("")
        return ""
    if len(value) % 2 == 1:
        print(value[int((len(value) / 2) - 0.5)])
        return value[int((len(value) / 2) - 0.5)]
# mid("tea")
# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->
def covert(insert):
    count = len(insert) - 4
    endcap = insert[-4:]
    synthesis = "*"*count + endcap
    print(synthesis)
#From Alvin

# ---------------------------------



# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------
#      Solution Goes Here ->
def online_count(my_dict):
    count=0
    for i in my_dict.values():
        if i == "online":
            count+=1
    return count 

my_dict = {"Tyler":"online",
            "Justin":"online",
            "Lorenzo":"online",
            "Jack" : "online"}
            
ans = online_count(my_dict)            
print(ans)
#From Tyler
# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->
def discount(price, off):
    percent = off/100
    amt_discount = percent * price
    savings = price - amt_discount
    print(savings)
    #From Jason
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->
import math
def pythagorean(num1, num2):
    return (math.sqrt((num1**2)+(num2**2)))
print(pythagorean(3,3))
#From Devon
# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

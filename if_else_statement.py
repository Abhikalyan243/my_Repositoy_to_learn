from loguru import logger
import math

# length_of_land = 100
# breadth_of_land = 150
# bricks_cost_per_piece = 10.5
# labour_name = "chandu"
# mistri_name = "maroti"
# is_home = True

# length_of_land = int(input("enter your lenth of land"))
# if length_of_land < 100 :
#     logger.info(f"your length is not sufficesnt to build 4BHK ")
# else:
#     logger.info(f"can u please share your requirement ")
    
# user_lenth = int(input("Enter your number: "))

# if user_lenth == 0:
#     logger.info("Zero is neither even nor odd.")
# elif user_lenth % 2 == 0:
#     logger.info(f"{user_lenth} is an even number.")
# else:
#     logger.info(f"{user_lenth} is an odd number.")


new_list=[1,2,3,4,5,6]
sec_list=[4,5,6,7,8]

new_set = set(new_list)
sec_set = set(sec_list)

missing_value = new_set - sec_set
logger.info(missing_value)

new_list = [1, 2, 3, 4, 5, 6]
sec_list = [4, 5, 6, 7, 8]

new_set = set(new_list)  # {1, 2, 3, 4, 5, 6}
sec_set = set(sec_list)  # {4, 5, 6, 7, 8}

additional_values = sec_set - new_set

# print("Additional value(s) in new_list:", additional_values)


list11=[12,33,42,121,543,65]

largest_num=0

for i in  list11:
    if i > largest_num:
        largest_num = i
print(largest_num)

a,b=2,4
c="@"
print(a*c*b)
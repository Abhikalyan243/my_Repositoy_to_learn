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
    
user_lenth = int(input("Enter your number: "))

if user_lenth == 0:
    logger.info("Zero is neither even nor odd.")
elif user_lenth % 2 == 0:
    logger.info(f"{user_lenth} is an even number.")
else:
    logger.info(f"{user_lenth} is an odd number.")

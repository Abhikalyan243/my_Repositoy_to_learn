from loguru import logger
import math

length_of_land = 100
breadth_of_land = 150
bricks_cost_per_piece = 10.5
labour_name = "chandu"
mistri_name = "maroti"
is_home = True

total_are_of_land = length_of_land * breadth_of_land

perimeter_of_land = 2 *( breadth_of_land + length_of_land)
total_emp = labour_name + mistri_name

logger.info(f"toatal are of my land is {total_are_of_land} sq ft ") 

# logger.info(f"perimeter of land {perimeter_of_land} ft ")
# logger.info (f"toatl_emp {labour_name },{mistri_name} ")



# a="1"
# b="3"
# print(a+b)

total_are_of_land = int(input("please emter your length of your land : "))
total_breadth_of_land = int (input("enter the bredth your land : "))

total_area_of_land1 = total_are_of_land * total_breadth_of_land 

logger.info(f"total are of land { total_area_of_land1} sq ft") 

# lit="Abhijeet"

# for i in lit:
#     print(i)

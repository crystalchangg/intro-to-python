# paint.py
# Crystal Chang
#
# Calculate the number of paint cans needed based on room size.

# Name of the paint calculator
print("Paint coverage estimator")
# Input room length in inches
room_length=input("Length of room in inches:")
room_length=float(room_length)
# Input room width in inches
room_width=input("Width of room in inches:")
room_width=float(room_width)
# Input average room height in inches
average_room_height=input("Average height of room in inches:")
average_room_height=float(average_room_height)
# Formula for area of the room wall
room_wall_area=2*(room_length*average_room_height)+2*(room_width*average_room_height)
# Conversion from square inches to square feet
room_wall_area=room_wall_area/144
# Formula for the number of cans needed
number_of_cans=(room_wall_area)//100
number_of_cans=int(number_of_cans)+1
# Output result
print("You'll want", number_of_cans, "cans.")

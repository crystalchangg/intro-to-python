# heart.py
# Crystal Chang
#
# Based on age, the maximum heart rate and target heart rate can be predicted.

# Input age
age=input("Enter your age:")
age=int(age)
# Calculate bpm based on inputted age
bpm=220-age
bpm=int(bpm)
# Output result
print("Your maximum heart rate is", bpm, "bpm")
# Calculations for lower end and upper end of the target heart rate
lower_end_of_target_heart_rate=bpm*0.5
lower_end_of_target_heart_rate=float(lower_end_of_target_heart_rate)
upper_end_of_target_heart_rate=bpm*0.85
upper_end_of_target_heart_rate=float(upper_end_of_target_heart_rate)
# Output result
print("Your target heart rate is", lower_end_of_target_heart_rate,"-",upper_end_of_target_heart_rate,"bpm")

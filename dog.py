# dog.py
# Crystal Chang
#
# Giving instructions on dog walking based on the weather

# Weather and temperature input
weather=input("Enter weather condition (rainy/sunny/snowy/cloudy):")
# Instructions based on sunny input
if weather == "sunny":
    temperature=input("Enter temperature:")
    temperature=int(temperature)
    if temperature>80 and temperature<=114:
        print("Instructions for the walk:")
        print("The dog should be taken for a walk in the shade and given water.")
    elif temperature>45 and temperature<=80:
        print("Instructions for the walk:")
        print("The dog can enjoy a regular walk.")
    elif temperature>-14 and temperature<=45:
        print("Instructions for the walk:")
        print("Dress the dog warmly for a walk.")
    else:
        print("Instructions for the walk:")
        print("Invalid weather condition.")
# Instructions based on rainy input
elif weather == "rainy":
    print("Instructions for the walk:")
    print("The dog should be taken for a short walk with an umbrella.")
# Instructions based on snowy input
elif weather == "snowy":
    print("Instructions for the walk:")
    print("Take the dog for a short walk and ensure they stay warm.")
# Instructions based on cloudy input
elif weather == "cloudy":
    print("Instructions for the walk:")
    print("Enjoy a regular walk with your dog.")
# Instructions based on invalid input
else:
    print("Instructions for the walk:")
    print("Invalid weather condition.")

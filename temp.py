# temp_list.py
# Crystal Chang 
#
# Using a given file to make a growing list of years and temperatures 

# Inputting file name to read
filename=input("Temperature anomaly filename:")
# Reading file 
infile=open(filename)
# Building a header
header=infile.readline()
# Setting up list to prepare for adding 
temp_list=[]
# Using for loop to read temperatures from the inputted file
for line in infile:
    # Stripping whitespace off
    line=line.strip()
    # Separates items in list
    year,temp=line.split(",")
    # Converting temperature to float while adding in new temperature values within list 
    temp_list.append(float(temp))
# Printing out temperature list
print(temp_list)


# temp_file_stats.py
# Crystal Chang
#
# Using a given file to read minimum and maximum temperatures out of all the years

# Setting up null values for min and max temps and min and max years before reading temperatures
min_temp=None
max_temp=None
min_year=None
max_year=None
# Inputting file name to read
filename=input("Temperature anomaly filename:")
# Reading file 
infile=open(filename)
# Building a header
header=infile.readline()
# Using for loop to read temperatures from the inputted file
for line in infile:
    # Stripping whitespace off
    line=line.strip()
    # Separates items in list
    year,temp=line.split(",")
    # Converting temperature to float 
    temp=float(temp)
    # Boolean expression to update read lines of temperatures until smallest temperature 
    if min_temp==None or temp<min_temp:
        # Most updated temperature is the minimum temperature
        min_temp=temp
        min_year=year
    # Boolean expression to update read lines of temperatures until largest temperature
    if max_temp==None or temp>max_temp:
        # Most updated temperature is the maximum temperature
        max_temp=temp
        max_year=year
# Printing min and max temperatures of those years
print("Min temp:", min_temp, "in", min_year)
print("Max temp:", max_temp, "in", max_year)

# read_temp_file.py
# Crystal Chang 
#
# Using a given file to read temperatures

# Inputting file name to read
filename=input("Temperature anomaly filename:")
# Opening and reading file 
infile=open(filename)
header=infile.readline()
# Using for loop to read temperatures from the inputted file
for line in infile:
    # Stripping whitespare off
    line=line.strip()
    # Separatting items in list
    year,temp=line.split(",")
    # Printing year, temperature
    print(year,float(temp))

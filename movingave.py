# moving_ave_csv2.py
# Crystal Chang 
#
# Using a given file to make a growing list of years and temperatures and calculate its moving averages

# Setting up list to prepare for adding within infile and outfile
temp_list=[]
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
    # Converting temperature to float while adding in new temperature values within list 
    temp_list.append(float(temp))
# Closing infile after reading
infile.close()
# Inputting in window size to prepare for outfile/csv file
k=int(input("Enter window size:"))
# Defining that index is the inputted value
index=k
# Making csv by using outfile function to write 
outfile=open("MovingAve2.csv", "w")
# Making titles on table of csv file
outfile.write("Year,Value\n")
# Using for loop to loop calculations based on inputted window size
for index in range(k,len(temp_list)-k):
    # Calculations for year
    year=1880+index
    # Calculations for average
    ave=sum(temp_list[index-k:index+k+1])/(2*k+1)
    outfile.write(f"{year},{ave:.4f}\n")
# Closing file
outfile.close()

# first_ave.py
# Crystal Chang 
#
# Using a given file to make a growing list of years and temperatures and calculate its moving averages

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
# Inputting in window size
k=int(input("Enter window size:"))
# Defining that index is the inputted value
index=k
# Calculations for year
year=1880+index
# Calculations for average
ave=sum(temp_list[index-k:index+k+1])/(2*k+1)
# Printing out moving average
print(f"{year},{ave:.4f}")

# moving_ave.py
# Crystal Chang 
#
# Using a given file to make a growing list of years and temperatures and calculate its moving averages

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
# Inputting in window size
k=int(input("Enter window size:"))
# Defining that index is the inputted value
index=k
# Using for loop to loop calculations based on inputted window size
for index in range(k,len(temp_list)-k):
    # Calculations for year
    year=1880+index
    # Calculations for average
    ave=sum(temp_list[index-k:index+k+1])/(2*k+1)
    # Printing out moving average
    print(f"{year},{ave:.4f}")


# moving_ave_csv.py
# Crystal Chang 
#
# Using a given file to make a growing list of years and temperatures and calculate its moving averages

# Setting up list to prepare for adding within infile and outfile
temp_list=[]
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
    # Converting temperature to float while adding in new temperature values within list 
    temp_list.append(float(temp))
# Closing infile after reading
infile.close()
# Inputting in window size to prepare for outfile/csv file
k=int(input("Enter window size:"))
# Defining that index is the inputted value
index=k
# Making csv by using outfile function to write 
outfile=open("MovingAve.csv", "w")
# Making titles on table of csv file
outfile.write("Year,Value\n")
# Using for loop to loop calculations based on inputted window size
for index in range(k,len(temp_list)-k):
    # Calculations for year
    year=1880+index
    # Calculations for average
    ave=sum(temp_list[index-k:index+k+1])/(2*k+1)
    outfile.write(f"{year},{ave:.4f}\n")
# Closing file
outfile.close()
    

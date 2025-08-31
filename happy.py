# happy1.py
#
# Crystal Chang 
# Building a dictionary and mapping to happiness index

# Defining the happiness file
HAPPYFILE = "happiness.csv"
# Define main()
def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    # print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    # lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    #read_gdp_data(happy_dict)

# Defining make_happy_dict
def make_happy_dict():
    # Creating empty dictionary to store
    happy_dict={}
    # Open file in read mode    
    infile=open(HAPPYFILE)
    # Making header of column
    header = infile.readline()
    # Creating a for loop to read lines from file
    for line in infile:
        # Stripping whitespace from line
        line=line.strip()
        # Splitting values in the line by comma
        line = line.split(",")
        # Storing country name and happiness index in variables
        country = line[0]
        happiness_index = line[2]
        # Storing values in dictionary
        happy_dict[country] = happiness_index
        # Printing country and happiness index
        print(country,happiness_index)
    # Close the input file
    infile.close()
    # Return dictionary
    return happy_dict

def read_gdp_data(happy_dict):
    return

def lookup_happiness_by_country(happy_dict):
    return

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(D.keys()):
        print(key, D[key])
        
main()

# happy2.py
#
# Crystal Chang 
# Building a dictionary and printing key values sorted by key

# Defining the happiness file
HAPPYFILE = "happiness.csv"
# Define main()
def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    # lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    #read_gdp_data(happy_dict)

def make_happy_dict():
    # Creating empty dictionary to store
    happy_dict={}
    # Open file in read mode    
    infile=open(HAPPYFILE)
    # Making header of column
    header = infile.readline()
    # Creating a for loop to read lines from file
    for line in infile:
        # Stripping whitespace from line
        line=line.strip()
        # Splitting values in the line by comma
        line = line.split(",")
        # Storing country name and happiness index in variables
        country = line[0]
        happiness_index = line[2]
        # Storing values in dictionary
        happy_dict[country] = happiness_index
        # Printing country and happiness index
        # print(country,happiness_index)
    # Close the input file
    infile.close()
    # Return dictionary
    return happy_dict

def read_gdp_data(happy_dict):
    return

def lookup_happiness_by_country(happy_dict):
    return

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(D.keys()):
        print(key, D[key])
        
main()

# happy3.py
#
# Crystal Chang 
# Querying the creating dictionary 

# Defining the happiness file
HAPPYFILE = "happiness.csv"
# Define main()
def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    # print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    #read_gdp_data(happy_dict)

# Defining make_happy_dict
def make_happy_dict():
    # Creating empty dictionary to store
    happy_dict={}
    # Open file in read mode    
    infile=open(HAPPYFILE)
    # Making header of column
    header = infile.readline()
    # Creating a for loop to read lines from file
    for line in infile:
        # Stripping whitespace from line
        line=line.strip()
        # Splitting values in the line by comma
        line = line.split(",")
        # Storing country name and happiness index in variables
        country = line[0]
        happiness_index = line[2]
        # Storing values in dictionary
        happy_dict[country] = happiness_index
        # Printing country and happiness index
        # print(country,happiness_index)
    # Close the input file
    infile.close()
    # Return dictionary
    return happy_dict

def read_gdp_data(happy_dict):
    return
# Defining lookup_happiness_by_country
def lookup_happiness_by_country(happy_dict):
    # Creating while loop to keep asking for a country until user exits
        while True:
            # Inputting country to lookup
            country=input("Enter a country to lookup or 'done' to exit:")
            # If country is within the file
            if country in happy_dict:
                # Happiness index is based on the country within the happy file
                happiness_index=happy_dict[country]
                # Printing happiness index when country is found
                print(happiness_index)
            # When user inputs "done" to exit
            elif country=="done":
                # Stops running
                break
            # When user inputs a country that isn't within the file
            else:
                # Printing country not found
                print(country,"not found")
                # Continues the loop until user exits
                continue
                # Returning happiness_index
                return happiness_index

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(D.keys()):
        print(key, D[key])
        
main()

# happy4.py
#
# Crystal Chang 
# Reading a file to add data

# Defining the happiness file
HAPPYFILE = "happiness.csv"
# Define main()
def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    # print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    # lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    read_gdp_data(happy_dict)

# Defining make_happy_dict
def make_happy_dict():
    # Creating empty dictionary to store
    happy_dict={}
    # Open file in read mode    
    infile=open(HAPPYFILE)
    # Reading header of column
    header = infile.readline()
    # Creating a for loop to read lines from file
    for line in infile:
        # Stripping whitespace from line
        line=line.strip()
        # Splitting values in the line by comma
        line = line.split(",")
        # Storing country name and happiness index in variables
        country = line[0]
        happiness_index = line[2]
        # Storing values in dictionary
        happy_dict[country] = happiness_index
        # Printing country and happiness index
        # print(country,happiness_index)
    # Close the input file
    infile.close()
    # Return dictionary
    return happy_dict

# Defining the tsv file
TSVFILE="world_pop_gdp.tsv"
# Defining read_gdp_data
def read_gdp_data(happy_dict):
    # Creating list of data
    gdp_data=[]
    # Open tsv file in read mode
    infile=open(TSVFILE)
    # Creating a for loop to read lines from file
    for line in infile:
        # Stripping whitespace
        line=line.strip()
        # Splitting values in line with comma
        line=line.split("\t")
        # Adding lines into list 
        gdp_data.append(line)
        # Storing country in variables
        country=line[0]
        # Storing population in variables
        population=line[1]
        # Replacing the space with commas for population
        population=population.replace(",","")
        # Storing gdp in variables
        gdp=line[2]
        # Stripping the dollar sign from gdp
        gdp=gdp.strip("$")
        # Replacing the space with commas for gdp
        gdp=gdp.replace(",","")
        # Printing country, population, gdp
        print(country+","+population+","+gdp)
    # Close the input file
    infile.close()
    # Return dictionary
    return gdp_data

# Defining lookup_happiness_by_country
def lookup_happiness_by_country(happy_dict):
    # Creating while loop to keep asking for a country until user exits
        while True:
            # Inputting country to lookup
            country=input("Enter a country to lookup or 'done' to exit:")
            # If country is within the file
            if country in happy_dict:
                # Happiness index is based on the country within the happy file
                happiness_index=happy_dict[country]
                # Printing happiness index when country is found
                print(happiness_index)
            # When user inputs "done" to exit
            elif country=="done":
                # Stops running
                break
            # When user inputs a country that isn't within the file
            else:
                # Printing country not found
                print(country,"not found")
                # Continues the loop until user exits
                continue
                # Returning happiness_index
                return happiness_index

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(D.keys()):
        print(key, D[key])
        
main()

# happy5.py
#
# Crystal Chang 
# Adding data to a file

# Defining the happiness file
HAPPYFILE = "happiness.csv"
# Define main()
def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    # print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    # lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    read_gdp_data(happy_dict)

# Defining make_happy_dict
def make_happy_dict():
    # Creating empty dictionary to store
    happy_dict={}
    # Open file in read mode    
    infile=open(HAPPYFILE)
    # Reading header of column
    header = infile.readline()
    # Creating a for loop to read lines from file
    for line in infile:
        # Stripping whitespace from line
        line=line.strip()
        # Splitting values in the line by comma
        line = line.split(",")
        # Storing country name and happiness index in variables
        country = line[0]
        happiness_index = line[2]
        # Storing values in dictionary
        happy_dict[country] = happiness_index
        # Printing country and happiness index
        # print(country,happiness_index)
    # Close the input file
    infile.close()
    # Return dictionary
    return happy_dict

# Defining the tsv file
TSVFILE="world_pop_gdp.tsv"
print("Country,Population in Millions,GDP per Capita,Happiness")
# Defining read_gdp_data
def read_gdp_data(happy_dict):
    # Creating list of data
    gdp_data=[]
    # Open tsv file in read mode
    infile=open(TSVFILE)
    # Creating a for loop to read lines from file
    for line in infile:
        # Stripping whitespace
        line=line.strip()
        # Splitting values in line with comma
        line=line.split("\t")
        # Adding lines into list 
        gdp_data.append(line)
        # Storing country in variables
        country=line[0]
        # Storing population in variables
        population=line[1]
        # Replacing the space with commas for population
        population=population.replace(",","")
        # Storing gdp in variables
        gdp=line[2]
        # Stripping the dollar sign from gdp
        gdp=gdp.strip("$")
        # Replacing the space with commas for gdp
        gdp=gdp.replace(",","")
        # Getting values from a dictionary
        happiness=happy_dict.get(country,0)
        # Boolean statement to check if whether or not to print output based on if country exists in dictionary or not
        if country in happy_dict:
            # Printing country, population, gdp
            print(country+","+population+","+gdp+","+str(happiness))
    # Close the input file
    infile.close()
    # Return dictionary
    return gdp_data

# Defining lookup_happiness_by_country
def lookup_happiness_by_country(happy_dict):
    # Creating while loop to keep asking for a country until user exits
        while True:
            # Inputting country to lookup
            country=input("Enter a country to lookup or 'done' to exit:")
            # If country is within the file
            if country in happy_dict:
                # Happiness index is based on the country within the happy file
                happiness_index=happy_dict[country]
                # Printing happiness index when country is found
                print(happiness_index)
            # When user inputs "done" to exit
            elif country=="done":
                # Stops running
                break
            # When user inputs a country that isn't within the file
            else:
                # Printing country not found
                print(country,"not found")
                # Continues the loop until user exits
                continue
                # Returning happiness_index
                return happiness_index

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(D.keys()):
        print(key, D[key])
        
main()

# happy6.py
#
# Crystal Chang 
# Changing output of data file

# Defining the happiness file
HAPPYFILE = "happiness.csv"
# Define main()
def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    # print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    # lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    read_gdp_data(happy_dict)

# Defining make_happy_dict
def make_happy_dict():
    # Creating empty dictionary to store
    happy_dict={}
    # Open file in read mode    
    infile=open(HAPPYFILE)
    # Reading header of column
    header = infile.readline()
    # Creating a for loop to read lines from file
    for line in infile:
        # Stripping whitespace from line
        line=line.strip()
        # Splitting values in the line by comma
        line = line.split(",")
        # Storing country name and happiness index in variables
        country = line[0]
        happiness_index = line[2]
        # Storing values in dictionary
        happy_dict[country] = happiness_index
        # Printing country and happiness index
        # print(country,happiness_index)
    # Close the input file
    infile.close()
    # Return dictionary
    return happy_dict

# Defining the tsv file
TSVFILE="world_pop_gdp.tsv"
print("Country,Population in Millions,GDP per Capita,Happiness")
# Defining read_gdp_data
def read_gdp_data(happy_dict):
    # Creating list of data
    gdp_data=[]
    # Open tsv file in read mode
    infile=open(TSVFILE)
    # Accounting for the header
    infile.readline()
    # Creating a for loop to read lines from file
    for line in infile:
        # Stripping whitespace
        line=line.strip()
        # Splitting values in line with comma
        line=line.split("\t")
        # Adding lines into list 
        gdp_data.append(line)
        # Storing country in variables
        country=line[0]
        # Storing population in variables
        population=line[1]
        # Replacing the space with commas for population
        population=population.replace(",","")
        # Storing gdp in variables
        gdp=line[2]
        # Stripping the dollar sign from gdp
        gdp=gdp.strip("$")
        # Replacing the space with commas for gdp
        gdp=gdp.replace(",","")
        # Getting values from a dictionary
        happiness=happy_dict.get(country,0)
        # Boolean statement to check if population is greater than 100 million
        if (float(population)>=100):
            # Boolean statement to check if whether or not to print output based on if country exists in dictionary or not
            if country in happy_dict:
                # Printing country, population, gdp
                print(country+","+population+","+gdp+","+str(happiness))
    # Close the input file
    infile.close()
    # Return dictionary
    return gdp_data

# Defining lookup_happiness_by_country
def lookup_happiness_by_country(happy_dict):
    # Creating while loop to keep asking for a country until user exits
        while True:
            # Inputting country to lookup
            country=input("Enter a country to lookup or 'done' to exit:")
            # If country is within the file
            if country in happy_dict:
                # Happiness index is based on the country within the happy file
                happiness_index=happy_dict[country]
                # Printing happiness index when country is found
                print(happiness_index)
            # When user inputs "done" to exit
            elif country=="done":
                # Stops running
                break
            # When user inputs a country that isn't within the file
            else:
                # Printing country not found
                print(country,"not found")
                # Continues the loop until user exits
                continue
                # Returning happiness_index
                return happiness_index

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(D.keys()):
        print(key, D[key])
        
main()

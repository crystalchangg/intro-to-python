# trycat.py
# Crystal Chang
#
# Opening a file and printing every line within the file, while accounting for files that cannot be opened

# Loop inputted file name so that user can keep inputting file names when file is invalid
while True:
    # Inputting file name
    filename=input("Enter a file name to open:")
    # Testing of block of code with try and except
    try:
        # Opening file based on inputted file name
        infile=open(filename,"r")
        # When file is opened, the program stops the loop
        break
    # When file is not opened, the loop continues and prints out "could not open file name"
    except:
        print("Could not open '{}'".format(filename))
        continue
# Loop that reads and prints line by line of opened file when file is opened
for line in infile:
        line=line.strip()
        print(line)

# cat.py
# Crystal Chang 
#
# Opening a file name and printing every line within the file

# Inputting file name
filename=input("Enter a file name to open:")
# Opening file based on inputted file name
infile=open(filename,"r")
# Loop that reads and prints line by line of opened file
for line in infile:
    line=line.strip()
    print(line)
